#!/usr/bin/env python3
"""
Setup script for ConnectOnion Error Recovery Tool
"""

import subprocess
import sys
import os
from pathlib import Path

def install_connectonion():
    """Install ConnectOnion if not already installed."""
    try:
        import connectonion
        print("✅ ConnectOnion is already installed")
        return True
    except ImportError:
        print("📦 Installing ConnectOnion...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "connectonion"], check=True)
            print("✅ ConnectOnion installed successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install ConnectOnion: {e}")
            return False

def create_symlink():
    """Create a symlink or batch file for the connectonion command."""
    if sys.platform == "win32":
        # Create a batch file for Windows
        batch_content = '''@echo off
python "%~dp0connectonion_cli.py" %*
'''
        batch_path = Path("connectonion.bat")
        batch_path.write_text(batch_content)
        print("✅ Created connectonion.bat - you can now use 'connectonion fix <command>'")
    else:
        # Create a symlink for Unix-like systems
        try:
            os.symlink("connectonion_cli.py", "connectonion")
            os.chmod("connectonion", 0o755)
            print("✅ Created connectonion symlink")
        except OSError:
            print("⚠️  Could not create symlink. You can run: python connectonion_cli.py fix <command>")

def main():
    print("🔧 Setting up ConnectOnion Error Recovery Tool")
    print("=" * 50)
    
    # Install ConnectOnion
    if not install_connectonion():
        print("❌ Setup failed - could not install ConnectOnion")
        sys.exit(1)
    
    # Create command-line interface
    create_symlink()
    
    print("\n🎉 Setup complete!")
    print("\nUsage examples:")
    print("  connectonion fix python app.py")
    print("  connectonion fix python -c \"import requests\"")
    print("  connectonion fix python test_script.py")

if __name__ == "__main__":
    main()

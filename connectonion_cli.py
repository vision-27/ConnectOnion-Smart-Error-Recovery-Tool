#!/usr/bin/env python3
"""
ConnectOnion CLI - Smart Error Recovery Tool
Usage: connectonion fix [command]
"""

import sys
import subprocess
import argparse
from pathlib import Path
from error_recovery_agent import fix_error

def run_command_and_catch_errors(command: str) -> str:
    """Run a command and return the error if it fails."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

def main():
    parser = argparse.ArgumentParser(
        description="ConnectOnion Smart Error Recovery Tool",
        prog="connectonion"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Fix command
    fix_parser = subparsers.add_parser("fix", help="Fix errors in a command")
    fix_parser.add_argument("command", nargs="+", help="Command to run and fix if it fails")
    
    args = parser.parse_args()
    
    if args.command == "fix":
        if not hasattr(args, 'command') or not args.command:
            print("❌ Error: Please provide a command to run")
            print("Usage: connectonion fix <your-command>")
            print("Example: connectonion fix python app.py")
            sys.exit(1)
        
        # Join the command parts
        command_to_run = " ".join(args.command)
        
        print(f"🚀 Running: {command_to_run}")
        print("=" * 50)
        
        # First, try to run the command
        output = run_command_and_catch_errors(command_to_run)
        
        # If there was an error, try to fix it
        if "Error:" in output or "Traceback" in output or "ModuleNotFoundError" in output:
            print("❌ Command failed with error:")
            print(output)
            print("\n🔧 Attempting to fix the error...")
            print("=" * 50)
            
            # Use the ConnectOnion agent to fix the error
            fix_result = fix_error(output)
            print(fix_result)
            
            # Try running the command again
            print("\n🔄 Trying to run the command again...")
            print("=" * 50)
            final_output = run_command_and_catch_errors(command_to_run)
            
            if "Error:" in final_output or "Traceback" in final_output:
                print("❌ Still failing after fix attempt:")
                print(final_output)
                print("\n💡 The error might need manual intervention.")
            else:
                print("✅ Fixed! Command now runs successfully:")
                print(final_output)
        else:
            print("✅ Command ran successfully:")
            print(output)
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

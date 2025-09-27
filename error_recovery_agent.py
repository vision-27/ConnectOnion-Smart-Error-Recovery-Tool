#!/usr/bin/env python3
"""
Smart Error Recovery Agent using ConnectOnion
Automatically detects and fixes common Python errors
"""

import subprocess
import sys
import re
import os
from pathlib import Path
from typing import List, Dict, Optional
from connectonion import Agent

def analyze_error(error_output: str) -> Dict[str, str]:
    """Analyze error output to determine the type and solution."""
    error_info = {
        "type": "unknown",
        "module": None,
        "suggestion": "Unknown error - manual intervention required"
    }
    
    # ModuleNotFoundError detection
    if "ModuleNotFoundError" in error_output:
        match = re.search(r"No module named '([^']+)'", error_output)
        if match:
            error_info["type"] = "missing_module"
            error_info["module"] = match.group(1)
            error_info["suggestion"] = f"Install missing module: pip install {match.group(1)}"
    
    # ImportError detection
    elif "ImportError" in error_output:
        match = re.search(r"cannot import name '([^']+)'", error_output)
        if match:
            error_info["type"] = "import_error"
            error_info["module"] = match.group(1)
            error_info["suggestion"] = f"Check import statement for '{match.group(1)}'"
    
    # FileNotFoundError detection
    elif "FileNotFoundError" in error_output:
        match = re.search(r"\[Errno 2\] No such file or directory: '([^']+)'", error_output)
        if match:
            error_info["type"] = "missing_file"
            error_info["module"] = match.group(1)
            error_info["suggestion"] = f"Create missing file: {match.group(1)}"
    
    # SyntaxError detection
    elif "SyntaxError" in error_output:
        error_info["type"] = "syntax_error"
        error_info["suggestion"] = "Check Python syntax in the file"
    
    # PermissionError detection
    elif "PermissionError" in error_output:
        error_info["type"] = "permission_error"
        error_info["suggestion"] = "Check file permissions or run with appropriate privileges"
    
    return error_info

def install_package(package_name: str) -> str:
    """Install a Python package using pip."""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", package_name],
            capture_output=True,
            text=True,
            check=True
        )
        return f"✅ Successfully installed {package_name}"
    except subprocess.CalledProcessError as e:
        return f"❌ Failed to install {package_name}: {e.stderr}"

def check_package_installed(package_name: str) -> bool:
    """Check if a package is already installed."""
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "show", package_name],
            capture_output=True,
            check=True
        )
        return True
    except subprocess.CalledProcessError:
        return False

def run_command(command: str) -> str:
    """Run a shell command and return the output."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        return f"✅ Command successful:\n{result.stdout}"
    except subprocess.CalledProcessError as e:
        return f"❌ Command failed:\n{e.stderr}"

def create_missing_file(filepath: str) -> str:
    """Create a missing file with basic content."""
    try:
        path = Path(filepath)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        # Create basic Python file if it's a .py file
        if path.suffix == '.py':
            content = '''#!/usr/bin/env python3
"""
Auto-generated file by ConnectOnion Error Recovery Agent
"""
'''
            path.write_text(content)
            return f"✅ Created missing file: {filepath}"
        else:
            path.touch()
            return f"✅ Created missing file: {filepath}"
    except Exception as e:
        return f"❌ Failed to create file {filepath}: {e}"

def suggest_fix(error_info: Dict[str, str]) -> str:
    """Suggest a fix based on error analysis."""
    if error_info["type"] == "missing_module":
        module = error_info["module"]
        if not check_package_installed(module):
            return f"🔍 I see the error. Installing {module}...\n{install_package(module)}"
        else:
            return f"✅ Module {module} is already installed. The error might be elsewhere."
    
    elif error_info["type"] == "missing_file":
        filepath = error_info["module"]
        return f"🔍 I see the error. Creating missing file...\n{create_missing_file(filepath)}"
    
    else:
        return f"🔍 I see the error. {error_info['suggestion']}"

# Create the error recovery agent
error_recovery_agent = Agent(
    name="error_recovery",
    system_prompt="""You are a smart error recovery assistant. Your job is to:

1. Analyze error messages and understand what went wrong
2. Provide clear, actionable solutions
3. Automatically fix common issues when possible
4. Be helpful and encouraging in your responses

When you see an error:
- First analyze what type of error it is
- Suggest the most appropriate fix
- If it's a missing module, install it automatically
- If it's a missing file, create it
- Always explain what you're doing and why

Be concise but thorough. Use emojis to make your responses friendly and clear.""",
    tools=[analyze_error, install_package, check_package_installed, run_command, create_missing_file, suggest_fix],
    max_iterations=5
)

def fix_error(error_message: str) -> str:
    """Main function to fix an error using the ConnectOnion agent."""
    prompt = f"""I encountered this error:

```
{error_message}
```

Please analyze it and fix it automatically if possible. If you can fix it, run the original command again to verify the fix works."""
    
    return error_recovery_agent.input(prompt)

if __name__ == "__main__":
    # Example usage
    if len(sys.argv) > 1:
        error_message = sys.argv[1]
        result = fix_error(error_message)
        print(result)
    else:
        print("Usage: python error_recovery_agent.py '<error_message>'")
        print("\nExample:")
        print("python error_recovery_agent.py \"ModuleNotFoundError: No module named 'requests'\"")

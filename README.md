# ConnectOnion Smart Error Recovery Tool

A powerful AI-powered error recovery tool built with ConnectOnion that automatically detects and fixes common Python errors.

## Features

- 🔍 **Smart Error Detection**: Automatically identifies error types (missing modules, syntax errors, etc.)
- 🛠️ **Automatic Fixes**: Installs missing packages, creates missing files, and more
- 🤖 **AI-Powered**: Uses ConnectOnion agents to understand and resolve complex errors
- 🚀 **Easy to Use**: Simple CLI interface with `connectonion fix` command

## Quick Start

### 1. Setup

```bash
# Install ConnectOnion and setup the tool
python setup.py
```

### 2. Usage

```bash
# Fix errors in any Python command
connectonion fix python app.py
connectonion fix python -c "import requests"
connectonion fix python test_script.py
```

### 3. Example

```bash
$ python test_app.py
Error: ModuleNotFoundError: No module named 'requests'

$ connectonion fix python test_app.py
🔍 I see the error. Installing requests...
✅ Successfully installed requests
🚀 Server starting on http://localhost:8000
```

## How It Works

The tool uses a ConnectOnion agent with specialized tools:

- **Error Analysis**: Detects error types and suggests fixes
- **Package Installation**: Automatically installs missing Python packages
- **File Creation**: Creates missing files when needed
- **Command Execution**: Runs commands and captures errors
- **Smart Recovery**: Uses AI to understand context and provide appropriate solutions

## Supported Error Types

- ✅ **Missing Modules**: `ModuleNotFoundError: No module named 'requests'`
- ✅ **Import Errors**: `ImportError: cannot import name 'xyz'`
- ✅ **Missing Files**: `FileNotFoundError: [Errno 2] No such file or directory`
- ✅ **Syntax Errors**: Basic Python syntax issues
- ✅ **Permission Errors**: File permission problems

## Architecture

```
connectonion_cli.py          # Main CLI interface
├── error_recovery_agent.py   # ConnectOnion agent with tools
├── setup.py                 # Installation script
└── test_app.py             # Test application
```

## ConnectOnion Agent Tools

The error recovery agent includes these specialized tools:

1. **analyze_error()** - Analyzes error messages and determines type
2. **install_package()** - Installs missing Python packages
3. **check_package_installed()** - Verifies if packages are installed
4. **run_command()** - Executes shell commands safely
5. **create_missing_file()** - Creates missing files
6. **suggest_fix()** - Provides intelligent fix suggestions

## Advanced Usage

### Custom Error Handling

You can extend the agent with custom error handlers:

```python
from error_recovery_agent import error_recovery_agent

# Add custom tools
def custom_fix_tool(error: str) -> str:
    """Custom error handling logic."""
    # Your custom logic here
    return "Custom fix applied"

# Add to agent
error_recovery_agent.add_tool(custom_fix_tool)
```

### Integration with Other Tools

The ConnectOnion agent can be integrated with other development tools:

```python
# Use in CI/CD pipelines
result = error_recovery_agent.input("Fix this build error: ...")

# Use in development workflows
result = error_recovery_agent.input("Analyze and fix this test failure: ...")
```

## Best Practices

1. **Always test fixes**: The tool re-runs commands to verify fixes work
2. **Use specific error messages**: More detailed errors lead to better fixes
3. **Check permissions**: Some fixes may require appropriate system permissions
4. **Review changes**: Always review what the tool changes before committing

## Troubleshooting

### Common Issues

- **Permission denied**: Run with appropriate privileges for system-level changes
- **Network issues**: Ensure internet connection for package installations
- **Complex errors**: Some errors may need manual intervention

### Debug Mode

Enable debug output by setting environment variable:

```bash
export CONNECTONION_DEBUG=1
connectonion fix python app.py
```

## Contributing

This tool demonstrates ConnectOnion's capabilities for building intelligent development tools. You can extend it with:

- More error types
- Custom fix strategies
- Integration with specific frameworks
- Advanced error analysis

## Learn More

- [ConnectOnion Documentation](https://github.com/wu-changxing/connectonion)
- [ConnectOnion Examples](https://github.com/wu-changxing/connectonion/tree/main/examples)
- [AI Agent Development](https://connectonion.readthedocs.io/)

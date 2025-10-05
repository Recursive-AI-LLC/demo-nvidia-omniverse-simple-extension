# Extension List Printer

## Demo Video
See a quick video of how this was made with Recursive AI's bot platform:
[demo.mp4](https://coppy.me/4D/demo.mp4)

## Overview

The Extension List Printer is a utility extension for Nvidia Omniverse that prints a comprehensive list of all installed extensions in the application. This is useful for debugging, documentation, and understanding what extensions are available in your Omniverse environment.

## Features

- Lists all installed extensions in the Omniverse application
- Displays key information for each extension:
  - Extension ID
  - Extension name
  - Version number
  - Enabled/Disabled status
- Provides a summary count of total, enabled, and disabled extensions
- Outputs to the console/log using Omniverse's logging system

## Installation

### Method 1: Copy to Extensions Folder

1. Copy the entire `omni.example.extension_lister` folder to your Omniverse extensions directory:
   - Windows: `%LOCALAPPDATA%\ov\pkg\<app-name>\exts\`
   - Linux: `~/.local/share/ov/pkg/<app-name>/exts/`

2. Restart the Omniverse application or refresh the Extension Manager

### Method 2: Development Mode (Folder Linking)

1. Open your Omniverse application (e.g., Kit, Create, Code)

2. Add the extension folder path to the extension search paths:
   - Go to **Window** → **Extensions**
   - Click the **hamburger menu** (three lines) → **Settings**
   - Add the parent folder path containing `omni.example.extension_lister` to the search paths

3. The extension should now appear in the Extension Manager

## Usage

### Enabling the Extension

1. Open the **Extension Manager** (Window → Extensions)
2. Search for "Extension List Printer"
3. Toggle the extension to **ON**

### Viewing the Output

When the extension is enabled, it automatically prints the list of all extensions to the console/log.

**To view the output:**

- **Console Window**: Go to **Window** → **Console** to see the output in real-time
- **Log File**: Check the log files in your Kit application's log directory:
  - Windows: `%LOCALAPPDATA%\ov\pkg\<app-name>\logs\`
  - Linux: `~/.local/share/ov/pkg/<app-name>/logs/`

### Example Output

```
================================================================================
INSTALLED EXTENSIONS LIST
================================================================================
Extension ID: omni.kit.window.console-1.0.0
  Name: omni.kit.window.console
  Version: 1.0.0
  Status: ENABLED
--------------------------------------------------------------------------------
Extension ID: omni.ui-2.14.0
  Name: omni.ui
  Version: 2.14.0
  Status: ENABLED
--------------------------------------------------------------------------------
Extension ID: omni.example.extension_lister-1.0.0
  Name: omni.example.extension_lister
  Version: 1.0.0
  Status: ENABLED
--------------------------------------------------------------------------------
================================================================================
SUMMARY: 3 total extensions (3 enabled, 0 disabled)
================================================================================
```

## Technical Details

### Dependencies

- `omni.kit.app` - Required for accessing the Extension Manager API

### Architecture

The extension implements the `omni.ext.IExt` interface with:
- `on_startup(ext_id)` - Retrieves and prints the extension list when enabled
- `on_shutdown()` - Performs cleanup when disabled

### API Usage

The extension uses the Extension Manager API:
```python
manager = omni.kit.app.get_app().get_extension_manager()
extensions = manager.get_extensions()
```

## Use Cases

- **Debugging**: Quickly see what extensions are installed and enabled
- **Documentation**: Generate a list of extensions for documentation purposes
- **Development**: Understand the extension ecosystem in your application
- **Troubleshooting**: Verify extension installation and status

## Version History

See [CHANGELOG.md](CHANGELOG.md) for version history.

## License

This extension is provided as an example for educational purposes.

## Support

For issues or questions, please refer to the Nvidia Omniverse documentation:
- [Omniverse Kit SDK Documentation](https://docs.omniverse.nvidia.com/kit/docs/kit-manual/latest/index.html)
- [Extension Development Guide](https://docs.omniverse.nvidia.com/kit/docs/kit-manual/latest/guide/extensions_basic.html)

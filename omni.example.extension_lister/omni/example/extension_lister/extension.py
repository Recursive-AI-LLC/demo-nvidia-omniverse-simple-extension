import omni.ext
import omni.kit.app
import carb


class ExtensionListerExtension(omni.ext.IExt):
    """Extension that prints a list of all installed extensions."""

    def on_startup(self, ext_id: str):
        """Called when the extension is enabled.
        
        Args:
            ext_id: Extension ID (name-version)
        """
        carb.log_info(f"[{ext_id}] Extension List Printer starting up")
        
        try:
            # Get the extension manager
            manager = omni.kit.app.get_app().get_extension_manager()
            
            # Get all extensions
            extensions = manager.get_extensions()
            
            # Print header
            carb.log_info("=" * 80)
            carb.log_info("INSTALLED EXTENSIONS LIST")
            carb.log_info("=" * 80)
            
            # Count extensions
            total_count = 0
            enabled_count = 0
            
            # Iterate through all extensions and print their information
            for ext in extensions:
                total_count += 1
                ext_id = ext.get("id", "N/A")
                ext_name = ext.get("name", "N/A")
                ext_version = ext.get("version", "N/A")
                ext_enabled = ext.get("enabled", False)
                
                if ext_enabled:
                    enabled_count += 1
                    status = "ENABLED"
                else:
                    status = "DISABLED"
                
                # Print extension information
                carb.log_info(f"Extension ID: {ext_id}")
                carb.log_info(f"  Name: {ext_name}")
                carb.log_info(f"  Version: {ext_version}")
                carb.log_info(f"  Status: {status}")
                carb.log_info("-" * 80)
            
            # Print summary
            carb.log_info("=" * 80)
            carb.log_info(f"SUMMARY: {total_count} total extensions ({enabled_count} enabled, {total_count - enabled_count} disabled)")
            carb.log_info("=" * 80)
            
        except Exception as e:
            carb.log_error(f"Error listing extensions: {e}")
            carb.log_error("Extension List Printer failed to retrieve extension information")

    def on_shutdown(self):
        """Called when the extension is disabled."""
        carb.log_info("Extension List Printer shutting down")

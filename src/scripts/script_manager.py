class ScriptManager:
    def __init__(self):
        self.scripts = {
            "greeting": "Hello, how can I assist you today?",
            "product_info": "Our product offers a range of features including...",
            "closing": "Thank you for your time. Have a great day!"
        }

    def get_script(self, script_name):
        """Fetch the script based on the script name."""
        return self.scripts.get(script_name, "Script not found")

    def display_script(self, script_name):
        """Display the script to the operator."""
        script = self.get_script(script_name)
        print(f"Script: {script}")

# Example usage
if __name__ == "__main__":
    script_manager = ScriptManager()
    script_manager.display_script("greeting")
    script_manager.display_script("product_info")
    script_manager.display_script("closing") 
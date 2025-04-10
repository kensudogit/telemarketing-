class IVRSystem:
    def __init__(self):
        self.menu_options = {
            "1": "For account information, press 1",
            "2": "For technical support, press 2",
            "3": "To speak with a representative, press 3"
        }

    def play_menu(self):
        """Play the IVR menu options."""
        for option in self.menu_options.values():
            print(option)

    def handle_input(self, user_input):
        """Handle user input and provide appropriate response."""
        if user_input in self.menu_options:
            print(f"You selected: {self.menu_options[user_input]}")
        else:
            print("Invalid selection. Please try again.")

# Example usage
if __name__ == "__main__":
    ivr_system = IVRSystem()
    ivr_system.play_menu()
    ivr_system.handle_input("1")
    ivr_system.handle_input("4") 
class AIAssist:
    def __init__(self, script_manager):
        self.script_manager = script_manager

    def analyze_customer_input(self, customer_input):
        """Analyze customer input and suggest a script."""
        # Simple keyword-based analysis for demonstration
        if "price" in customer_input:
            return "product_info"
        elif "thank you" in customer_input:
            return "closing"
        else:
            return "greeting"

    def suggest_script(self, customer_input):
        """Suggest a script based on customer input."""
        script_name = self.analyze_customer_input(customer_input)
        self.script_manager.display_script(script_name)

# Example usage
if __name__ == "__main__":
    from script_manager import ScriptManager
    script_manager = ScriptManager()
    ai_assist = AIAssist(script_manager)

    # Simulate customer input
    ai_assist.suggest_script("Can you tell me about the price?")
    ai_assist.suggest_script("Thank you for your help!") 
class ReportManager:
    def __init__(self):
        self.call_data = []  # List to store call data

    def log_call(self, operator_id, phone_number, success):
        """Log call data for reporting."""
        self.call_data.append({
            "operator_id": operator_id,
            "phone_number": phone_number,
            "success": success
        })

    def generate_report(self):
        """Generate a simple report of call data."""
        total_calls = len(self.call_data)
        successful_calls = sum(1 for call in self.call_data if call["success"])
        success_rate = (successful_calls / total_calls) * 100 if total_calls > 0 else 0
        print(f"Total Calls: {total_calls}, Successful Calls: {successful_calls}, Success Rate: {success_rate:.2f}%")

# Example usage
if __name__ == "__main__":
    report_manager = ReportManager()
    report_manager.log_call("op1", "123-456-7890", True)
    report_manager.log_call("op2", "098-765-4321", False)
    report_manager.generate_report() 
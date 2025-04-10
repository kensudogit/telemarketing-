import datetime

class ComplianceManager:
    def __init__(self):
        self.dnc_list = set()  # Set to store Do Not Call numbers
        self.call_records = []  # List to store call records
        self.allowed_call_hours = (9, 17)  # Calls allowed between 9 AM and 5 PM

    def record_call(self, phone_number, call_data):
        """Record call data for compliance."""
        self.call_records.append({
            "phone_number": phone_number,
            "call_data": call_data,
            "timestamp": datetime.datetime.now()
        })
        print(f"Call recorded for {phone_number}")

    def is_allowed_time(self):
        """Check if the current time is within allowed call hours."""
        current_hour = datetime.datetime.now().hour
        return self.allowed_call_hours[0] <= current_hour < self.allowed_call_hours[1]

    def add_to_dnc(self, phone_number):
        """Add a phone number to the Do Not Call list."""
        self.dnc_list.add(phone_number)
        print(f"Added {phone_number} to DNC list")

    def is_on_dnc(self, phone_number):
        """Check if a phone number is on the Do Not Call list."""
        return phone_number in self.dnc_list

# Example usage
if __name__ == "__main__":
    compliance_manager = ComplianceManager()
    compliance_manager.add_to_dnc("123-456-7890")
    print(compliance_manager.is_on_dnc("123-456-7890"))
    print(compliance_manager.is_allowed_time())
    compliance_manager.record_call("098-765-4321", "Sample call data") 
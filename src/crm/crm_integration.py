class CRMIntegration:
    def __init__(self):
        # This could be extended to include API keys, endpoints, etc.
        self.customers = {
            "123-456-7890": {"name": "John Doe", "history": "Previous call on 2023-10-01"},
            "098-765-4321": {"name": "Jane Smith", "history": "Previous call on 2023-09-15"}
        }

    def get_customer_info(self, phone_number):
        """Fetch customer information based on phone number."""
        return self.customers.get(phone_number, None)

# Example usage
if __name__ == "__main__":
    crm = CRMIntegration()
    customer_info = crm.get_customer_info("123-456-7890")
    if customer_info:
        print(f"Customer Name: {customer_info['name']}, History: {customer_info['history']}")
    else:
        print("Customer not found") 
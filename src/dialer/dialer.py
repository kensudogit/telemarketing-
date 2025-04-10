import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OperatorStatus:
    def __init__(self, operator_id, is_available=True):
        self.operator_id = operator_id
        self.is_available = is_available


class PredictiveDialer:
    def __init__(self):
        self.operators = []  # List of OperatorStatus
        self.call_queue = []  # Queue of phone numbers to call

    def add_operator(self, operator_id):
        self.operators.append(OperatorStatus(operator_id))

    def add_call(self, phone_number):
        if phone_number:  # Simple validation
            self.call_queue.append(phone_number)
            logging.info(f"Added call to queue: {phone_number}")
        else:
            logging.error("Invalid phone number provided")

    def get_next_call(self):
        for operator in self.operators:
            if operator.is_available:
                if self.call_queue:
                    next_call = self.call_queue.pop(0)
                    operator.is_available = False  # Mark operator as busy
                    logging.info(f"Operator {operator.operator_id} is calling {next_call}")
                    return operator.operator_id, next_call
        logging.warning("No available operators or calls")
        return None, None  # No available operators or calls

    def mark_operator_available(self, operator_id):
        for operator in self.operators:
            if operator.operator_id == operator_id:
                operator.is_available = True
                break

    def complete_call(self, operator_id):
        """Mark the operator as available after completing a call."""
        self.mark_operator_available(operator_id)
        logging.info(f"Operator {operator_id} has completed the call and is now available.")

# Example usage
if __name__ == "__main__":
    dialer = PredictiveDialer()
    dialer.add_operator("op1")
    dialer.add_operator("op2")
    dialer.add_call("123-456-7890")
    dialer.add_call("")  # Invalid number for testing

    operator_id, phone_number = dialer.get_next_call()
    if operator_id:
        print(f"Operator {operator_id} is calling {phone_number}")
        # Simulate call completion
        dialer.complete_call(operator_id)
    else:
        print("No available operators or calls") 
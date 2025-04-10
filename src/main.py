from dialer.dialer import PredictiveDialer
from crm.crm_integration import CRMIntegration
from scripts.script_manager import ScriptManager
from scripts.ai_assist import AIAssist
from voice_recognition.voice_recognition import VoiceRecognition
from reports.report_manager import ReportManager
from omnichannel.omnichannel_manager import OmnichannelManager
from ivr.ivr_system import IVRSystem
from compliance.compliance_manager import ComplianceManager


def main():
    # Initialize components
    dialer = PredictiveDialer()
    crm = CRMIntegration()
    script_manager = ScriptManager()
    ai_assist = AIAssist(script_manager)
    voice_recognition = VoiceRecognition()
    report_manager = ReportManager()
    omnichannel_manager = OmnichannelManager()
    ivr_system = IVRSystem()
    compliance_manager = ComplianceManager()

    # Example integration
    # Add operators and calls
    dialer.add_operator("op1")
    dialer.add_operator("op2")
    dialer.add_call("123-456-7890")
    dialer.add_call("098-765-4321")

    # Process a call
    operator_id, phone_number = dialer.get_next_call()
    if operator_id:
        print(f"Operator {operator_id} is calling {phone_number}")
        # Simulate call completion
        dialer.complete_call(operator_id)
        # Log the call
        report_manager.log_call(operator_id, phone_number, True)
        # Check compliance
        if compliance_manager.is_allowed_time() and not compliance_manager.is_on_dnc(phone_number):
            compliance_manager.record_call(phone_number, "Sample call data")
        else:
            print("Call not allowed due to compliance restrictions.")

    # Use CRM to get customer info
    customer_info = crm.get_customer_info(phone_number)
    if customer_info:
        print(f"Customer Name: {customer_info['name']}, History: {customer_info['history']}")

    # Use AI Assist
    transcribed_text = voice_recognition.transcribe_audio("audio_with_price_question")
    ai_assist.suggest_script(transcribed_text)

    # Send a message via omnichannel
    omnichannel_manager.send_sms(phone_number, "Follow-up message via SMS")

    # Play IVR menu
    ivr_system.play_menu()
    ivr_system.handle_input("1")

    # Generate report
    report_manager.generate_report()


if __name__ == "__main__":
    main() 
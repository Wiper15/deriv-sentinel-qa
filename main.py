import vertexai
from architect import TestArchitect
from sentinel import ComplianceSentinel

# Initialize Google Cloud Vertex AI
PROJECT_ID = "YOUR_PROJECT_ID" 
vertexai.init(project=PROJECT_ID, location="us-central1")

def run_self_healing_pipeline(goal):
    architect = TestArchitect()
    sentinel = ComplianceSentinel()

    # Phase 1: Generation & Audit
    print(f"🛠️ Building test for: {goal}")
    code = architect.generate_test(goal)
    
    report = sentinel.audit_code(code)
    if "FAIL" in report:
        print(f"❌ Security Blocked: {report}")
        return

    # Phase 2: Simulated Execution & Healing
    # Let's simulate a 'Button Not Found' error
    execution_error = "Error: locator('button#withdraw').click() failed. Element not found."
    
    if "not found" in execution_error.lower():
        print("🔧 UI Change Detected. Starting Self-Healing...")
        
        # Phase 3: Healing (Architect reasons through the error)
        heal_prompt = f"The test failed with error: {execution_error}. Rewrite the code using a more resilient selector (like text or ARIA labels)."
        healed_code = architect.generate_test(heal_prompt)
        
        print("✅ Code Healed. Sending for Re-Audit...")
        final_report = sentinel.audit_code(healed_code)
        
        if "PASS" in final_report:
            print("🚀 Healed Test Approved & Ready for Deployment.")
            print(f"FINAL CODE:\n{healed_code}")

if __name__ == "__main__":
    run_self_healing_pipeline("Test the BTC withdrawal flow")

import vertexai
from architect import TestArchitect
from sentinel import ComplianceSentinel

vertexai.init(project="YOUR_PROJECT_ID", location="us-central1")

def run_pipeline(user_goal):
    architect = TestArchitect()
    sentinel = ComplianceSentinel()

    # Step 1: Generate
    print(f"🛠️ Architect is building test for: {user_goal}")
    generated_code = architect.generate_test(user_goal)

    # Step 2: Audit
    print("🛡️ Sentinel is auditing for compliance...")
    audit_report = sentinel.audit_code(generated_code)

    if "PASS" in audit_report:
        print("✅ Compliance Verified. Ready for Execution.")
        # In a full demo, you would save and run this with Playwright
    else:
        print(f"❌ Compliance Failed: {audit_report}")

if __name__ == "__main__":
    goal = "Verify the BTC deposit button on the Deriv dashboard"
    run_pipeline(goal)
  

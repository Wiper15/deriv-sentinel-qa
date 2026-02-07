from vertexai.generative_models import GenerativeModel

class ComplianceSentinel:
    def __init__(self):
        # Using Flash for speed/efficiency in auditing
        self.model = GenerativeModel("gemini-1.5-flash")

    def audit_code(self, code):
        prompt = f"""
        Act as a Fintech Compliance Auditor. Audit this code against PCI DSS 4.0 and GDPR:
        {code}
        Check for:
        1. Hardcoded passwords/PII
        2. Missing Risk Warning interactions
        Return JSON: {{"status": "PASS/FAIL", "reason": "..."}}
        """
        response = self.model.generate_content(prompt)
        return response.text
      

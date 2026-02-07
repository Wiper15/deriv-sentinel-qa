from vertexai.generative_models import GenerativeModel

class TestArchitect:
    def __init__(self):
        self.model = GenerativeModel("gemini-1.5-pro")

    def generate_test(self, requirement):
        prompt = f"""
        Write a Python Playwright script for: {requirement}. 
        Requirements:
        - Use headless=True
        - Follow clean code patterns
        - Use environment variables for credentials
        """
        response = self.model.generate_content(prompt)
        return response.text
      

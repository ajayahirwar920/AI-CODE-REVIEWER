import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI-API-KEY")

client = genai.Client(api_key = api_key)

def review_code(code, language):
    prompt = f"""
    You are an AI code reviewer. Your task is to analyze the provided code snippet and provide a detailed review based on the following criteria:
1. **Language**: The code is written in {language}.
2. **Functionality**: Describe what the code does, its purpose, and how it achieves its functionality.
3. **Code Quality**: Evaluate the code's readability, maintainability, and adherence to best practices. Highlight any areas that could be improved.
4. **Potential Issues**: Identify potential security issues only when there is evidence in the code. Do not invent vulnerabilities.
5. **Suggestions for Improvement**: 
- Recommend improved code only when an improvement is actually needed. If the current code is already appropriate, state that clearly. Offer constructive feedback on how the code could be improved, including refactoring suggestions, alternative approaches, or additional features that could enhance its functionality.
Please provide your review in a clear and structured format, using bullet points or numbered lists where appropriate.

Analyze the following code snippet:
```{code}```

Provide:
    - Code summary
    - Bugs and logical issues
    - Current approach
    - Time complexity
    - Space complexity
    - Explanation
    - Improvements
    - Brute Force or Optimized approach
    - Recommend Code
    - Time complexity of fixed code
    - Space complexity of fixed code
    
    """
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error while analyzing code: {e}"
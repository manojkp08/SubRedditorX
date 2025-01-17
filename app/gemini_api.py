import google.generativeai as genai

from config import GEMINI_API_KEY

# Configure the API key
genai.configure(api_key=GEMINI_API_KEY)

def generate_content(prompt):
    try:
    
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        
        response = model.generate_content(prompt)
        
        if hasattr(response, 'text') and response.text:
            return response.text
        else:
            
            return f"Unexpected response format: {response}"
    except Exception as e:
       
        return f"Error generating content: {str(e)}"

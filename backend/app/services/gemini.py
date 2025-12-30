import google.generativeai as genai
from ..core.config import settings

class GeminiService:
    def __init__(self):
        if settings.GEMINI_API_KEY:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            self.model = genai.GenerativeModel('gemini-pro')
        else:
            self.model = None
            print("Warning: GEMINI_API_KEY not set. AI features will not work.")

    async def generate_resume_content(self, job_description: str, current_resume: str) -> str:
        if not self.model:
            return "Error: AI service not configured."
        
        prompt = f"""
        Act as an expert resume writer. 
        Analyze the following resume and job description.
        Rewrite the resume content to better match the job description, emphasizing relevant skills and achievements.
        Use professional, action-oriented language.
        
        Job Description:
        {job_description}
        
        Current Resume:
        {current_resume}
        
        Output the result as a structured JSON with keys: summary, experience (list), skills (list).
        """
        
        try:
            response = await self.model.generate_content_async(prompt)
            return response.text
        except Exception as e:
            return f"Error generating content: {str(e)}"

    async def polish_bullet_point(self, bullet: str) -> str:
        if not self.model:
            return "Error: AI not configured"
            
        prompt = f"Rewrite this resume bullet point to be more impactful and achievement-oriented, using action verbs: '{bullet}'. Output only the rewritten bullet point."
        
        try:
            response = await self.model.generate_content_async(prompt)
            return response.text.strip()
        except Exception as e:
            return bullet

gemini_service = GeminiService()

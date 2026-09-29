import os
import google.generativeai as genai

class SocialMediaAIAgent:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        # Using Gemini 2.5 Flash for fast multimodal and text processing
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    def generate_algorithm_blueprint(self, brand_name, niche, video_concept):
        prompt = f"""
        You are an elite Algorithm Growth Hacker and Recommendation Engine Engineer for Instagram, Facebook, and YouTube Shorts.
        Brand: {brand_name} ({niche})
        Video Concept: {video_concept}
        
        Provide an actionable, strict Algorithm-Hacking Blueprint covering:
        1. THE 3-SECOND HOOK (Pattern Interrupt to keep 3-sec drop rate below 30%)
        2. RETENTION ARCHITECTURE & LOOPS (Exact pacing and loop-back trick to cross 100% watch time)
        3. ALGORITHM SIGNALS (Specific hooks to spike Shares & Comments)
        4. OPTIMIZED CAPTION & 15 TARGETED HASHTAGS
        """
        response = self.model.generate_content(prompt)
        return response.text

from groq import Groq

from app.core.config import settings


class GenerationService:

    client = Groq(
        api_key=settings.GROQ_API_KEY
    )

    @classmethod
    def generate_response(
        cls,
        query,
        context
    ):

        prompt = f"""
        You are an enterprise AI assistant.

        Answer ONLY using the provided context.

        If the answer is not present,
        say you do not know.

        Context:
        {context}

        Question:
        {query}
        """

        response = cls.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        return response.choices[0].message.content
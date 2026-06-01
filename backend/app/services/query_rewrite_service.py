from groq import Groq

from app.core.config import settings


class QueryRewriteService:

    client = Groq(
        api_key=settings.GROQ_API_KEY
    )

    @classmethod
    def rewrite(cls, query):

        prompt = f"""
        Rewrite this query to improve
        enterprise document retrieval.

        Query:
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
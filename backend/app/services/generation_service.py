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
        context,
        history=[]
    ):

        history_text = "\n".join(

            f"{msg['role']}: {msg['content']}"

            for msg in history

        )

        prompt = f"""
            You are an enterprise AI assistant.

            Answer ONLY using the provided context.

            Use previous conversation history if relevant.

            If answer is not present,
            say you do not know.

            Conversation History:

            {history_text}

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
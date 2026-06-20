from groq import Groq

from app.core.config import settings


client = Groq(
    api_key=settings.GROQ_API_KEY
)


def summarizer_agent(state):

    query = state["query"]

    prompt = f"""
    Summarize the following request clearly:

    {query}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return {
        "response":
        response.choices[0].message.content,
        "sources": []
    }

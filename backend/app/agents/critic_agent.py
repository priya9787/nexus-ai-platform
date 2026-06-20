from groq import Groq

from app.core.config import settings


client = Groq(
    api_key=settings.GROQ_API_KEY
)


def critic_agent(state):

    response = state["response"]

    prompt = f"""
    Evaluate whether this response
    appears factually grounded.

    Response:
    {response}
    """

    critique = client.chat.completions.create(
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
        "final_response":response,
        "critic_feedback":critique.choices[0].message.content,
        "sources": state.get("sources", [])
    }

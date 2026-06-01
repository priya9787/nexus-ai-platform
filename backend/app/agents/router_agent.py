from groq import Groq

from app.core.config import settings


client = Groq(
    api_key=settings.GROQ_API_KEY
)

def router_agent(state):
    print("Groq Key",settings.GROQ_API_KEY)

    query = state["query"]

    prompt = f"""
    Return ONLY one word.

    Allowed outputs:

    retrieval
    summarization

    Do not explain.
    Do not add extra text.

    Query:
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

    decision = (
        response.choices[0]
        .message.content
        .strip()
        .lower()
    )

    return {
        "agent_decision": decision
    }
from groq import Groq

from app.core.config import settings

import time

client = Groq(
    api_key=settings.GROQ_API_KEY
)

def router_agent(state):
    print("Groq Key",settings.GROQ_API_KEY)
    
    start = time.time()

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
        model="llama-3.1-8b-instant",
        messages=[
            {
            "role": "system",

            "content": """

            You are a query router. 

            Return ONLY one word.
            retrieval:
            - factual questions
            - explanations
            - document questions
            - knowledge lookup
            - "what is"
            - "explain"


            summarization:
            - summarize text
            - shorten content
            - rewrite content

            Output ONLY:

                retrieval

                OR

                summarization

                No explanation.
                """
        },

        {
            "role": "user",

            "content": state["query"]
        }

       ],temperature=0
    )
    
    print(
        "ROUTER TIME:",
        time.time() - start
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
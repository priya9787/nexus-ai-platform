from fastapi import FastAPI

app = FastAPI(
    title="NexusAI Platform",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "message": "NexusAI Backend Running"
    }
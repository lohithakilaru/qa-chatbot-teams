from fastapi import FastAPI, Request
from teams_adapter import adapter, handle_teams_message
from botbuilder.schema import Activity

app = FastAPI()

@app.post("/api/messages")
async def messages(request: Request):
    body = await request.json()
    activity = Activity().deserialize(body)
    
    async def send_activity(text):
        return {"type": "message", "text": text}
    
    await handle_teams_message(activity, send_activity)
    return {"status": "OK"}
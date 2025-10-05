import uvicorn
from biomni.agent import A1
from fastapi import FastAPI, WebSocket

app = FastAPI()
agent = A1(path='../data', llm='claude-sonnet-4-20250514')

@app.get("/health")
async def get_health():
    return {
        "status": "ok"
    }
    
@app.websocket("/agent")
async def agent_endpoint(ws: WebSocket):
    await ws.accept()
    await ws.send_text("Hello bro")
    
    while True:
        message = await ws.receive_text()
        response = agent.go(message)
        await ws.send_text(response[1])
        
if __name__ == "__main__":
    print("APP RUNNING AT PORT 8000")
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

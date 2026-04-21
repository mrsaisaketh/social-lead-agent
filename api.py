from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agent import Agent

app = FastAPI()
agent = Agent()

# ✅ CORS FIX (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend is running successfully 🚀"}

@app.post("/chat")
def chat(data: dict):
    user_input = data.get("message", "")
    response = agent.run(user_input)
    return {"response": response}
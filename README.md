Social-to-Lead Agent (Inflx Assignment)

This project is a conversational AI agent designed to convert user interactions into qualified business leads. It is built for a fictional SaaS product AutoStream, which provides automated video editing tools for content creators.


Features

*  Intent Detection (Greeting, Pricing, High Intent)
*  RAG-based Knowledge Retrieval (from JSON)
*  Lead Capture Workflow (Name, Email, Platform)
*  Controlled Tool Execution (No premature calls)
*  State Management across conversation
*  React Frontend Chat UI
*  FastAPI Backend Integration

Architecture
The system follows a modular design:

* Intent Layer → Classifies user input
* RAG Layer → Retrieves pricing & policy data
* Agent Logic → Controls conversation flow
* Tool Layer → Captures leads via mock function
* State Management → Maintains user data across turns

A LangGraph version is also implemented to demonstrate advanced orchestration and state handling.

Tech Stack
* Frontend: React (Vite), Axios
* Backend: FastAPI (Python)
* AI Logic: Custom Agent + LangGraph
* Storage: JSON (local knowledge base)
How to Run
Backend
```bash
pip install fastapi uvicorn
uvicorn api:app --reload
```

Open: http://localhost:8000

---

Frontend
```bash
cd frontend
npm install
npm run dev
```

Open: http://localhost:5173

---

Sample Flow

```
User: Hi  
Bot: Hi! How can I help you?

User: What is your pricing?  
Bot: $29/month...

User: I want to try Pro plan  
Bot: What's your name?

User: Sai  
Bot: Your email?

User: sai@gmail.com  
Bot: Platform?

User: YouTube  
Bot: Lead captured successfully 
```
WhatsApp Integration (Concept)
The system can be integrated with WhatsApp using **Twilio API + Webhooks**. Incoming messages are routed to a backend endpoint, processed by the AI agent, and responses are sent back via Twilio. Conversation state can be stored using Redis or a database for persistence.

Demo
Shows full conversation flow
Demonstrates intent detection, RAG, and lead capture

Status
Assignment Completed
Fully Functional
Ready for Deployment

---

 Author

Sai Saketh
GitHub: https://github.com/mrsaisaketh

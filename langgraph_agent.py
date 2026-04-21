from langgraph.graph import StateGraph, END
from typing import TypedDict
from intent import detect_intent
from rag import get_answer
from tools import mock_lead_capture

class AgentState(TypedDict):
    user_input: str
    intent: str
    name: str
    email: str
    platform: str
    response: str

def intent_node(state):
    state["intent"] = detect_intent(state["user_input"])
    return state

def response_node(state):

    intent = state["intent"]
    text = state["user_input"]

    if intent == "greeting":
        state["response"] = "Hi! How can I help you?"
    
    elif intent == "pricing":
        state["response"] = get_answer(text)

    elif intent == "high_intent":

        if not state.get("name"):
            state["name"] = text
            state["response"] = "What's your email?"

        elif not state.get("email"):
            state["email"] = text
            state["response"] = "Your platform?"

        elif not state.get("platform"):
            state["platform"] = text

            mock_lead_capture(
                state["name"],
                state["email"],
                state["platform"]
            )

            state["response"] = "Lead captured successfully "

    else:
        state["response"] = "Can you clarify?"

    return state

builder = StateGraph(AgentState)

builder.add_node("intent", intent_node)
builder.add_node("response", response_node)

builder.set_entry_point("intent")
builder.add_edge("intent", "response")
builder.add_edge("response", END)

graph = builder.compile()

if __name__ == "__main__":
    state = {
        "name": None,
        "email": None,
        "platform": None
    }

    while True:
        user = input("User: ")
        state["user_input"] = user
        state = graph.invoke(state)
        print("Bot:", state["response"])

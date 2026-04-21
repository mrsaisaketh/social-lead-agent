from intent import detect_intent
from rag import get_answer
from tools import mock_lead_capture

class Agent:
    def __init__(self):
        self.state = {
            "intent": None,
            "name": None,
            "email": None,
            "platform": None
        }

    def run(self, user_input):

        # 🔒 Lock high-intent flow
        if self.state["intent"] != "high_intent":
            intent = detect_intent(user_input)
            self.state["intent"] = intent

        # ✅ Greeting
        if self.state["intent"] == "greeting":
            return "Hi! How can I help you today?"

        # ✅ Pricing (RAG)
        elif self.state["intent"] == "pricing":
            return get_answer(user_input)

        # ✅ High Intent Flow (CORRECT)
        elif self.state["intent"] == "high_intent":

            # Ask name
            if not self.state["name"]:
                self.state["name"] = user_input
                return "Great! What's your email?"

            # Ask email
            elif not self.state["email"]:
                self.state["email"] = user_input
                return "Which platform do you create content on? (YouTube/Instagram)"

            # Ask platform + trigger tool
            elif not self.state["platform"]:
                self.state["platform"] = user_input

                mock_lead_capture(
                    self.state["name"],
                    self.state["email"],
                    self.state["platform"]
                )

                return "You're all set! We’ll reach out soon 🚀"

        return "Can you please clarify?"
import json

with open("data.json") as f:
    data = json.load(f)

def get_answer(query):
    query = query.lower()

    if "pro" in query:
        return data["pricing"]["pro"]
    else:
        return data["pricing"]["basic"]
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from config import GEMINI_API_KEY

app = Flask(__name__)

# ✅ Configure Gemini API key
genai.configure(api_key=GEMINI_API_KEY)

# Store chat history
chat_history = ""

def get_gemini_response(user_input):
    global chat_history
    chat_history += f"You: {user_input}\nChatbot: "

    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(chat_history)

        answer = response.text.strip()
        chat_history += answer + "\n"
        return answer

    except Exception as e:
        error_msg = str(e)

        # 🌸 Sweet quota message
        if "RESOURCE_EXHAUSTED" in error_msg or "429" in error_msg:
            return (
                "🌸 I'm feeling a little tired right now 😴\n\n"
                "I've reached my daily chat limit.\n"
                "Please come back tomorrow — I’ll be happy to chat again! 💬✨"
            )
        else:
            return (
                "💔 Oops! Something went wrong on my side.\n"
                "Please try again in a moment."
            )

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message", "")
    answer = get_gemini_response(user_input)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
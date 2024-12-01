from django.shortcuts import render
from django.http import JsonResponse
from .utils import query_gemini_api

# Initialize conversation history
conversation_history = []

def home(request):
    global conversation_history

    if request.method == "POST":
        import json

        # Parse the incoming JSON request
        body = json.loads(request.body)
        user_message = body.get("prompt", "").strip()

        if user_message:
            # Append user's message to the history
            conversation_history.append({"role": "user", "message": user_message})

            # Query the Gemini API with the conversation history
            prompt = "\n".join(
                f"{msg['role'].capitalize()}: {msg['message']}" for msg in conversation_history
            )
            bot_message = query_gemini_api(prompt)

            # Append bot's response to the history
            conversation_history.append({"role": "bot", "message": bot_message})

            return JsonResponse({"response": bot_message})

        return JsonResponse({"response": "Error: Please enter a valid prompt."})

    # Clear conversation history on initial page load
    conversation_history = []
    return render(request, "home.html")

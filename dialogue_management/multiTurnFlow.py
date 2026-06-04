# -----------------------------------------
# MULTI-TURN CONVERSATIONAL FLOW DEMONSTRATION
# -----------------------------------------
# This program demonstrates how a chatbot
# maintains CONTEXT across multiple turns
# and how TOKENS are consumed per interaction.

import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Add project root directory to Python path
# This allows importing utils from any subfolder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.token_utils import count_tokens

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -------------------------------
# DISPLAY CONCEPT INFORMATION
# -------------------------------
print("\n==============================")
print("TOPIC : MULTI-TURN CONVERSATION")
print("==============================")
print("Concept:")
print("The chatbot maintains conversation history")
print("by sending previous messages with each request.\n")

print("Type 'exit' to end the conversation.\n")

# -------------------------------
# INITIALIZE CONVERSATION HISTORY
# -------------------------------
conversation_history = []

# Optional: track total tokens for entire session
total_session_tokens = 0

# -------------------------------
# START CHAT LOOP
# -------------------------------
while True:
    # Take user input
    user_input = input("You: ")

    # Exit condition
    if user_input.lower() == "exit":
        print("\nConversation ended.")
        print(f"Total Tokens Used in Session: {total_session_tokens}")
        break

    # Count tokens used by user input
    user_tokens = count_tokens(user_input)

    # Add user message to conversation history
    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    # -------------------------------
    # SEND FULL HISTORY TO MODEL
    # -------------------------------
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation_history
    )

    # Extract assistant reply
    assistant_reply = response.choices[0].message.content

    # Count tokens used by assistant response
    assistant_tokens = count_tokens(assistant_reply)

    # Add assistant response to history
    conversation_history.append({
        "role": "assistant",
        "content": assistant_reply
    })

    # Update session token count
    turn_tokens = user_tokens + assistant_tokens
    total_session_tokens += turn_tokens

    # -------------------------------
    # DISPLAY CHAT RESPONSE
    # -------------------------------
    print("\nBot:")
    print(assistant_reply)

    # -------------------------------
    # DISPLAY TOKEN STATISTICS
    # -------------------------------
    print("\n--- Token Usage (This Turn) ---")
    print(f"User Input Tokens       : {user_tokens}")
    print(f"Assistant Response Tokens: {assistant_tokens}")
    print(f"Total Tokens This Turn  : {turn_tokens}")
    print("-------------------------------\n")

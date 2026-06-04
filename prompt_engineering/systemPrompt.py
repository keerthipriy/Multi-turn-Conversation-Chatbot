# -----------------------------------------
# SYSTEM PROMPT DEMONSTRATION
# -----------------------------------------
# This program demonstrates the POWER of SYSTEM PROMPTS.
# System prompts define global rules and behavior
# and have the HIGHEST priority in a conversation.

import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -------------------------------
# DISPLAY CONCEPT INFORMATION
# -------------------------------
print("\n==============================")
print("PROMPT TYPE : SYSTEM PROMPT")
print("==============================")
print("Concept:")
print("System prompts define rules and behavior that the AI must follow.\n")

# -------------------------------
# DEFINE SYSTEM INSTRUCTION
# -------------------------------
system_instruction = (
    "You are a strict examiner. "
    "Answer briefly in 2–3 lines only."
)

user_question = "Explain prompt engineering."

print("System Instruction:")
print(system_instruction)

print("\nUser Question:")
print(user_question)

# -------------------------------
# PREPARE MESSAGES
# -------------------------------
messages = [
    {
        "role": "system",
        "content": system_instruction
    },
    {
        "role": "user",
        "content": user_question
    }
]

# -------------------------------
# SEND PROMPT TO MODEL
# -------------------------------
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

# Extract model response
answer = response.choices[0].message.content

# -------------------------------
# DISPLAY MODEL RESPONSE
# -------------------------------
print("\nModel Response (System-Controlled):")
print(answer)

print("\n--- Explanation ---")
print("Even if the user asks normally,")
print("the system instruction strictly controls the response style.")
print("System messages override user intent.")
print("------------------------------\n")


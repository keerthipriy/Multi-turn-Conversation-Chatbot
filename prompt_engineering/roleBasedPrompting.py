# -----------------------------------------
# ROLE-BASED PROMPTING DEMONSTRATION
# -----------------------------------------
# This program demonstrates ROLE-BASED prompting,
# where the AI is assigned a specific ROLE or PERSONA
# using a system message.

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
print("PROMPT TYPE : ROLE-BASED PROMPTING")
print("==============================")
print("Concept:")
print("The AI is given a role that controls its tone, depth, and style.\n")

# -------------------------------
# DEFINE ROLE AND QUESTION
# -------------------------------
system_role = "You are a senior AI instructor teaching undergraduate students."
user_question = "Explain prompt engineering with a simple example."

print("Assigned System Role:")
print(system_role)

print("\nUser Question:")
print(user_question)

# -------------------------------
# PREPARE MESSAGES
# -------------------------------
messages = [
    {
        "role": "system",
        "content": system_role
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
print("\nModel Response:")
print(answer)

print("\n--- Explanation ---")
print("The same model behaves differently based on the assigned role.")
print("Role-based prompting controls HOW the AI responds, not WHAT it knows.")
print("------------------------------\n")


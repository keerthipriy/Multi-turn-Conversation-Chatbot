# -----------------------------------------
# STOP SEQUENCES DEMONSTRATION
# -----------------------------------------
# This program demonstrates how STOP SEQUENCES
# force the model to STOP generating output
# when a specific token or text appears.
#
# This is useful for:
# - Structured conversations
# - Preventing unwanted continuation
# - Enforcing output format

import os
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
print("TOPIC : STOP SEQUENCES")
print("==============================")
print("Concept:")
print("Stop sequences tell the model when to stop generating text.\n")

# -------------------------------
# DEFINE PROMPT
# -------------------------------
prompt = (
    "User: What is prompt engineering?\n"
    "Assistant:"
)

print("Prompt Sent to Model:")
print(prompt)

# -------------------------------
# CALL MODEL WITH STOP SEQUENCE
# -------------------------------
stop_sequence = "User:"

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    stop=[stop_sequence]
)

# -------------------------------
# DISPLAY RESPONSE
# -------------------------------
print(f"\nStop Sequence Used: '{stop_sequence}'")
print("Model Response (Stopped Automatically):")
print(response.choices[0].message.content)

print("\n--- Explanation ---")
print("The model stopped generating output when the stop sequence was encountered.")
print("This helps enforce structured responses.")
print("------------------------------\n")


# -----------------------------------------
# MAX TOKENS PARAMETER DEMONSTRATION
# -----------------------------------------
# This program demonstrates how the MAX TOKENS
# parameter limits the length of the AI response.
#
# This is important for:
# - Cost control
# - Response size control
# - Preventing overly long answers

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
print("TOPIC : MAX TOKENS CONTROL")
print("==============================")
print("Concept:")
print("Max tokens limits how long the AI response can be.\n")

# -------------------------------
# DEFINE PROMPT
# -------------------------------
prompt = "Explain prompt engineering in detail with examples."

print("Prompt Sent to Model:")
print(prompt)

# -------------------------------
# CALL MODEL WITH LIMITED TOKENS
# -------------------------------
max_tokens_limit = 50

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=max_tokens_limit
)

# -------------------------------
# DISPLAY RESPONSE
# -------------------------------
print(f"\nMax Tokens Set: {max_tokens_limit}")
print("Model Response (Truncated):")
print(response.choices[0].message.content)

print("\n--- Explanation ---")
print("The response is cut off once the max token limit is reached.")
print("This helps control cost and response length.")
print("------------------------------\n")


# -----------------------------------------
# ZERO-SHOT PROMPTING DEMONSTRATION
# -----------------------------------------
# This program demonstrates ZERO-SHOT prompting,
# where the model is asked a question WITHOUT
# providing any examples.

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
print("PROMPT TYPE : ZERO-SHOT PROMPTING")
print("==============================")
print("Concept:")
print("The model is asked a question directly without examples.\n")

# -------------------------------
# USER QUESTION
# -------------------------------
user_question = "Explain zero-shot prompting in simple terms."

print("User Question:")
print(user_question)

# -------------------------------
# SEND PROMPT TO MODEL
# -------------------------------
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": user_question}
    ]
)

# Extract response
answer = response.choices[0].message.content

# -------------------------------
# DISPLAY MODEL RESPONSE
# -------------------------------
print("\nModel Response:")
print(answer)

print("\n--- Explanation ---")
print("Notice that no examples were provided.")
print("The model relied only on its pretrained knowledge.")
print("------------------------------\n")


# -----------------------------------------
# FEW-SHOT PROMPTING DEMONSTRATION
# -----------------------------------------
# This program demonstrates FEW-SHOT prompting,
# where the model is given EXAMPLES before
# asking the actual question.

import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -------------------------------
# DISPLAY CONCEPT INFORMATION
# -------------------------------
print("\n==============================")
print("PROMPT TYPE : FEW-SHOT PROMPTING")
print("==============================")
print("Concept:")
print("The model is guided using example question–answer pairs.\n")

# -------------------------------
# FEW-SHOT EXAMPLES
# -------------------------------
examples = """
Q: What is AI?
A: AI is intelligence demonstrated by machines.

Q: What is Machine Learning?
A: Machine Learning is a subset of AI that learns from data.
"""

# Actual question after examples
actual_question = "What is prompt engineering?"

# Combine examples and question into a single prompt
prompt = f"""
{examples}

Q: {actual_question}
A:
"""

print("Examples Provided to the Model:")
print(examples)

print("Actual Question:")
print(actual_question)

# -------------------------------
# SEND PROMPT TO MODEL
# -------------------------------
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

# Extract model response
answer = response.choices[0].message.content

# -------------------------------
# DISPLAY MODEL RESPONSE
# -------------------------------
print("\nModel Response:")
print(answer)

print("\n--- Explanation ---")
print("The examples guided the model’s structure and tone.")
print("Compare this output with zero-shot prompting.")
print("------------------------------\n")

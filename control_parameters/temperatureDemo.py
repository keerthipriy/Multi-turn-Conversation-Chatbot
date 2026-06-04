# -----------------------------------------
# TEMPERATURE PARAMETER DEMONSTRATION
# -----------------------------------------
# This program demonstrates how the TEMPERATURE
# parameter controls randomness and creativity
# in the model's responses.

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
print("TOPIC : TEMPERATURE CONTROL")
print("==============================")
print("Concept:")
print("Temperature controls randomness in AI responses.")
print("Lower = more factual, Higher = more creative.\n")

# -------------------------------
# DEFINE PROMPT
# -------------------------------
prompt = "Write a short explanation about Artificial Intelligence."

print("Prompt Sent to Model:")
print(prompt)

# -------------------------------
# LOW TEMPERATURE RESPONSE
# -------------------------------
low_temp = 0.2
response_low = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=low_temp
)

print("\nResponse with LOW Temperature (0.2):")
print(response_low.choices[0].message.content)

# -------------------------------
# HIGH TEMPERATURE RESPONSE
# -------------------------------
high_temp = 0.9
response_high = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=high_temp
)

print("\nResponse with HIGH Temperature (0.9):")
print(response_high.choices[0].message.content)

print("\n--- Explanation ---")
print("Lower temperature gives consistent and factual output.")
print("Higher temperature produces more creative variations.")
print("------------------------------\n")

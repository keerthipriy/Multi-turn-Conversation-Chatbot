# -----------------------------------------
# PROMPT STRUCTURE & TOKEN USAGE DEMONSTRATION
# -----------------------------------------
# This program demonstrates HOW a prompt is structured
# and HOW many tokens it consumes.
#
# Prompt structure typically contains:
# 1. Instruction
# 2. Context
# 3. Input
# 4. Expected Output format

import sys
import os

# Add project root to Python path so utils can be imported
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.token_utils import count_tokens

# -------------------------------
# DISPLAY CONCEPT INFORMATION
# -------------------------------
print("\n==============================")
print("TOPIC : PROMPT STRUCTURE & TOKENS")
print("==============================")
print("Concept:")
print("Well-structured prompts produce clearer and predictable outputs.\n")

# -------------------------------
# DEFINE STRUCTURED PROMPT
# -------------------------------
instruction = "Explain the concept clearly."
context = "You are teaching undergraduate students."
input_question = "What is prompt engineering?"
output_format = "Provide a simple explanation with one example."

# Combine all parts into a structured prompt
structured_prompt = f"""
Instruction:
{instruction}

Context:
{context}

Input:
{input_question}

Expected Output:
{output_format}
"""

# -------------------------------
# DISPLAY PROMPT STRUCTURE
# -------------------------------
print("Structured Prompt Sent to Model:")
print(structured_prompt)

# -------------------------------
# TOKEN COUNTING
# -------------------------------
tokens_used = count_tokens(structured_prompt)

print("\nToken Usage:")
print(f"Total Tokens Used by Prompt: {tokens_used}")

print("\n--- Explanation ---")
print("Each part of the prompt contributes to token usage.")
print("More context = more tokens, but usually better output quality.")
print("------------------------------\n")

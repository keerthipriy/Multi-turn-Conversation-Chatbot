# -----------------------------------------
# PROMPT DEBUGGING DEMONSTRATION
# -----------------------------------------
# This program demonstrates PROMPT DEBUGGING,
# which means inspecting the EXACT prompt
# before sending it to the AI model.
#
# Prompt debugging helps answer questions like:
# - Why did the model respond incorrectly?
# - Is the prompt unclear or ambiguous?
# - Is too much or too little context provided?

# -------------------------------
# DISPLAY CONCEPT INFORMATION
# -------------------------------
print("\n==============================")
print("TOPIC : PROMPT DEBUGGING")
print("==============================")
print("Concept:")
print("When AI output is incorrect,")
print("we debug the PROMPT, not the model.\n")

# -------------------------------
# DEFINE A SAMPLE PROMPT
# -------------------------------
prompt = """
You are an AI tutor.
Explain prompt engineering to beginners.
Use simple language and one example.
"""

# -------------------------------
# DISPLAY PROMPT FOR DEBUGGING
# -------------------------------
print("----- PROMPT DEBUG START -----")
print(prompt.strip())
print("------ PROMPT DEBUG END ------")

# -------------------------------
# EXPLANATION FOR STUDENTS
# -------------------------------
print("\n--- Explanation ---")
print("This is the exact prompt that would be sent to the model.")
print("By inspecting it, we can improve clarity, structure, and instructions.")
print("Prompt debugging is an iterative process.")
print("------------------------------\n")

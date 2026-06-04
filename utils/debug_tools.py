# This function is used to debug and inspect prompts
# It helps developers understand exactly what is being sent to the AI model
# This is useful during prompt engineering and iterative refinement
def debug(prompt):
    
    # Print a blank line followed by a header for clarity
    # This visually separates debug output from normal program output
    print("\n--- PROMPT DEBUG ---")
    
    # Print the full prompt text
    # This allows developers to review instructions, examples, and structure
    print(prompt)
    
    # Print a footer line to clearly mark the end of the debug output
    print("-------------------\n")

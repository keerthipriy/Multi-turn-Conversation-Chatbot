# -----------------------------------------
# INTERRUPTION HANDLING IN DIALOGUE
# -----------------------------------------
# This program demonstrates how a chatbot
# handles INTERRUPTIONS such as:
# - Empty input
# - Very short input
# - Unclear user messages

# -------------------------------
# FUNCTION: HANDLE INTERRUPTION
# -------------------------------
def handle_interruption(user_input):
    """
    Detects interruption scenarios and
    returns an appropriate system message.
    """

    # Check for empty or whitespace-only input
    if not user_input.strip():
        return "Please enter a valid question."

    # Check for very short or unclear input
    if len(user_input.strip()) < 3:
        return "Can you please explain your question in more detail?"

    # No interruption detected
    return None

# -------------------------------
# DEMONSTRATION
# -------------------------------
if __name__ == "__main__":

    print("\n==============================")
    print("TOPIC : INTERRUPTION HANDLING")
    print("==============================")
    print("Concept:")
    print("Chatbots must handle unclear or incomplete inputs gracefully.\n")

    test_inputs = [
        "",
        "hi",
        "Explain prompt engineering"
    ]

    for user_input in test_inputs:
        print(f"User Input: '{user_input}'")

        result = handle_interruption(user_input)

        if result:
            print(f"Interruption Detected: YES")
            print(f"System Response: {result}\n")
        else:
            print("Interruption Detected: NO")
            print("Input is valid.\n")

    print("--- Explanation ---")
    print("Real users often give incomplete inputs.")
    print("Handling interruptions improves user experience.")
    print("------------------------------\n")

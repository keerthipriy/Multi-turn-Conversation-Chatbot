# -----------------------------------------
# ERROR HANDLING IN CONVERSATIONAL AI
# -----------------------------------------
# This program demonstrates how a chatbot
# handles ERRORS gracefully instead of crashing.
#
# Errors may occur due to:
# - API issues
# - Network failures
# - Unexpected runtime problems

# -------------------------------
# FUNCTION: HANDLE ERROR
# -------------------------------
def handle_error(error):
    """
    Handles errors and returns a
    user-friendly message.
    """

    # Print the actual error for developers
    print("Internal Error (for debugging):")
    print(error)

    # Return a safe message for the user
    return "Sorry, something went wrong. Please try again."

# -------------------------------
# DEMONSTRATION
# -------------------------------
if __name__ == "__main__":

    print("\n==============================")
    print("TOPIC : ERROR HANDLING")
    print("==============================")
    print("Concept:")
    print("A chatbot should recover gracefully from errors.\n")

    # Simulate an error
    simulated_error = "API Timeout Error"

    print("Simulating an error...")
    user_message = handle_error(simulated_error)

    print("\nUser-Facing Message:")
    print(user_message)

    print("\n--- Explanation ---")
    print("Errors are logged for developers.")
    print("Users see only a friendly message.")
    print("------------------------------\n")

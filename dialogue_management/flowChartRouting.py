# -----------------------------------------
# CONVERSATIONAL FLOWCHART ROUTING
# -----------------------------------------
# This program demonstrates how chatbots
# follow FLOWCHARTS instead of free conversation.
#
# Based on user input, the chatbot decides:
# - HELP flow
# - EXIT flow
# - NORMAL chat flow

# -------------------------------
# FUNCTION: ROUTE USER INPUT
# -------------------------------
def route_conversation(user_input):
    """
    Determines the conversation flow
    based on user intent.
    """

    # Normalize input for comparison
    text = user_input.lower()

    if "help" in text:
        return "HELP_FLOW"

    if "exit" in text or "bye" in text:
        return "EXIT_FLOW"

    return "NORMAL_CHAT"

# -------------------------------
# DEMONSTRATION
# -------------------------------
if __name__ == "__main__":

    print("\n==============================")
    print("TOPIC : CONVERSATIONAL FLOWCHARTS")
    print("==============================")
    print("Concept:")
    print("Chatbots use decision-based flowcharts")
    print("to route conversations.\n")

    # Test inputs
    test_inputs = [
        "I need help",
        "bye",
        "Explain tokens"
    ]

    for user_input in test_inputs:
        flow = route_conversation(user_input)

        print(f"User Input: {user_input}")
        print(f"Detected Flow: {flow}\n")

    print("--- Explanation ---")
    print("Different keywords trigger different conversation paths.")
    print("This is how real chatbots are designed.")
    print("------------------------------\n")

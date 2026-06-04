# -----------------------------------------
# CONVERSATION HISTORY MANAGEMENT
# -----------------------------------------
# This module demonstrates how conversation
# history can be managed SEPARATELY from
# the chatbot logic.
#
# This is an example of GOOD SOFTWARE DESIGN:
# - Logic is reusable
# - Code is clean
# - Easier to maintain and debug

# -------------------------------
# INITIALIZE HISTORY STORAGE
# -------------------------------
conversation_history = []

# -------------------------------
# FUNCTION: ADD MESSAGE
# -------------------------------
def add_message(role, content):
    """
    Adds a message to the conversation history.

    role   : 'user' or 'assistant'
    content: message text
    """
    conversation_history.append({
        "role": role,
        "content": content
    })

# -------------------------------
# FUNCTION: GET HISTORY
# -------------------------------
def get_history():
    """
    Returns the full conversation history.
    """
    return conversation_history

# -------------------------------
# DEMONSTRATION (STANDALONE RUN)
# -------------------------------
if __name__ == "__main__":
    print("\n==============================")
    print("TOPIC : CONVERSATION HISTORY")
    print("==============================")
    print("Concept:")
    print("Conversation history is stored and reused")
    print("to maintain context in multi-turn dialogue.\n")

    # Simulate a conversation
    add_message("user", "What is prompt engineering?")
    add_message("assistant", "Prompt engineering is the practice of designing prompts.")

    print("Stored Conversation History:")
    for msg in get_history():
        print(f"{msg['role'].upper()}: {msg['content']}")

    print("\n--- Explanation ---")
    print("Separating history logic makes the chatbot modular.")
    print("The same history can be reused across different components.")
    print("------------------------------\n")

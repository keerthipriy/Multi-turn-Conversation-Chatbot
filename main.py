# -----------------------------------------
# MAIN MENU-DRIVEN RUNNER FOR UNIT–II
# -----------------------------------------
# This file allows users to select and execute
# different Prompt Engineering and Dialogue
# Management concepts from a single interface

# Import os module to execute other Python files
import os


def show_menu():
    """
    Displays the menu options to the user
    """
    print("\n==============================")
    print("UNIT–II: Prompt Engineering & Dialogue Management")
    print("==============================")
    print("1. Zero-Shot Prompting")
    print("2. Few-Shot Prompting")
    print("3. Role-Based Prompting")
    print("4. System Prompt Demo")
    print("5. Prompt Structure & Tokens")
    print("6. Multi-Turn Conversation")
    print("7. Conversational Flowchart Routing")
    print("8. Interruption Handling")
    print("9. Error Handling")
    print("10. Temperature Control Demo")
    print("11. Max Tokens Demo")
    print("12. Stop Sequences Demo")
    print("13. Prompt Debugging")
    print("0. Exit")

    print("===============================")


while True:
    show_menu()

    # Take user choice
    choice = input("Enter your choice: ")

    # Execute the selected option
    if choice == "1":
        os.system("python prompt_engineering/zeroShot.py")

    elif choice == "2":
        os.system("python prompt_engineering/fewShot.py")

    elif choice == "3":
        os.system("python prompt_engineering/roleBasedPrompting.py")

    elif choice == "4":
        os.system("python prompt_engineering/systemPrompt.py")

    elif choice == "5":
        os.system("python prompt_engineering/promptStructure.py")

    elif choice == "6":
        os.system("python dialogue_management/multiTurnFlow.py")

    elif choice == "7":
        os.system("python dialogue_management/flowChartRouting.py")

    elif choice == "8":
        os.system("python dialogue_management/interruptionHandling.py")

    elif choice == "9":
        os.system("python dialogue_management/errorHandling.py")


    elif choice == "10":
        os.system("python control_parameters/temperatureDemo.py")

    elif choice == "11":
        os.system("python control_parameters/maxTokensDemo.py")

    elif choice == "12":
        os.system("python control_parameters/stopSequencesDemo.py")

    elif choice == "13":
        os.system("python debugging/promptDebugging.py")


    elif choice == "0":
        print("Exiting UNIT–II Program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

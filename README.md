# Smart Prompt-Driven Multi-Turn Conversational Chatbot

## UNIT–II: Prompt Engineering and Dialogue Management

---

## 📌 Project Overview
This project is developed as part of **UNIT–II: Prompt Engineering and Dialogue Management** in the course **Designing Conversational AI**.

The objective of this project is to help students **understand and practically apply prompt engineering and dialogue management concepts** using a topic-wise, modular Python implementation, similar to the structure followed in UNIT–I.

The project uses a **menu-driven approach** to demonstrate each concept independently.

---

## 🎯 Project Objectives
- Understand how prompts influence AI behavior
- Implement zero-shot, few-shot, and role-based prompting
- Design structured prompts
- Manage multi-turn conversations
- Control AI behavior using temperature, max tokens, and stop sequences
- Handle dialogue interruptions and errors
- Debug and refine prompts
- Gain hands-on experience with GenAI APIs

---

## 🧠 UNIT–II Concepts Implemented (Topic-wise)

### Prompt Engineering
- Zero-shot prompting
- Few-shot prompting
- Role-based prompting
- System prompts
- Prompt structure and token usage

### Dialogue Management
- Multi-turn conversational flow
- Conversation history handling
- Conversational flowcharts and routing
- Interruption handling
- Error handling

### Model Behavior Control
- Temperature parameter
- Max tokens
- Stop sequences

### Debugging
- Prompt debugging techniques

---

## 🗂️ Final Project Structure (Submission Ready)

```
Smart_Prompt_Driven_Multi_Turn_Conversational_Chatbot/
│
├── main.py                  # Menu-driven runner (ENTRY POINT)
├── config.py                # Model configuration
├── requirements.txt         # Project dependencies
├── README.md                # Project documentation
│
├── prompt_engineering/      # Prompt Engineering concepts
│   ├── zeroShot.py
│   ├── fewShot.py
│   ├── roleBasedPrompting.py
│   ├── systemPrompt.py
│   └── promptStructure.py
│
├── dialogue_management/     # Dialogue Management concepts
│   ├── multiTurnFlow.py
│   ├── conversationHistory.py
│   ├── flowChartRouting.py
│   ├── interruptionHandling.py
│   └── errorHandling.py
│
├── control_parameters/      # Model behavior control
│   ├── temperatureDemo.py
│   ├── maxTokensDemo.py
│   └── stopSequencesDemo.py
│
├── debugging/               # Debugging utilities
│   └── promptDebugging.py
│
└── utils/                   # Utility functions
    └── token_utils.py
```

---

## ▶️ How to Run the Project

1. Create and activate a virtual environment
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your OpenAI API key to `.env`
4. Run the menu-driven program:
   ```bash
   python main.py
   ```

---

## 🧪 Learning Outcomes
After completing this project, students will be able to:
- Design effective prompts for LLMs
- Control AI responses programmatically
- Build multi-turn conversational systems
- Handle real-world dialogue interruptions
- Debug and optimize prompts

---



---

## 🏁 Conclusion
This project provides a complete, practical implementation of **Prompt Engineering and Dialogue Management**

# This variable specifies the OpenAI language model to be used
# "gpt-4o-mini" is a lightweight and cost-effective model
# suitable for educational and conversational applications
MODEL_NAME = "gpt-4o-mini"


# This variable controls the randomness of the model’s responses
# Lower values (e.g., 0.1–0.3) produce more factual and deterministic outputs
# Higher values (e.g., 0.7–1.0) generate more creative and diverse responses
TEMPERATURE = 0.3


# This variable defines the maximum number of tokens
# the model is allowed to generate in a single response
# It helps control response length, cost, and latency
MAX_TOKENS = 300


# This list defines stop sequences for text generation
# When the model encounters any of these sequences,
# it will immediately stop generating further output
# This is useful for structured conversations and role-based prompts
STOP_SEQUENCES = ["User:", "System:"]

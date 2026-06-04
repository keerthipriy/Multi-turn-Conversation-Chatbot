# Import the tiktoken library
# tiktoken is used to tokenize text in the same way as OpenAI language models
# This helps accurately calculate how many tokens a prompt uses
import tiktoken


# This function counts the number of tokens in a given text
# Token count is important because:
# - LLMs have maximum context window limits
# - API cost depends on the number of tokens used
def count_tokens(text, model="gpt-4o-mini"):
    
    # Get the token encoding scheme used by the specified model
    # Different models may use different tokenization rules
    encoding = tiktoken.encoding_for_model(model)
    
    # Encode the input text into tokens and return the total token count
    # len() gives the number of tokens generated from the text
    return len(encoding.encode(text))

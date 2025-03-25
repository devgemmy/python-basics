import re

def format_text(text):
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    return text.lower().replace(" ", "-")

text = "MISCELLANEOUS"
formatted_text = format_text(text)
print(formatted_text)

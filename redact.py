import random
import re

REDACT = "█"
PERCENT = 0.45
open_path = "Redactor\string_input.txt"
return_path = "Redactor\output.txt"

###

try:
    with open(open_path, 'r', encoding='utf-8') as file:
        text = file.read()
except FileNotFoundError:
    print(f"Error: The file at {open_path} was not found.")

split_text = re.split(r'(\n|[ \t]+)', text)
word_count = len(split_text)
amount_to_redact = int(PERCENT * word_count)
words_to_redact = random.sample(range(0, word_count), amount_to_redact)

for word in words_to_redact:
    special_word = split_text[word]
    count = len(special_word)
    split_text[word] = REDACT*count

redacted_text = " ".join(split_text)
try:
    with open(return_path, 'w', encoding='utf-8') as f:
        f.write(redacted_text)
except FileNotFoundError:
    print(f"Error: The file at {open_path} was not found.")

print(f"Redacted {PERCENT*100}% of message to: {return_path}")

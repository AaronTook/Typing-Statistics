"""
    Author: AaronTook (https://AaronTook.github.io)
    File Last Modified: 3/8/2024
    Project Name: Typing Statistics
    File Name: app.py
"""

import time
from random import randint

def is_an_int(string_to_check):
    try:
        string_int = int(string_to_check)
        return True
    except:
        return False

paragraphs = []
paragraph_sentences = []
with open("typing_text.txt", 'r') as full_text_doc:
    full_text = full_text_doc.readlines()
    for line in full_text:
        if line.strip() != "" and not is_an_int(line.strip()):
            paragraph_sentences.append(line.strip())
        else:
            paragraphs.append(" ".join(paragraph_sentences))
            paragraph_sentences = []
    paragraphs.append(" ".join(paragraph_sentences))

my_paragraph = ""
while my_paragraph == "":
    num_paragraphs = len(paragraphs)
    my_paragraph_num = randint(0,num_paragraphs-1)
    my_paragraph = paragraphs[my_paragraph_num]

print(my_paragraph)

input("\nRead the text above, then hit enter when you are ready to start the typing test...")
print("\nCopy the text:")
start_time = time.time()
user_typed = input("")
stop_time = time.time()
total_time = stop_time - start_time
print(f"Total time: {round(total_time, 2)} seconds.")
num_words = len(my_paragraph.split(" "))
word_avg_time = (total_time / num_words)
wpm = 60/word_avg_time
print(f"WPM: {wpm}")

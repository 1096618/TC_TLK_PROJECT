# -----------------------------------------------------------------------------
# Name:        Unique words
# Purpose:     Write a program that filter out a sentence/story with only unique words
#
# Author:      TC
# Created:     March 9, 2025
# -----------------------------------------------------------------------------

story = ("Trailer lived in a small trailer on the edge of town. Every morning, he’d sip coffee on the porch of his trailer, enjoying the quiet. His trailer wasn’t much, but it was enough. Sometimes he’d drive away, but he always returned to his trailer his peaceful, perfect home.")
words = story.split()

print("Random story:")
print(" ".join(words))
print()

unique_words = set(words)
empty_story = []

for word in words:
    if word in unique_words:
        empty_story.append(word)
        unique_words.remove(word)

print("Same story with only unique words:")
print(" ".join(empty_story))
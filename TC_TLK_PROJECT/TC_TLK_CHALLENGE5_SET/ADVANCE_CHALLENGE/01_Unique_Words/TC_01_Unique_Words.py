story = ("A hungry fox wanted to catch a rabbit, but the rabbit showed him a sweet berry patch instead. The fox enjoyed the berries and decided they'd be friends from then on.")
words = story.split()
print(words)

#print(" ".join(words))

set = set(words)
empty_story = ()
index = 0
for words in set:
    if words[index] in set:
        empty_story += words[index]
        index = index + 1

print(empty_story)
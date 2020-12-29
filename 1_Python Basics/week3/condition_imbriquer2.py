words = ["water", "chair", "pen", "basket", "hi", "car"]

num_words = 0
for word in words:
    if (len(word) > 3):
        num_words += 1
print(num_words)
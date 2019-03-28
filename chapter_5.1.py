WORDS = ["stupid", "book", "programming", "hateit", "boring"]

import random

while len(WORDS) > 0:
    idx = random.randint(0, len(WORDS) - 1)
    print(WORDS[idx])
    WORDS.pop(idx)
    
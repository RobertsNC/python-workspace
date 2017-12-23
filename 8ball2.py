import random

messages = ["It is certain",
            "It is decidedly so",
            "Yes definitely",
            "Reply hazy try again",
            "Ask again later",
            "Concentrate and ask again",
            "My peply is no",
            "Outlook doesn't look good",
            "Doubltful"]

print(messages[random.randint(0, len(messages) - 1)])

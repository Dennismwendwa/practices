import random

friends = [
        "dennis", "miily", "reginah", "tony", "fred"
        ]

random.shuffle(friends)

for i in range(len(friends)):
    giver = friends[i]
    receiver = friends[(i + 1) % len(friends)]
    print(f"{giver} gives a present to {receiver}")

print()
print(friends)
num_friends = len(friends)
for i in range(num_friends):
    giver = friends[i]
    for j in range(num_friends):
        if j != i:
            receiver = friends[j]
            print(f"{giver} gives a present to {receiver}")

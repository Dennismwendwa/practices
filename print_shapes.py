

height = 30
width  = 20

def rectangle(width, height):

    for _ in range(height):
        print("#" * width)

rectangle(width, height)


def square(size):

    for _ in range(size):
        for _ in range(size):
            print("*", end="")
        print()

square(20)




def triangle_90(height, width):

    count = 1
    for m in range(height):
        for _ in range(m + 1):
            print("*", end="")
        
        print()

    count = height
    for k in range(height - 1):
        for _ in range(count - 1):
            print("*", end="")
        
        count -= 1
        
        print()


triangle_90(7, 8)

def rombus(size):
    word = "PYTHON"
    c = 0
    for k in range(size):
        for y in range(size - k - 1):
            print(" ", end="")

        for x in range(k + 1):
            print("*", end="")

        
        print("*" * k, end="")

        print(word[c], end="")
        c += 1
        if c >= len(word):
            c = 0
        
        print()

    for j in range(size):
        #for t in range(size - j):
        print(" " * j, end="")

        #for h in range(size - j):
        print("*" * (size - j), end="")

        print("*" * (size - j))

rombus(20)













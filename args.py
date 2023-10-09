
def greet(**kwangs, args:w):

    for arg in args:
        print(arg)

#greet(3, 5, 7, 8, "Dennis", "millicent", "john")
#greet("dog", "nigel", "cat", "fruits")


def friend(a, b, c, *args, **kwangs):
    sum1 = 0
    for arg in args:
        sum1 += arg
    sum = 0
    #use items() to acces the keys and values
    for k, b in kwangs.items():
        sum += b
        print(k)
        print(b)
    sum = sum + sum1
    print(f"sum = {sum}")
    print(f"sum1 = {sum1}")

#friend(2, 2, 3, 3, 5, 7, k=3, b=5, c=8)

def friends(**kwangs):

    for i, k in kwangs.items():
        print(i, k)


friends(nam1 = "Millicent", name2="kelvin", name3="Tony")

def fri2(a, b, c):
    print(a, b, c)

my_dict = {'a': 1, 'b': 2, 'c': 3}

fri2(**my_dict)

def fact(n):

    if n == 1:
        return 1
    else:
      fat =  n * fact(n - 1)

    return fat

fzz = fact(990)

print(fzz)

# reverse the number

def reverseNumber(n):
    while (n > 0):
        a = list(str(n))
        break
    a.reverse()
    Reverse = "".join(a)
    return int(Reverse)


print(reverseNumber(1565))


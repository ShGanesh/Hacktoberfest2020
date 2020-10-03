"""
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
"""
a = int(raw_input("enter the number "))
n1 = int( "%d" % a )
n2 = int( "%d%d" % (a,a ) )
n3 = int( "%d%d%d" % (a, a, a ) )
n4 = int( "%d%d%d%d" % (a, a, a, a) )
print n1+n2+n3+n4


dozen=int(input())
m = dozen//12
n = dozen%12
if (n == 0):
    print(m,"dozen")
else:
    print(m,"dozen and",n)

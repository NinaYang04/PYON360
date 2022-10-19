# 2~100質數判斷程式

n = eval(input())
for n in range(2,101):
 
    fct = 0
 
    for i in range(1,n+1):
        if n%i == 0:
            fct += 1
 
    if fct == 2:
        print(n,"is prime")

ans = eval(input())

guess = 0
min = 1
max = 100
print(min,"< ? <",max)

while guess in range (101):
    guess = eval(input())

    if guess <= min or guess >= max:
        print("out of range")
        print(min,"< ? <",max)
        continue

    if guess == ans:
        print ("bingo answer is",ans)
        break
    
    elif ans < guess:
        max=guess
        print("wrong answer, guess smaller")
        print(min,"< ? <",max)
    else:
        min=guess
        print("wrong answer, guess larger")
        print(min,"< ? <",max)
     
    


    

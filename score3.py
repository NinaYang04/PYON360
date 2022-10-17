for school in 'content':

    school = int(input())
    if (school !=1 and school !=2):
        print("role error")
        break
    score = int(input())
    if (score < 0 or score > 100):
        print("score error")
        break

    for school in 'content':
          
        if (school == 1):
            if score >= 60:
                print("pass")
            else:
                print("fail")
        else:
            if score >= 70:
                print("pass")
            else:
                print("fail")
        break
    break

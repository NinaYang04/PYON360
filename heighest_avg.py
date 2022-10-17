score = [[76,73,85],[88,84,76],[92,82,92],[82,91,85],[72,74,73]]

totalSum = 0
totalAvg = 0
highestavg = 0
for i in range(5):
    print("student",str(i+1))
    
    for j in range(3):
        print(" "+str(j+1)+":",score[i][j])

    stSum =int("%d" % sum(score[i]))
    stAvg = "%.2f" % (sum(score[i])/len(score[i]))
    stAvg2 =round((sum(score[i])/len(score[i])),2)
    
    print(" sum:",stSum)
    print(" avg:",stAvg)

    totalSum = totalSum+stSum
    totalAvg = totalSum/15

    if stAvg2 > highestavg:
        student = i
        highestavg = stAvg2
    
    if i >=4:
        print("total: ",totalSum,", avg: %.2f" % totalAvg,sep="")
        print("highest avg: student ",student+1,": ",highestavg,sep="")



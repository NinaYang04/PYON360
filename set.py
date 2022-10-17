M = {"柯南","灰原","步美","美環","光彦"}
E = {"柯南","灰原","丸尾","野口","步美"}

i = M.difference(E)
lstI = list(i)
lstI.sort()
print (lstI)

u = E.difference(M)
lstU = list(u)
lstU.sort()
print (lstU)

ans = E.intersection(M)
lst = list(ans)
lst.sort()
print (lst)

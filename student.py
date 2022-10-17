class Student:
    def __init__(self, n, g):
        self.name = n
        self.gender = g
        self.grades = []
  
    def avg(self):
        self.avg = sum(self.grades) / len(self.grades)
        return self.avg

    def add(self, grade):
        self.grades.append(grade)

    def fcount(self):
        failGrades = 0
        for i in self.grades:
          if i < 60:
            failGrades = failGrades + 1
        self.failGrades = failGrades
        return failGrades
    
    def show(self):
        print("Name: ",self.name)
        print("Gender: ",self.gender)
        print("Grades:",self.grades)
        print("Avg:",self.avg())
        print("Fail Number:",self.fcount(),"\n")

def top(inputSeq):
  avgSeq = []
  for student in inputSeq:
    avgSeq.append(student.avg)
  maxAvgIndex = avgSeq.index(max(avgSeq))
  return inputSeq[maxAvgIndex].name

s1 = Student("Tom","M")
s2 = Student("Jane","F")
s3 = Student("John","M")
s4 = Student("Ann","F")
s5 = Student("Peter","M")
s1.add(80)
s1.add(90)
s1.add(55)
s1.add(77)
s1.add(40)
s2.add(58)
s2.add(87)
s3.add(100)
s3.add(80)
s4.add(40)
s4.add(55)
s5.add(60)
s5.add(60)

#top_student = top(s1,s2,s3,s4,s5)
class_student = [s1,s2,s3,s4,s5]

s1.show()
s2.show()
s3.show()
s4.show()
s5.show()

print("平均分數最高的是:" + top(class_student))



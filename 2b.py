x=input("Enter Marks in Exam: ")
if x>75:
	grade="Distinction"
elif x>=60 and x<75:
	grade="First Class"
elif x>=50 and x<60:
	grade="Pass"
else:
	grade="Fail"
print(grade)

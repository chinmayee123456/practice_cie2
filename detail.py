import sys
if len(sys.argv)!=6:
  script_name=sys.argv[0]
  sub_1=sys.argv[1]
  sub_2=sys.argv[2]
  sub_3=sys.argv[3]
  sub_4=sys.argv[4]
  sub_5=sys.argv[5]
  print("user provided input values:")
else:
  script_name=sys.argv[0]
  sub_1=90
  sub_2=80
  sub_3=65
  sub_4=76
  sub_5=50
  print("No input given-using default values:")
  avg=(sub_1+sub_2+sub_3+sub_4+sub_5)/100
  print("average marks is:",avg)
  print("grade is:",grade)
  if(avg>=80):
    grade="A"
  elif(avg>=70):
    grade="B"
  elif(avg>=60):
    grade="C"
  elif(avg>=40):
    grade="D"
  else:
    grade:fail

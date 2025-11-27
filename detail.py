import sys

if len(sys.argv) == 6:
    # User provided values
    script_name = sys.argv[0]
    sub_1 = float(sys.argv[1])
    sub_2 = float(sys.argv[2])
    sub_3 = float(sys.argv[3])
    sub_4 = float(sys.argv[4])
    sub_5 = float(sys.argv[5])

    print("User provided input values:")

else:
    # Default values
    script_name = sys.argv[0]
    sub_1 = 90
    sub_2 = 80
    sub_3 = 65
    sub_4 = 76
    sub_5 = 50
  print("No input given - using default values:")
avg = (sub_1 + sub_2 + sub_3 + sub_4 + sub_5) / 5
print("Average marks is:", avg)
if avg >= 80:
    grade = "A"
elif avg >= 70:
    grade = "B"
elif avg >= 60:
    grade = "C"
elif avg >= 40:
    grade = "D"
else:
    grade = "Fail"

print("Grade is:", grade)

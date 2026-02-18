try:
    score = int(input("Please Enter your score (0-100): "))
    if score >= 90:
          print("Grade: A = Excellent!")
    elif score >= 80:
          print("Grade: B = Very Good!")
    elif score >= 70:
          print("Grade: C - Good")
    elif score >= 60:
          print("Grade: D - Satisfactory")
    else:
          print("Grade: F - Needs Improvement")
except ValueError:
   print("Error. Please Enter a Number Again (0-100).")    
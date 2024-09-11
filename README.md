While True:
    for i in range(5):
        student_last = input("Please type your last name, or if you wish to not continue please input ZZZ in all caps.")
        if student_last == "ZZZ":
          print("we will not continue to seof you are on the Dean's list!")
        else:
            student_first = input ("Please insert your first name.")
            gpa = float(input("Please insert your GPA."))
            if gpa >= 3.25:
                print("Congratulations you are on Honor roll!!")
            if gpa >= 3.5:
                print("sorry you did not get on the Dean's list and you are not on honor roll.")

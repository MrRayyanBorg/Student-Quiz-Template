#geography questions
geo_question = 1

#Science Questions
sci_question = 1

#Mathematics Questions
math_question = 1


invalid_counter = 0
Check1 = 0

subject_choice = input("What subject would you like to be tested on?\n"
                       "\n"
                       "A. Geography\n"
                       "B. Science\n"
                       "C. Mathematics\n")
while Check1 == 0:

    if subject_choice.upper() == "A" :
        print("You will now be tested on Geography")
        while geo_question != 21:
            print("Geography Question ", geo_question)
            user_answer = input("A.\n"
                                "B.\n"
                                "C.\n"
                                "D.\n")
            if user_answer.upper() == "A":
                print("correct!")
            else:
                print("That answer was invalid/incorrect")
            geo_question += 1

        break
    elif subject_choice.upper() == "B" :
        print("You will now be tested on Science")
        while sci_question != 5:
            print("Science Question ", sci_question)
            user_answer = input("A.\n"
                                "B.\n"
                                "C.\n"
                                "D.\n")
            if user_answer.upper() == "A":
                print("correct!")
            else:
                print("That answer was invalid/incorrect")
            sci_question += 1
        break
    elif subject_choice.upper() == "C" :
        print("You will now be tested on Mathematics")
        while math_question != 10:
            print("Geography Question ", math_question)
            user_answer = input("A.\n"
                                "B.\n"
                                "C.\n"
                                "D.\n")
            if user_answer.upper() == "A":
                print("correct!")
            else:
                print("That answer was invalid/incorrect")
            math_question += 1
        break
    else:
        print("That input was not valid")
        subject_choice = input("What subject would you like to be tested on?\n"
                               "\n"
                               "A. Geography\n"
                               "B. Science\n"
                               "C. Mathematics\n")

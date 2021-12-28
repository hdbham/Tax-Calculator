playing = True

while playing:

    ############## LOGIC: ##############
    #
    # STEP 1 = TRUE
    #
    #   if income > LOWEREND and step1:
    #       totalTax += (income - LOWEREND) * x%
    #       step1 = False
    #       bracket = x

    #   elif income > LOWEREND:
    #       totalTax += (UPPEREND - LOWEREND) * x%
    #
    ####################################

    def calculateSingle():
        totalTax = 0

        step1 = True

        if income > 379150 and step1:
            totalTax += (income - 379150) * .35
            # print ("35%s1")
            step1 = False
            bracket = 35
            # matching elif not logically possible, deleted
        # .35

        if income > 174400 and step1:
            totalTax += (income - 174400) * .33
            # print ("33%s1")
            step1 = False
            bracket = 33
        elif income > 174400:
            totalTax += (379150 - 174400) * .33
            # print ("33%")
        # 379150 - 174400 .33

        if income > 83600 and step1:
            totalTax += (income - 83600) * .28
            # print ("28%s1")
            step1 = False
            bracket = 28
        elif income > 83600:
            totalTax += (174400 - 83600) * .28
            # print ("28%")
        # 174400 - 83600.28

        if income > 34500 and step1:
            totalTax += (income - 34500) * .25
            # print ("25%s1")
            step1 = False
            bracket = 25
        elif income > 34500:
            totalTax += (83600 - 34500) * .25
            # print ("25%")
        # 83600 - 34500 .25

        if income > 8500 and step1:
            totalTax += (income - 8500) * .15
            # print ("15%s1")
            step1 = False
            bracket = 15
        elif income > 8500:
            totalTax += (34500 - 8500) * .15
            # print ("15%")

        # 34500 - 8500 .15

        if income > 0 and step1:
            totalTax += (income - 0) * .10
            # print ("10%s1")
            step1 = False
            bracket = 10
        elif income > 0:
            totalTax += (8500 - 0) * .10
            # print ("10%")
        # 8500-0 .10

        yourTax = (totalTax / income) * 100

        print("\n")
        print("\n")
        print('your total taxes due are:')
        print(totalTax)
        print('your tax bracket is:')
        print(bracket)
        print('with a total tax of')
        print(yourTax)
        print("\n")


    # end calculateSingle
    # -------------------------

    def calculateMarried():
        taxableBracket = 0
        totalTax = 0

        step1 = True

        # upper end - lower end of bracket * bracket rate += taxTotal
        # EXCEPT for first where income is upperend

        if income > 379150 and step1:
            totalTax += (income - 379150) * .35
            # print ("35%s1")
            step1 = False
            bracket = 35
            # matching elif not logically possible, deleted

        if income > 212300 and step1:
            totalTax += (income - 212300) * .33
            # print ("33%s1")
            step1 = False
            bracket = 33
        elif income > 212300:
            totalTax += (379150 - 212300) * .33
            # print ("33%")
        # 379150-212300 .33

        if income > 139350 and step1:
            totalTax += (income - 139350) * .28
            # print ("28%s1")
            step1 = False
            bracket = 28
        elif income > 139350:
            totalTax += (212300 - 139350) * .28
        # print ("28%")
        # 212300-139350 .28

        if income > 69000 and step1:
            totalTax += (income - 69000) * .25
            # print ("25%s1")
            step1 = False
            bracket = 25
        elif income > 69000:
            totalTax += (139350 - 69000) * .25
        # print ("25%")
        # 139350-69000 .25

        if income > 17000 and step1:
            totalTax += (income - 17000) * .15
            # print ("15%s1")
            step1 = False
            bracket = 15
        elif income > 17000:
            totalTax += (69000 - 17000) * .15
        # print ("15%")
        # 69000-17000 .15

        if income > 0 and step1:
            totalTax += (income - 0) * .10
            # print ("10%s1")
            step1 = False
            bracket = 10
        elif income > 0:
            totalTax += (17000 - 0) * .10
        # print ("10%")
        # 17000-0 .10

        yourTax = (totalTax / income) * 100

        print("\n")
        print("\n")
        print('your total taxes due are:')
        print(totalTax)
        print('your tax bracket is:')
        print(bracket)
        print('with a total tax of')
        print(yourTax)
        print("\n")


    # end calculateMarried
    # -------------------------

    # -------------------------------
    def calculateHoh():
        totalTax = 0
        step1 = True

        if income > 379150 and step1:
            totalTax += (income - 379150) * .35
            # print ("35%s1")
            step1 = False
            bracket = 35
            # matching elif not logically possible, deleted
        # $379,150 .35

        if income > 193350 and step1:
            totalTax += (income - 193350) * .33
            # print ("33%s1")
            step1 = False
            bracket = 33
        elif income > 193350:
            totalTax += (379150 - 193350) * .33
            # print ("33%")
        # 379150 - 193350 .33

        if income > 119400 and step1:
            totalTax += (income - 119400) * .28
            # print ("28%s1")
            step1 = False
            bracket = 28
        elif income > 119400:
            totalTax += (193350 - 119400) * .28
            # print ("28%")
        # 193350 - 119400 .28

        if income > 46250 and step1:
            totalTax += (income - 46250) * .25
            # print ("25%s1")
            step1 = False
            bracket = 25
        elif income > 46250:
            totalTax += (119400 - 46250) * .25
            # print ("25%")
        # 119400 - 46250 .25

        if income > 12150 and step1:
            totalTax += (income - 12150) * .15
            # print ("15%s1")
            step1 = False
            bracket = 15
        elif income > 12150:
            totalTax += (46250 - 12150) * .15
            # print ("15%")
        # 46250 - 12150 .15

        if income > 0 and step1:
            totalTax += (income - 0) * .10
            # print ("10%s1")
            step1 = False
            bracket = 10
        elif income > 0:
            totalTax += (12150 - 0) * .10
            # print ("10%")
        # 12150-0 .10

        yourTax = (totalTax / income) * 100

        print("\n")
        print("\n")
        print('your total taxes due are:')
        print(totalTax)
        print('your tax bracket is:')
        print(bracket)
        print('with a total tax of')
        print(yourTax)
        print("\n")


    # end calculateHoh
    # -------------------------

    def main():  #
        print("I'm Hunter Burningham \n Welcome to my mini tax accounting calculator!! \n\n How are you filing?  \n ")


    main()

    # askuserforinput
    filingStatus = int(input("  \n 1. Single   \n 2. Married Filing Jointly   \n 3. Head of Household   \n\n "))
    income = 0
    income = int(input("Enter taxable income (after deductions and exemptions)  "))

    # user input defines method ran

    if (filingStatus == 1):
        calculateSingle()

    elif (filingStatus == 2):
        calculateMarried()

    elif (filingStatus == 3):
        calculateHoh()

    againPrompt = input('Press Enter to calculate more, or type "quit": ')
    while againPrompt == 'quit':
        playing = False

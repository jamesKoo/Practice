loan = input("Please enter your the cost of the loan : ")
interRate = input("Please enter your the interest rate : ")
year = input("Please enter your the number of years for the loan : ")

monthlyPay = (float(loan) * float(interRate) * (1 + float(interRate)) * float(year)) \
    / ((1 + float(interRate)) * float(year) - 1)

print("The monthly payments is {0:.2f}.".format(monthlyPay))
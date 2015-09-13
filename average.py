# average.py
#
# A program to compute the average of three numbers.

def main():
    print ("This program will compute the average of three numbers.")

    score1 = float(input("Enter first number: "))
    score2 = float(input("Enter second number: "))
    score3 = float(input("Enter third number: "))
    avg = (score1 + score2 + score3) / 3.0

    print("The average is " + str(avg))

main()


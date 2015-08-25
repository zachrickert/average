# average.py
#
# A program to compute the average of two numbers.
# Illustrates use of multiple imputs.

def main():
    print ("This program will compute the average of two numbers.")

    score1, score2 = input("Enter two numbers separated by a comma: ")
    avg = (score1 + score2) / 2.0

    print("The average is ") + str(avg)

main()


"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    while 100 >= score > 0:
        user_score(score)
        score = float(input("Enter score: "))
    else:
        print("Invalid Score")


def user_score(score):
    if 0 < score <= 50:
        print("Bad")
    elif 50 < score <= 90:
        print("Pass")
    elif 90 < score <= 100:
        print("Excellent")


main()

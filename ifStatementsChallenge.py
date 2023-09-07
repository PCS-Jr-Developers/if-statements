# ___________________________________________________
# Part 1
# ___________________________________________________

# Get input for the exam score
score = int(input("Enter your exam score: "))

# Determine the grade based on the score
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"

# ___________________________________________________
# Part 2
# ___________________________________________________
# Provide feedback based on the grade
if grade == "A":
    print("Excellent job! You got an A.")
    if score >= 95:
        print("You're a top performer!")
    else:
        print("Great work!")

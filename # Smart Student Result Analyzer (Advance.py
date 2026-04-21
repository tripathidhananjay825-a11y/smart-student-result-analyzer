# Smart Student Result Analyzer (Advanced Version)

print("===== Student Result Analyzer =====")

while True:
    name = input("\nEnter student name: ")

    try:
        maths = int(input("Enter Maths marks: "))
        science = int(input("Enter Science marks: "))
        english = int(input("Enter English marks: "))
    except ValueError:
        print("❌ Please enter valid numbers!")
        continue

    # Check for invalid marks
    if maths > 100 or science > 100 or english > 100:
        print("❌ Marks should not exceed 100!")
        continue

    # Total and percentage
    total = maths + science + english
    percentage = total / 3

    print("\n----- Result -----")
    print("Name:", name)
    print("Total Marks:", total)
    print("Percentage:", round(percentage, 2))

    # Grade system
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 35:
        grade = "D"
    else:
        grade = "F"

    # Subject-wise fail condition
    if maths < 35 or science < 35 or english < 35:
        result = "FAIL (Subject-wise)"
    elif percentage >= 35:
        result = "PASS"
    else:
        result = "FAIL"

    # Performance message
    if percentage >= 90:
        message = "Excellent performance!"
    elif percentage >= 60:
        message = "Good job, keep improving!"
    elif percentage >= 35:
        message = "You passed, but work harder."
    else:
        message = "You failed, don't give up!"

    print("Grade:", grade)
    print("Result:", result)
    print("Message:", message)

    # Continue or stop
    choice = input("\nDo you want to check another student? (yes/no): ")
    if choice.lower() != "yes":
        print("Exiting program...")
        break
def get_grade_description(grade):
    if grade == 'A':
        return 'Outstanding'
    elif grade == 'B':
        return 'Excellent'
    elif grade == 'C':
        return 'Very Good'
    elif grade == 'D':
        return 'Good'
    elif grade == 'E':
        return 'Satisfactory'
    else:
        return 'Unrecognized'

def main():
    student_name = input("Enter student name: ")
    student_class = input("Enter class: ")
    student_section = input("Enter Section: ")
    student_grade = input("Enter student's grade: ")

    grade_description = get_grade_description(student_grade)

    print(f"\nStudent Name: {student_name}")
    print(f"Class: {student_class}")
    print(f"Section: {student_section}")
    print(f"Grade: {student_grade} ({grade_description})")

if __name__ == "__main__":
    main()


#          Output

# Enter student name: Naveen Sony
# Enter class: MCA
# Enter Section: D2214
# Enter student's grade: A

# Student Name: Naveen Sony
# Class: MCA
# Section: D2214
# Grade: A (Outstanding)
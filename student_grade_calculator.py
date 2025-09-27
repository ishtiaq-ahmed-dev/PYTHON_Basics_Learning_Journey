def calculate_total_marks(math, english, biology):
    """
    Calculate total marks obtained in three subjects.
    """
    total = math + english + biology
    print("Obtained marks are:", total)
    return total


def calculate_percentage(total_obtained, total_possible):
    """
    Calculate percentage from obtained and total marks.
    """
    percentage = (total_obtained * 100) / total_possible
    print("You got", percentage, "% marks")
    return percentage


def determine_grade(percentage):
    """
    Determine grade based on percentage.
    """
    if percentage >= 90:
        print("You Got Grade of A++")
    elif 80 <= percentage < 90:
        print("You Got Grade of A+")
    elif 70 <= percentage < 80:
        print("You Got Grade of B")
    elif 60 <= percentage < 70:
        print("You Got Grade of C")
    else:
        print("You are FAIL")


def main():
    # You can change these values or use input() to make it interactive
    math_marks = 70
    english_marks = 60
    biology_marks = 90
    total_possible_marks = 300

    total = calculate_total_marks(math_marks, english_marks, biology_marks)
    percentage = calculate_percentage(total, total_possible_marks)
    determine_grade(percentage)


if __name__ == "__main__":
    main()

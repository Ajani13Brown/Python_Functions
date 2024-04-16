# Task 1: Code a function to calculate the average grade.

grades = [84,78,89,81,93,59,99]



def avg_grade(grades):
    average = sum(grades) / len(grades)
    print(average)

avg_grade(grades)

# Task 2: Implement a function to find the highest and lowest grade.

def min_max(grades):
    max_grade = max(grades)
    min_grade = min(grades)

    print(f'the highest grade is {max_grade} and the lowest grade is {min_grade}')

min_max(grades)
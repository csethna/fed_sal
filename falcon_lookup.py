
def input_grade_step():
    grade = raw_input("Employee GS Grade:")
    step = raw_input("GS Step:")
    grade_step = {}
    grade_step[grade] = step
    return grade_step

gs = input_grade_step()

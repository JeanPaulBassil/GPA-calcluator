import sys

courses = {}
total_points_earned = 0
total_credits_attempted = 0
nominator = 0


def point_grade():
    point_value = 0
    letter_grade = input('Letter grade: ').upper()
    if letter_grade.lower() == 'menu':
        menu()
    while letter_grade not in 'A-B+B-C+C-D+D-F':
        print('Not a valid value, Try again.')
        point_grade()
    else:
        if letter_grade.upper() == 'A':
            point_value = 4
        elif letter_grade.upper() == 'A-':
            point_value = 3.7
        elif letter_grade.upper() == 'B+':
            point_value = 3.3
        elif letter_grade.upper() == 'B':
            point_value = 3
        elif letter_grade.upper() == 'B-':
            point_value = 2.7
        elif letter_grade.upper() == 'C+':
            point_value = 2.3
        elif letter_grade.upper() == 'C':
            point_value = 2
        elif letter_grade.upper() == 'C-':
            point_value = 1.7
        elif letter_grade.upper() == 'D+':
            point_value = 1.3
        elif letter_grade.upper() == 'D':
            point_value = 1
        elif letter_grade.upper() == 'D-':
            point_value = 0.7
        elif letter_grade.upper() == 'F':
            point_value = 0

    return point_value


def credits():
    try:
        credits_num = (input('Course credit number: '))
        if credits_num.lower() == 'menu':
            menu()
        elif eval(credits_num) <= 0:
            print('The number of credits must be at least 1, try again.')
            credits()
    except (NameError, SyntaxError):
        print('Input must be a number, try again.')
        credits()
    else:
        return eval(credits_num)


def new_course():
    global total_points_earned
    global total_credits_attempted
    global courses
    global nominator
    course_name = input('Course name: ')
    if course_name.lower() == 'menu':
        menu()
    credit = credits()
    point_value = point_grade()
    total_points_earned += point_value
    total_credits_attempted += credit
    nominator += (point_value * credit)
    courses.update({course_name: [credit, point_value]})
    menu()


def on_or_off():
    on = input('Do you wish to continue using the program? (Yes/No)\n').capitalize()
    if on == 'Menu':
        menu()
    elif on == 'Yes':
        global courses
        global total_points_earned
        global total_credits_attempted
        global nominator
        courses = {}
        total_points_earned = 0
        total_credits_attempted = 0
        nominator = 0
        menu()
    elif on == 'No':
        sys.exit()
    else:
        print('Answer should be either yes or no, try again.')
        on_or_off()


def gpa_calc():
    try:
        print(f'Your GPA is: {round(nominator / total_credits_attempted, 2)}')
    except ZeroDivisionError:
        print('You should input at least one class.')
        menu()
    else:
        on_or_off()


def lists():
    for x in courses:
        print(
            f'Class name: {x} | Credits attempted: {courses[x][0]} | \
Point value: {courses[x][1]}')
    menu()


def remove():
    try:
        course_name = input("Course name: ")
        if course_name.lower() == 'menu':
            menu()
        courses.pop(f'{course_name}')
        menu()
    except KeyError:
        print('There is no such course name in the system, enter another name.')
        remove()


def menu():
    mode = input('''Enter: -"GPA" if you want to calculate your total GPA.
       -"Add" if you want to add a new course to the list.
       -"Remove" if you want to remove a certain class from the list.
       -"List" if you want the list of your courses.
       (Use the keyword "menu" at any time during the program to go back to the main manu)
Mode: ''').capitalize()
    if mode == 'Add':
        new_course()
    elif mode == 'Gpa':
        gpa_calc()
    elif mode == 'List':
        if len(list(courses.items())) > 0:
            lists()
        else:
            print('You should input at least one course first.')
            menu()
    elif mode == 'Remove':
        remove()
    else:
        print('This is not an option on our list.')
        menu()


menu()

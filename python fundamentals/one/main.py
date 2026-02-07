from calculate_area import Rectangle, Circle, Triangle

def show_menu():
    while True:
        print(
            '\nChoose Activity: \n1.Calculate Area\n2.Prime Number\n3.Simple Calculator\n4.Count Occurrence\n5.Remove Duplicates\n6.Student Records\n7.Exit\n')
        response = int(input('Response >> '))
        match response:
            case 1:
                calculate_area_menu()
            case 2:
                print(prime_number_menu())
            case 3:
                simple_calculator_menu()
            case 4:
                count_occurrence_menu()
            case 5:
                remove_duplicates_menu()
            case 6:
                student_records_menu()
            case 7:
                break
            case _:
                print("Invalid response")

def calculate_area_menu():
    while True:
        print('\nSolve Area: \n1.Circle\n2.Triangle\n3.Rectangle\n4.Exit\n')
        response = int(input('Response >> '))
        match response:
            case 1:
                radius = int(input('Radius:'))
                circle = Circle(radius)
                print(f'The calculated area is {circle.calculate_area()}')
            case 2:
                side1 = float(input('Side 1:'))
                side2 = float(input('Side 2:'))
                triangle = Triangle(side1, side2)
                print(f'The calculated area is {triangle.calculate_area()}')
            case 3:
                width = float(input('Width:'))
                height = float(input('Height:'))
                rectangle = Rectangle(width, height)
                print(f'The calculated area is {rectangle.calculate_area()}')
            case 4:
                break
            case _:
                print("Invalid response")

def prime_number_menu():
    number = int(input('Number >> '))
    if number <= 1:
        return 'Not a prime number'
    elif number == 2:
        return 'Prime number'
    else:
        occur = 0
        for x in range(1, number + 1):
            for y in range(1, number + 1):
                product = x * y
                if product == number:
                    occur += 1
        if occur == 2:
            return 'Prime number'
        return 'Not a Prime number'

def simple_calculator_menu():
    while True:
        print('\n1.Multiplication: \n2.Division\n3.Subtraction\n4.Addition\n5.Exit\n')
        num1 = int(input('Num1 >> '))
        num2 = int(input('Num2 >> '))
        operation = int(input('Operation (1-4) >> '))

        match operation:
            case 1:
                print(f'Product: {num1 * num2}')
            case 2:
                print(f'Quotient: {num1 / num2}')
            case 3:
                print(f'Subtraction: {num1 - num2}')
            case 4:
                print(f'Addition: {num1 + num2}')
            case 5:
                break


def count_occurrence_menu():
    lists = ['burger', 'fries', 'napkins', 'burger','cheese','cheese']
    [print(item, end=' ') for item in lists]
    print('\nCounts: ',end='\n')
    sets = set(lists)
    for item in sets:
        print(f"Count of {item} is {lists.count(item)}")

def remove_duplicates_menu():
    lists = ['burger', 'fries', 'napkins', 'burger', 'cheese', 'cheese']
    print('Before: ',end="\n")
    [print(item, end=' ') for item in lists]
    print('\nAfter: ',end='\n')
    sets = set(lists)
    [print(item, end=' ') for item in sets]

def student_records_menu():
    students = {}
    name = input('Student Name >> ')
    age = int(input('Student Age >> '))
    courses = []
    while True:
        course = input('Course (Exit 999)>> ')
        if course == '999':
            break
        else:
            courses.append(course)

    students.update(
        {'name':name,
         'age' : age,
         'courses': courses
        }
    )
    for x , y in students.items():
        print(f'{x} : {y}')

show_menu()







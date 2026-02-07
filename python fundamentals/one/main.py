from calculate_area import Rectangle, Circle, Triangle

def show_menu():
    while True:
        print(
            '\nChoose Activity: \n1.Calculate Area\n2.Prime Number\n3.Simple Calculator\n4.Count Occurrence\n5.Convert Temperature\n6.Remove Duplicates\n7.Student Records\n8.Exit\n')
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
                convert_temperature_menu()
            case 6:
                remove_duplicates_menu()
            case 7:
                student_records_menu()
            case 8:
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
    pass
def count_occurrence_menu():
    pass

def convert_temperature_menu():
    pass
def remove_duplicates_menu():
    pass
def student_records_menu():
    pass

show_menu()







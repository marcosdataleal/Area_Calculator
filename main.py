from calculator import Calculator
from room import Room

calc = Calculator()

room = Room(
    input('What is the width of the room? '),
    input('What is the depth of the room? ')
)

print('The area of the walls is: ', calc.calculate_wall_area(room))

print('The area of the ceiling is: ', calc.calculate_ceiling_area(room))

print('The required paint volume is: ', calc.calculate_required_paint())

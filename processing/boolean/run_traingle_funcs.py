import triangle_funcs
import csv

with open("triangles.csv") as file:
    csv_reader = csv.reader(file)
    headings = next(csv_reader)

print("Select an Option Menu: 1.Check if Equaliteral; 2.Check if Scalene; 3.Check if Isosceles; 4.Check if is in range; 5.Check if is valid; 6.Classify the triangle; 7.Check if the triangles is in range;")

sides = input()

if sides == 1:
    print(triangle_funcs.is_equilateral())
elif sides == 2:
    print(triangle_funcs.is_scalene())
elif sides == 3:
    print(triangle_funcs.is_isosceles())
elif sides == 4:
    print(triangle_funcs.is_in_range())
elif sides == 5:
    print(triangle_funcs.is_valid())
elif sides == 6:
    print(triangle_funcs.classify())
elif sides == 7:
    print(triangle_funcs.is_in_range())


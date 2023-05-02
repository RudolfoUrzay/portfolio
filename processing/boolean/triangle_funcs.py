def is_equilateral(sides):
     if sides[1] == sides[2] or sides[2] == sides[3] or sides[3] == sides[1]:
         return True
     else:
         return False

def is_scalene(sides):
    if sides[1] != sides[2] and sides[2] != sides[3]:
        return True
    else:
        return False

def is_isosceles(side):
    if is_equilateral(side) or not (is_equilateral(side) or is_scalene(side)):
        return True
    else:
        return False

def is_in_range(sides, lower_bound, upper_bound):
    for side in sides:
        if side < lower_bound or sides > upper_bound:
            return True
        else:
            return False

def is_valid(sides):
    if (sides[1] + sides[2] > sides[3]) and (sides[2]+sides[3]>sides[1]) and (sides[3]+sides[1]>sides[2]):
        return True
    else:
        return False

def classify(sides):
    if is_in_range(sides) and is_valid(sides):
        if is_equilateral(sides):
            return "Equilateral"
        elif is_scalene(sides):
            return "Scalene"
        else:
            return "Isosceles"
    else:
        return "Not Valid"


def triangles_with_sides_in_range(lower_bound, upper_bound):
    triangles = []

    for side_a in range(lower_bound, upper_bound):
        for side_b in range(lower_bound, upper_bound):
            for side_c in range(lower_bound, upper_bound):
                sides = [side_a, side_b, side_c]
                if is_in_range(sides) and is_valid(sides):
                    triangles.append(sides)

    return triangles
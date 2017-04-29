def triangle( a, b, c):
    if not 1 <= a <= 200:
        return "Out of range value"
    if not 1 <= b <= 200:
        return "Out of range value"
    if not 1 <= c <= 200:
        return "Out of range value"
    if not( a < b+c and b < a+c and c < a+b ):
        return "Not a triangle"
    if a == b == c:
        return "Equilateral"
    if a != b != c:
        return "Scalene"
    else:
        return "Isosceles"

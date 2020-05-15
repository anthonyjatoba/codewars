import math

def triangle_perimeter(triangle):
    side1 = math.hypot(triangle.a.x - triangle.b.x, triangle.a.y - triangle.b.y)
    side2 = math.hypot(triangle.a.x - triangle.c.x, triangle.a.y - triangle.c.y)
    side3 = math.hypot(triangle.b.x - triangle.c.x, triangle.b.y - triangle.c.y)
    return side1 + side2 + side3
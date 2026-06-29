# ==========================================
# AREA PROGRAMS
# ==========================================

# 1. Area of Rectangle
length = float(input("Length: "))
width = float(input("Width: "))
print("Area of Rectangle =", length * width)

# 2. Area of Square
side = float(input("Side: "))
print("Area of Square =", side * side)

# 3. Area of Circle
import math
radius = float(input("Radius: "))
print("Area of Circle =", math.pi * radius * radius)

# 4. Area of Triangle
base = float(input("Base: "))
height = float(input("Height: "))
print("Area of Triangle =", 0.5 * base * height)

# 5. Area of Parallelogram
base = float(input("Base: "))
height = float(input("Height: "))
print("Area of Parallelogram =", base * height)

# 6. Area of Trapezium
a = float(input("Parallel Side 1: "))
b = float(input("Parallel Side 2: "))
h = float(input("Height: "))
print("Area of Trapezium =", 0.5 * (a + b) * h)

# 7. Area of Rhombus
d1 = float(input("Diagonal 1: "))
d2 = float(input("Diagonal 2: "))
print("Area of Rhombus =", 0.5 * d1 * d2)

# ==========================================
# PERIMETER PROGRAMS
# ==========================================

# 8. Perimeter of Rectangle
length = float(input("Length: "))
width = float(input("Width: "))
print("Perimeter of Rectangle =", 2 * (length + width))

# 9. Perimeter of Square
side = float(input("Side: "))
print("Perimeter of Square =", 4 * side)

# 10. Circumference of Circle
radius = float(input("Radius: "))
print("Circumference =", 2 * math.pi * radius)

# 11. Perimeter of Triangle
a = float(input("Side 1: "))
b = float(input("Side 2: "))
c = float(input("Side 3: "))
print("Perimeter of Triangle =", a + b + c)



# ==========================================
# VOLUME PROGRAMS
# ==========================================

# 12. Volume of Cube
side = float(input("Side: "))
print("Volume of Cube =", side ** 3)

# 13. Surface Area of Cube
side = float(input("Side: "))
print("Surface Area of Cube =", 6 * side ** 2)

# 14. Volume of Cuboid
l = float(input("Length: "))
w = float(input("Width: "))
h = float(input("Height: "))
print("Volume of Cuboid =", l * w * h)

# 15. Volume of Cylinder
r = float(input("Radius: "))
h = float(input("Height: "))
print("Volume of Cylinder =", math.pi * r * r * h)

# 16. Volume of Sphere
r = float(input("Radius: "))
print("Volume of Sphere =", (4/3) * math.pi * r ** 3)

# 17. Volume of Cone
r = float(input("Radius: "))
h = float(input("Height: "))
print("Volume of Cone =", (1/3) * math.pi * r * r * h)

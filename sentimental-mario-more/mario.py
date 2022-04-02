from cs50 import get_int

# This is a comment
height = 0
while not (height >= 1 and height <= 8):
    height = get_int("Height: ")

for i in range(height):
    print(" " * (height - i - 1) + "#" * (i + 1) + "  " + "#" * (i + 1))
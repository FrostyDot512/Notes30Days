from random import *
from string import *

def generate_colors(color_type, num):
    colorss = []

    for i in range(num):
        if color_type == 'rgb':
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            colorss.append(f"rgb({r}, {g}, {b})")
        elif color_type == 'hexa':
            hex_digits = "0123456789abcdef"
            color = '#'

            for j in range(6):
                color += random.choice(hex_digits)

            colorss.append(color)
    return colorss

print(generate_colors('rgb', 3))
print(generate_colors('hexa', 1))


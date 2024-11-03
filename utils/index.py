import random

def generate_random_rgb_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

def generate_random_hex_color():
    return "#{:02X}{:02X}{:02X}".format(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )
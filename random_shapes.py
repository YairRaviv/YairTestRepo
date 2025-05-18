#!/usr/bin/env python3
import random

def print_square(size):
    """Print a square of asterisks with the given size."""
    for _ in range(size):
        print('*' * size)
    print()

def print_rectangle(width, height):
    """Print a rectangle of asterisks with the given width and height."""
    for _ in range(height):
        print('*' * width)
    print()

def print_triangle(height):
    """Print a right-angled triangle of asterisks with the given height."""
    for i in range(1, height + 1):
        print('*' * i)
    print()

def print_pyramid(height):
    """Print a pyramid of asterisks with the given height."""
    for i in range(1, height + 1):
        spaces = height - i
        stars = 2 * i - 1
        print(' ' * spaces + '*' * stars)
    print()

def print_diamond(height):
    """Print a diamond of asterisks with the given height."""
    # Top half (including middle row)
    for i in range(1, height + 1):
        spaces = height - i
        stars = 2 * i - 1
        print(' ' * spaces + '*' * stars)
    
    # Bottom half (excluding middle row)
    for i in range(height - 1, 0, -1):
        spaces = height - i
        stars = 2 * i - 1
        print(' ' * spaces + '*' * stars)
    print()

def print_random_shape():
    """Print a random shape with random dimensions."""
    shapes = [
        'square',
        'rectangle',
        'triangle',
        'pyramid',
        'diamond'
    ]
    
    shape = random.choice(shapes)
    print(f"Printing a random {shape}:")
    
    if shape == 'square':
        size = random.randint(3, 10)
        print_square(size)
    elif shape == 'rectangle':
        width = random.randint(5, 15)
        height = random.randint(3, 8)
        print_rectangle(width, height)
    elif shape == 'triangle':
        height = random.randint(3, 10)
        print_triangle(height)
    elif shape == 'pyramid':
        height = random.randint(3, 10)
        print_pyramid(height)
    elif shape == 'diamond':
        height = random.randint(3, 7)  # Keep it reasonable
        print_diamond(height)

if __name__ == "__main__":
    print("Random Shape Generator")
    print("=====================")
    
    # Generate 3 random shapes
    for i in range(3):
        print(f"\nShape {i+1}:")
        print_random_shape()

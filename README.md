# Random Shapes Generator

A simple Python script that generates and displays random shapes made of asterisks (*).

## Description

This repository contains a Python script that can generate and display various shapes using asterisks, including:
- Squares
- Rectangles
- Triangles
- Pyramids
- Diamonds

Each time you run the script, it will randomly select and display three different shapes with random dimensions.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/YairRaviv/YairTestRepo.git
   ```
2. Navigate to the repository directory:
   ```
   cd YairTestRepo
   ```

### Usage

Run the script using Python:
```
python random_shapes.py
```

Example output:
```
Random Shape Generator
=====================

Shape 1:
Printing a random triangle:
*
**
***
****
*****

Shape 2:
Printing a random pyramid:
    *
   ***
  *****
 *******
*********

Shape 3:
Printing a random rectangle:
***********
***********
***********
***********
```

## How It Works

The script contains functions for generating each type of shape:
- `print_square(size)`: Prints a square with the specified size
- `print_rectangle(width, height)`: Prints a rectangle with the specified width and height
- `print_triangle(height)`: Prints a right-angled triangle with the specified height
- `print_pyramid(height)`: Prints a pyramid with the specified height
- `print_diamond(height)`: Prints a diamond with the specified height

The `print_random_shape()` function randomly selects one of these shapes and generates it with random dimensions.

## Customization

You can modify the script to:
- Change the number of shapes generated (edit the loop range in the `__main__` section)
- Adjust the minimum and maximum dimensions for each shape (edit the `random.randint()` parameters)
- Add new shapes or modify existing ones

## License

This project is available for anyone to use and modify.

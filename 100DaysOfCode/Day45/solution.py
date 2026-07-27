"""
Day 45 - Flood Fill

Problem:
Given an image represented as a 2D grid,
change the color of the starting pixel and all
connected pixels with the same original color.

Example:

Input:
image = [
[1,1,1],
[1,1,0],
[1,0,1]
]

Start = (1,1)
New Color = 2

Output:
[
[2,2,2],
[2,2,0],
[2,0,1]
]
"""


def dfs(image, row, col, original_color, new_color):

    rows = len(image)
    cols = len(image[0])

    # Boundary check
    if row < 0 or row >= rows or col < 0 or col >= cols:
        return

    # Stop if color doesn't match
    if image[row][col] != original_color:
        return

    # Fill current cell
    image[row][col] = new_color

    # Visit all four directions
    dfs(image, row + 1, col, original_color, new_color)
    dfs(image, row - 1, col, original_color, new_color)
    dfs(image, row, col + 1, original_color, new_color)
    dfs(image, row, col - 1, original_color, new_color)


def flood_fill(image, sr, sc, new_color):

    original_color = image[sr][sc]

    if original_color == new_color:
        return image

    dfs(image, sr, sc, original_color, new_color)

    return image



# Test Case
# -------------------------

image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

print("Original Image:")
for row in image:
    print(row)

result = flood_fill(image, 1, 1, 2)

print("\nFlood Filled Image:")
for row in result:
    print(row)
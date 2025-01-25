# Write your solution here
def print_square(layers):
    size = 2 * layers - 1  # Size of the square
    square = []

    for i in range(size):
        row = []
        for j in range(size):
            # Calculate the minimum distance to any edge
            layer = min(i, j, size - i - 1, size - j - 1)
            row.append(chr(65 + layers - layer - 1))  # Convert layer to letter
        square.append("".join(row))

    for line in square:
        print(line)

# Example usage
layers = int(input("Layers: "))
print_square(layers)
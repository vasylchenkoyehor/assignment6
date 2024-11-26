import sys

# Validate and parse input
def parse_input(input_str):
    try:
        return [int(x.strip()) for x in input_str.split(",")]
    except ValueError:
        print("Error: Input must be a comma-separated list of integers.")
        sys.exit(1)

# Perform bitwise operations
def calculate_bitwise_operations(numbers):
    bitwise_and = numbers[0]
    bitwise_or = numbers[0]
    bitwise_xor = numbers[0]
    for num in numbers[1:]:
        bitwise_and &= num
        bitwise_or |= num
        bitwise_xor ^= num
    return bitwise_and, bitwise_or, bitwise_xor

# Filter numbers above threshold
def filter_above_threshold(numbers, threshold):
    return [num for num in numbers if num > threshold]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error: Please provide a list of integers and a threshold value.")
        sys.exit(1)

    # Read and validate inputs
    numbers_input = sys.argv[1]
    threshold_input = sys.argv[2]

    numbers = parse_input(numbers_input)

    try:
        threshold = int(threshold_input)
    except ValueError:
        print("Error: Threshold must be an integer.")
        sys.exit(1)

    # Perform calculations
    bitwise_and, bitwise_or, bitwise_xor = calculate_bitwise_operations(numbers)
    filtered_numbers = filter_above_threshold(numbers, threshold)

    # Output results as HTML
    print("Content-type: text/html\n")
    print("<html><body>")
    print("<h2>Bitwise Operations Results</h2>")
    print(f"<p>Bitwise AND: {bitwise_and}</p>")
    print(f"<p>Bitwise OR: {bitwise_or}</p>")
    print(f"<p>Bitwise XOR: {bitwise_xor}</p>")
    print(f"<p>Numbers greater than threshold ({threshold}): {filtered_numbers}</p>")
    print("</body></html>")

# Author: 2025 Mikhail Ibrahim
# Date: May 5th, 2025
# Description: A crash-proof Python program that asks the user for a starting and
# ending number, then prints all integers in that range. It uses one for loop and one
# if statement to format the output so that five integers appear per line, separated by spaces.
# All invalid inputs are handled to prevent the program from crashing.


def main():
    print("Welcome to the 5-Integers Per Line Formatter!")
    print(
        "This program will print numbers from your chosen start to end, five per line.\n"
    )

    # Input loop for validated start and end numbers
    while True:
        try:
            start = int(input("Enter the starting number: "))
            end = int(input("Enter the ending number: "))

            if start > end:
                print(
                    "The starting number must be less than or equal to the ending number.\n"
                )
                continue
            break  # Valid input, exit loop

        except ValueError:
            print("Invalid input. Please enter whole numbers only.\n")

    # Output section
    print(f"\nPrinting numbers from {start} to {end}, five per line:\n")

    # Loop through the range and print numbers
    for i in range(start, end + 1):
        print(i, end=" ")
        if (i - start + 1) % 5 == 0:
            print()  # Print new line after every 5 numbers

    print("\n\nProgram complete. All numbers displayed successfully.")


# Execute the main function when the script is run directly
if __name__ == "__main__":
    main()

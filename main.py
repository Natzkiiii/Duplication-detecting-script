import random
import string

"""
NOTE: Due to the chanves of finding a duplicate (0.00000000000000000691777709%) are so low,
i highly suggest you to change the length value, or change something else,
because you would need to leave it running for years on end.
In other words the numbers of unique strings (52^10 =  144,555,105,949,057,024)
is so large that it is pratically impossible to get a duplicate
"""

def generate_random_string(length=10):
    """Generates a random string of uppercase and lowercase letters."""
    letters = string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.choice(letters) for i in range(length))

def format_iteration_number(iteration):
    """Formats the iteration number with a period every three digits."""
    return f"{iteration:,}".replace(",", ".")

def main():
    seen_strings = {}
    iteration = 0
    
    while True:
        random_string = generate_random_string()
        if random_string in seen_strings:
            first_occurrence = seen_strings[random_string]
            print(f"Duplicate string found: '{random_string}'")
            print(f"First occurrence was at iteration: {format_iteration_number(first_occurrence)}")
            print(f"Duplicate found at iteration: {format_iteration_number(iteration)}")
            break
        else:
            seen_strings[random_string] = iteration
            print(f"Iteration {format_iteration_number(iteration)}: {random_string}")
            iteration += 1

if __name__ == "__main__":
    main()
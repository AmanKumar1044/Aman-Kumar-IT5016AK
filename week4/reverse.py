def reverse_string(s):
    reverse_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reverse_string

def main():
    original_str = input("enter a string:")
    reverse_string = (original_str)[::-1]
    print(f"original: {original_str}")
    print(f"reversed: {reverse_string}")

main()
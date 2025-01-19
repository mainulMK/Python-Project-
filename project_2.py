def reverse_string(s):
    return s[::-1]

def replace_text(s, old, new):
    return s.replace(old, new)

def toggle_case(s):
    return s.swapcase()

def capitalize_each_word(s):
    return s.title()

def main():
    while True:
        print("\nMenu:")
        print("1. Reverse the string")
        print("2. Replace specific text")
        print("3. Toggle the case")
        print("4. Capitalize each word")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == '5':
            print("Exiting the program. Goodbye!")
            break

        if choice in {'1', '2', '3', '4'}:
            user_string = input("\nEnter a string: ")

            if choice == '1':
                print("Reversed string:", reverse_string(user_string))

            elif choice == '2':
                old_text = input("Enter the text to replace: ")
                new_text = input("Enter the replacement text: ")
                print("Updated string:", replace_text(user_string, old_text, new_text))

            elif choice == '3':
                print("Toggled case string:", toggle_case(user_string))

            elif choice == '4':
                print("Capitalized string:", capitalize_each_word(user_string))

        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

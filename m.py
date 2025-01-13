def string_operations(input_string, old_text, new_text):
    # 1. Reverse the string
    reversed_string = input_string[::-1]

    # 2. Replace a specific text
    replaced_string = input_string.replace(old_text, new_text)

    # 3. Toggle the case
    toggled_case_string = input_string.swapcase()

    # 4. Capitalize each word
    capitalized_string = input_string.title()

    return reversed_string, replaced_string, toggled_case_string, capitalized_string

# Example usage
input_string = "Hello world! Welcome to the Python programming."
old_text = "world"
new_text = "universe"

reversed_string, replaced_string, toggled_case_string, capitalized_string = string_operations(input_string, old_text, new_text)

print("Reversed String:", reversed_string)
print("Replaced String:", replaced_string)
print("Toggled Case String:", toggled_case_string)
print("Capitalized String:", capitalized_string)
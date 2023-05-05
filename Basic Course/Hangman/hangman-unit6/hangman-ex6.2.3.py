def format_list(my_list):
    # Extract even elements from the list
    even_elements = my_list[::2]

    # Extract the last element and add the "and" before it
    last_element = "and " + my_list[-1]

    # Combine the even elements with commas and add the last element
    formatted_str = ", ".join(even_elements) + ", " + last_element

    return formatted_str
def main():
    print(format_list(["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]))
    z
if __name__ == '__main__':
    main()
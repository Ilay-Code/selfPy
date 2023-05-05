def print_list(products):
    print("Products in list: ", ', '.join(products))


def print_num_of_products(products):
    print("Number of products in list:", len(products))


def is_product_in_list(products):
    product = input("Enter product name: ")
    if product in products:
        print(product, "is on the list")
    else:
        print(product, "is not on the list")


def count_product_occurrences(products):
    product = input("Enter product name: ")
    count = products.count(product)
    print(product, "appears", count, "time(s)")


def remove_product(products):
    product = input("Enter product name: ")
    if product in products:
        products.remove(product)
        print(product, "has been removed from the list")
    else:
        print(product, "is not on the list")


def add_product(products):
    product = input("Enter product name: ")
    if len(product) < 3 or not product.isalpha():
        print(product, "is invalid and cannot be added to the list")
    else:
        products.append(product)
        print(product, "has been added to the list")


def print_invalid_products(products):
    invalid_products = [product for product in products if len(product) < 3 or not product.isalpha()]
    print("Invalid products:", ', '.join(invalid_products))


def remove_duplicates(products):
    products = list(set(products))
    print("Duplicates removed")
    return products


def main():
    user_input = ''
    products = []

    while user_input != '9':
        print("1. Print list of products")
        print("2. Print number of products in the list")
        print("3. Check if a product is on the list")
        print("4. Count how many times a product appears")
        print("5. Remove a product from the list")
        print("6. Add a product to the list")
        print("7. Print invalid products")
        print("8. Remove duplicates")
        print("9. Exit")

        user_input = input("Enter a number (1-9): ")

        switch_dict = {
            '1': lambda: print_list(products),
            '2': lambda: print_num_of_products(products),
            '3': lambda: is_product_in_list(products),
            '4': lambda: count_product_occurrences(products),
            '5': lambda: remove_product(products),
            '6': lambda: add_product(products),
            '7': lambda: print_invalid_products(products),
            '8': lambda: remove_duplicates(products),
        }

        action = switch_dict.get(user_input, lambda: None)
        if action:
            action()
        else:
            print("Invalid input. Please enter a number from 1 to 9.")


if __name__ == '__main__':
    main()

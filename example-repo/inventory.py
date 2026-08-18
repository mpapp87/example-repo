# Inventory management program for a Nike warehouse.


class Shoe:
    # Create a shoe object and store its inventory information.
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        # Return the cost of the shoe.
        return self.cost

    def get_quantity(self):
        # Return the quantity of the shoe.
        return self.quantity

    def __str__(self):
        # Return a readable string representation of the shoe.
        return (
            f"Country: {self.country}, Code: {self.code}, "
            f"Product: {self.product}, Cost: R{self.cost:.2f}, "
            f"Quantity: {self.quantity}"
        )


# Store all Shoe objects in this list.
shoes_list = []

INVENTORY_FILE = "inventory.txt"


def read_shoes_data():
    # Read shoe data from inventory.txt and create Shoe objects.
    shoes_list.clear()

    try:
        with open(INVENTORY_FILE, "r", encoding="utf-8") as inventory_file:
            next(inventory_file, None)

            for line_number, line in enumerate(inventory_file, start=2):
                line = line.strip()

                if not line:
                    continue

                shoe_data = line.split(",")

                if len(shoe_data) != 5:
                    print(
                        f"Skipping invalid data on line {line_number}: {line}"
                    )
                    continue

                country, code, product, cost, quantity = shoe_data

                try:
                    shoe = Shoe(
                        country.strip(),
                        code.strip(),
                        product.strip(),
                        float(cost.strip()),
                        int(quantity.strip()),
                    )
                    shoes_list.append(shoe)
                except ValueError:
                    print(
                        f"Skipping invalid numerical data on line "
                        f"{line_number}: {line}"
                    )

        print(f"Successfully loaded {len(shoes_list)} shoe records.")

    except FileNotFoundError:
        print(
            f"Error: '{INVENTORY_FILE}' was not found. "
            "Make sure it is in the same folder as inventory.py."
        )
    except OSError as error:
        print(f"Error reading the inventory file: {error}")


def save_inventory():
    # Write the current shoe list back to inventory.txt.
    try:
        with open(INVENTORY_FILE, "w", encoding="utf-8") as inventory_file:
            inventory_file.write("Country,Code,Product,Cost,Quantity\n")

            for shoe in shoes_list:
                inventory_file.write(
                    f"{shoe.country},{shoe.code},{shoe.product},"
                    f"{shoe.cost:.2f},{shoe.quantity}\n"
                )

        return True

    except OSError as error:
        print(f"Error updating the inventory file: {error}")
        return False


def get_non_empty_input(prompt):
    # Keep asking until the user enters a non-empty value.
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_positive_float(prompt):
    # Ask the user for a valid non-negative decimal number.
    while True:
        try:
            value = float(input(prompt))

            if value < 0:
                print("The value cannot be negative.")
            else:
                return value

        except ValueError:
            print("Please enter a valid number.")


def get_non_negative_integer(prompt):
    # Ask the user for a valid non-negative whole number.
    while True:
        try:
            value = int(input(prompt))

            if value < 0:
                print("The quantity cannot be negative.")
            else:
                return value

        except ValueError:
            print("Please enter a valid whole number.")


def capture_shoes():
    # Capture a new shoe record from the user.
    print("\nCapture a new shoe")

    country = get_non_empty_input("Country: ")
    code = get_non_empty_input("Code: ")
    product = get_non_empty_input("Product: ")
    cost = get_positive_float("Cost: ")
    quantity = get_non_negative_integer("Quantity: ")

    for shoe in shoes_list:
        if shoe.code.lower() == code.lower():
            print("A shoe with that code already exists.")
            return

    new_shoe = Shoe(country, code, product, cost, quantity)
    shoes_list.append(new_shoe)

    if save_inventory():
        print("The shoe was added successfully.")


def view_all():
    # Display all shoe records in a readable table.
    if not shoes_list:
        print("\nNo shoe records are available.")
        return

    print("\nAll shoe inventory")
    print("-" * 91)
    print(
        f"{'Country':<15}{'Code':<12}{'Product':<30}"
        f"{'Cost':>14}{'Quantity':>15}"
    )
    print("-" * 91)

    for shoe in shoes_list:
        print(
            f"{shoe.country:<15}{shoe.code:<12}{shoe.product:<30}"
            f"{shoe.cost:>14.2f}{shoe.quantity:>15}"
        )

    print("-" * 91)


def re_stock():
    # Find and optionally restock the shoe with the lowest quantity.
    if not shoes_list:
        print("\nNo shoe records are available.")
        return

    lowest_quantity_shoe = min(
        shoes_list,
        key=lambda shoe: shoe.get_quantity(),
    )

    print("\nShoe with the lowest quantity:")
    print(lowest_quantity_shoe)

    choice = input(
        "Would you like to add stock to this shoe? (yes/no): "
    ).strip().lower()

    if choice in ("yes", "y"):
        added_quantity = get_non_negative_integer(
            "Enter the quantity to add: "
        )

        if added_quantity == 0:
            print("No stock was added.")
            return

        lowest_quantity_shoe.quantity += added_quantity

        if save_inventory():
            print(
                f"Stock updated successfully. New quantity: "
                f"{lowest_quantity_shoe.quantity}"
            )
    elif choice in ("no", "n"):
        print("The stock quantity was not changed.")
    else:
        print("Invalid selection. No changes were made.")


def search_shoe():
    # Search for and return a shoe using its code.
    if not shoes_list:
        print("\nNo shoe records are available.")
        return None

    search_code = input("Enter the shoe code to search for: ").strip()

    for shoe in shoes_list:
        if shoe.code.lower() == search_code.lower():
            return shoe

    return None


def value_per_item():
    # Calculate and display the total value of every shoe item.
    if not shoes_list:
        print("\nNo shoe records are available.")
        return

    print("\nValue per inventory item")
    print("-" * 75)
    print(
        f"{'Code':<12}{'Product':<30}{'Quantity':>10}"
        f"{'Cost':>10}{'Value':>13}"
    )
    print("-" * 75)

    for shoe in shoes_list:
        item_value = shoe.get_cost() * shoe.get_quantity()

        print(
            f"{shoe.code:<12}{shoe.product:<30}"
            f"{shoe.quantity:>10}{shoe.cost:>10.2f}"
            f"{item_value:>13.2f}"
        )

    print("-" * 75)


def highest_qty():
    # Find the shoe with the highest quantity and mark it as for sale.
    if not shoes_list:
        print("\nNo shoe records are available.")
        return

    highest_quantity_shoe = max(
        shoes_list,
        key=lambda shoe: shoe.get_quantity(),
    )

    print("\nThe following product has the highest quantity and is for sale:")
    print(highest_quantity_shoe)


def display_menu():
    # Display the available inventory management options.
    print(
        """
Nike Warehouse Inventory Menu
1. Read shoe data from file
2. Capture a new shoe
3. View all shoes
4. Restock the lowest-quantity shoe
5. Search for a shoe by code
6. Display value per item
7. Display the highest-quantity shoe
8. Exit
"""
    )


def main():
    # Load the inventory when the program starts.
    read_shoes_data()

    while True:
        display_menu()
        menu_choice = input("Select an option (1-8): ").strip()

        if menu_choice == "1":
            read_shoes_data()

        elif menu_choice == "2":
            capture_shoes()

        elif menu_choice == "3":
            view_all()

        elif menu_choice == "4":
            re_stock()

        elif menu_choice == "5":
            found_shoe = search_shoe()

            if found_shoe is None:
                print("No shoe with that code was found.")
            else:
                print("\nShoe found:")
                print(found_shoe)

        elif menu_choice == "6":
            value_per_item()

        elif menu_choice == "7":
            highest_qty()

        elif menu_choice == "8":
            print("Thank you for using the inventory management program.")
            break

        else:
            print("Invalid selection. Please choose an option from 1 to 8.")


if __name__ == "__main__":
    main()

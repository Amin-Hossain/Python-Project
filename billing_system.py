import sys


def main():
    print("Welcome to my shop")
    print("\t---\n")

    name = input("Enter your name \t")
    add = input("Enter your address \t")
    print("\n\aNote: If you want to close then enter 'null'\n")

    items = []  #item name, item price

    while True:
        item_name = input("Enter item name\t\t").strip()
        if item_name.lower() == "null":
            break

        item_name = item_name.capitalize()

        try:
            price = int(input("Enter price\t\t"))
            items.append((item_name, price))
        except ValueError:
            print("Invalid price! Please enter a valid number.")

    # Printing Receipt
    print("\n\n\n\t Forid Store")
    print("\t-------------\n")
    print(f"Name: {name}".ljust(20) + f"Address: {add}".rjust(20))
    print("\n{:<15}{:>22}".format("Item name", "Price"))
    print("-" * 38)

    total_price = 0
    for item, price in items:
        print(f"{item:<15}{price:>22}")
        print("-" * 38)
        total_price += price

    print(f"Total items: {len(items)}".ljust(20) + f"Total: {total_price}".rjust(16))
    print("\n\t Thank You For Visiting")


if __name__ == "__main__":
    main()

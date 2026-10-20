
products = []

a = input("Do you want to add more items? (y/n): ")

while a.lower() == "y":
    name = input("Enter product name: ").strip().title()
    category = input("Enter product category: ").strip().lower()
    quantity = int(input("Enter product quantity: "))

    products.append({
        "name": name,
        "category": category,
        "quantity": quantity
    })

    print("Product added successfully!")

    a = input("\nDo you want to add more items? (y/n): ")

print("\nThank you!")

if products:
    total_items = len(products)
    total_quantity = sum(p["quantity"] for p in products)
    average_quantity = total_quantity / total_items

    most_stocked = max(products, key=lambda p: p["quantity"])
    least_stocked = min(products, key=lambda p: p["quantity"])

    categories = sorted(set(p["category"] for p in products))
    sorted_products = sorted(
        products,
        key=lambda p: p["quantity"],
        reverse=True
    )

    print("\n========== INVENTORY SUMMARY ==========")

    print("\nTotal Different Items:", total_items)
    names = ", ".join(p["name"] for p in products)
    print("Explanation: You entered", total_items,
          "different items:", names)

    print("\nTotal Quantity in Stock:", total_quantity)
    quantities = " + ".join(str(p["quantity"]) for p in products)
    print("Explanation: Sum of all quantities:",
          quantities, "=", total_quantity)

    print("\nAverage Quantity per Item:", average_quantity)
    print("Explanation: Average =", total_quantity,
          "total /", total_items, "items")

    print("\nMost Stocked Item:", most_stocked["name"],
          "(", most_stocked["quantity"], "units)")
    print("Explanation:", most_stocked["name"],
          "has the highest quantity among all items.")

    print("\nLeast Stocked Item:", least_stocked["name"],
          "(", least_stocked["quantity"], "units)")
    print("Explanation:", least_stocked["name"],
          "has the lowest quantity.")

    print("\n" + "-" * 50)

    print("\nUnique Categories in Inventory:", set(categories))
    print("Explanation: Categories are taken from user input")
    print("and converted to lowercase.")
    print("No duplicates are shown here.")

    print("\n" + "-" * 50)

    print("\nItems Sorted by Quantity (High to Low):")

    for i, p in enumerate(sorted_products, start=1):
        print(f"{i}. {p['name']} - {p['quantity']} units")

    print("\nExplanation: Items are sorted using the quantity")
    print("field from highest to lowest.")

    print("\n" + "-" * 50)

    print("\nCategories in Alphabetical Order:")

    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

    print("\nExplanation: The set of unique categories")
    print("was sorted alphabetically for display.")

    print("\n========== END OF REPORT ==========")

else:
    print("No products were added.")

items = []
choice = -1
print(" =====| Welcome |=====")
print(" =====| My Listing |=====")
while choice != 0:
 print("\n==========[ MENU OPTIONS ]==========")
 print("1 - Add Items")
 print("2 - Search for an Item")
 print("3 - Remove an Item")
 print("4 - View all Items (Sorted A-Z or Z-A)")
 print("0 - Exit Program")
 print("====================================")
 try:
 choice = int(input("Pick one [0 to quit]: "))
 except ValueError:
 print("Invalid input. Please enter a number.")
 continue

  if choice == 1:
 while True:
 user_input = input("Enter items (type 'x' to stop):")
 if user_input.lower() == "x":
 break
 items.append(user_input)
 print("Items added successfully.")
 elif choice == 2:
 search_item = input("Enter item to search: ")
 count = items.count(search_item)
 if count > 0:
 print(f"'{search_item}' found {count} time(s).")
 else:
 print("Item not found.")
 elif choice == 3:
 remove_item = input("Enter item to remove: ")
 if remove_item in items:
 items.remove(remove_item)
 print("Item found and deleted.")
 else:
 print("Item not found - deletion unsuccessful.")
 elif choice == 4:
 if not items:
 print("No items to display.")
 else:
 sort_choice = input("Sort A-Z or Z-A? (Enter 'A' or
'Z'): ").upper()
 if sort_choice == "A":
 sorted_items = sorted(items)
 elif sort_choice == "Z":
 sorted_items = sorted(items, reverse=True)
 else:
 print("Invalid sort choice. Defaulting to A-Z.")
 sorted_items = sorted(items)
 print("\nItems in the list:")
 for i, item in enumerate(sorted_items, start=1):
 print(f"{i}. {item}")
 elif choice == 0:
 print("Exiting program... Goodbye!")
 else:
 print("Invalid option. Please try again.")

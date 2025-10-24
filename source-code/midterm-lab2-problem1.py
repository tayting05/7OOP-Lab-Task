rows = int(input("How many rows: "))
cols = int(input("How many cols: "))

print("----------------- Multiplication Table ---------------------")

for r in range(1, rows + 1):
    for c in range(1, cols + 1):
        print(f"{r * c:5d}", end="")
    print()

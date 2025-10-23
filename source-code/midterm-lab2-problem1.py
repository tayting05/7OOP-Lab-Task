rows = int(input("How many rows: "))
cols = int(input("How many Cols: "))
print("----------------- Multiplication Table ---------------------")
for rows in range(1, rows+1):
 for cols in range(1, cols+1):
 print(f" {rows*cols:5d}", end="")
 print ("\n")

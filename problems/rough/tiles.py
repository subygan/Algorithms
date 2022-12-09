input_values = input().split(" ")

l = int(input_values[0])
b = int(input_values[1])
a = int(input_values[2])

columns = l//a
col_residue = l%a
rows = b//a
row_residue = b%a
if col_residue > 0: columns+=1
if row_residue > 0: rows+=1

print(columns*rows)
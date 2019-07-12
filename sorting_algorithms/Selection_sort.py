arr = [1,3,2,4,7,5,9]

print("array before processing:",arr)

for i in range(len(arr)):
    print("entered for:")
    print("     with i:",i)

    min_idx = i
    for j in range(i+1,len(arr)):
        print("        enter for2:")
        print("            with j:",j)
        print("            array before logic:",arr)

        if arr[min_idx]>arr[j]:
            min_idx = j

    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print("finished array: ",arr)
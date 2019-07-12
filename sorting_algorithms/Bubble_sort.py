arr = [1,3,2,-7,4,7,5,9]

print("array before processing:",arr)

for i in range(len(arr)):
    print("entered for:")
    print("     with i:",i)

    for j in range(i+1,len(arr)):
        print("        enter for2:")
        print("            with j:",j)
        print("            array before logic:",arr)
        if arr[j]<arr[i]:
            arr[j],arr[i] = arr[i],arr[j]
        else:
            continue
        print("             array after logic:",arr)

print("finished array: ",arr)
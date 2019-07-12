#use smaller array
#so that the steps are easuy to follow

arr = [1,11,2,8,9,4,5,6,7,12,-1]



for index in range(1,len(arr)):

    print("entered for:")
    print("    arr:",arr)
    print("    index:",index)
    position = index
    count = 0

    #while conditions are used like conditional statements, if
    #true enter, else end.
    #most places the use case is the same.

    while position >0 and arr[position-1]>arr[position]:

        print("        entered while",count,":")
        print("            arr:",arr)
        arr[position],arr[position-1] = arr[position-1],arr[position]
        position = position - 1

        print("             position:",position)
        print("            after while logic:",arr)
        print("\n")
        count = count+1
    print("    while exit.\n")
print("final array:",arr)
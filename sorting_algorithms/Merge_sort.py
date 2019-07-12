#time complexity        =
#number of comparisons  =

def mergeSort(arr,recursive):

    #recursive functions need these ifs because when they reach the end of their
    #recursion they need to return some value.
    #if you notice, the implicit (implicit because not mentioned) else function returns the value
    if len(arr) >1:

        mid = len(arr)//2 #Finding the mid of the array
        L = arr[:mid] # Dividing the array elements
        R = arr[mid:] # into 2 halves

        #variable to measure how much deep the recursion goes
        recursive = recursive + 1

        print("mergesort called for first half: ",L)
        print("    recursive: ",recursive)
        mergeSort(L,recursive) # Sorting the first half
        print("mergesort called for second half: ",R)
        print("    recursive: ",recursive)
        mergeSort(R,recursive) # Sorting the second half

        i = j = k = 0

        # Copy_to_temp arrays L[] and R[]

        #this while loop takes the two argument (L,R) and
        #rewrites it in the temporary loop which in this case becomes
        #arr[] that was broken down by recursion

        while i < len(L) and j < len(R):

            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):

            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):

            arr[k] = R[j]
            j += 1
            k += 1


            print("        after while logic: ")
            print("            arr:",arr)
            print("              k:",k)
            print("              i:",i)
            print("              j:",j)



  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    print(arr)
    recursive = 0
    mergeSort(arr,recursive)
    print("Sorted array is: ", end="\n") 
    print(arr)
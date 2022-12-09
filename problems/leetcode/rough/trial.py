def remover(nums) :

    end = False
    previous = nums[i]
    i = 0
    while not end:
        i+=1
        internal_end = False
        while not internal_end:

            if previous == nums[i]:
                del nums[i]
            else:
                break

        i += 1
        previous = nums[i]

remover([1,2,3,4,5,5,6,6,7])
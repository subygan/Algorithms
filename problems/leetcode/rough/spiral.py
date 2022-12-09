matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

# matrix = [[0],[0]]

def traverse (matrix, my_list):


    # print('   <<<====== recursed ======>>>')
    # print(matrix)
    if matrix:
        m = len(matrix)
        n = len(matrix[0])
        this_row = [0] * m
        count = 0
        for i in range(0, m+2):
            # print('for :', count)
            count+=1
            if i == 0 :
                my_list += matrix[i]
                matrix[i] = ['v']
                # print(matrix)
            elif i == m :
                my_list+=matrix[i-1][::-1]
                del matrix[-1]
                # print(matrix)
            else:
                # print(matrix)
                if i+1 == m:
                    for row in range(1,m-1):
                        # print("row",row)
                        my_list += [matrix[row][-1]]
                        # print(my_list)
                        # this_row[i] = 1
                        del matrix[row][-1]
                elif i > m:

                    for row in range(m-2,0,-1):
                        # print("row", row)
                        my_list.append(matrix[row][0])
                        del matrix[row][0]
        #     print('floor :', matrix)
        #     print('floor_list :', my_list)
        # print('end of for')
        if matrix:
            del matrix[0]
        else:
            return my_list[:-1]
        # print('!!',matrix)
        # if matrix:
        #     del matrix[-1]
        # print(matrix)
        # print(my_list)
        return traverse(matrix, my_list)
    else:
        # print(my_list)
        # print(matrix)
        return my_list[::-1]

print(traverse(matrix, []))


def alice_eats(arrangement_now, alice_count, bob_last, alice_position, bob_position, done):
    print('   <<<=== Alice ====>>>  ')
    print(arrangement_now, alice_count, bob_last, alice_position, bob_position)
    now_count = 0

    for i in range(alice_position, len(arrangement_now)) :
        print(i)
        print(arrangement_now)
        print(arrangement_now[i], now_count)
        if alice_position <= bob_position-1 and (now_count < bob_last or now_count == 0 ):
            now_count += arrangement_now[i]
            alice_position = i+1
        else:
            if alice_position>bob_position-1:
                done = 1
            break

    alice_last = now_count
    alice_count+=now_count
    print('-----')
    print(alice_position, bob_position)
    print(alice_last)

    return arrangement_now, alice_count, alice_last, alice_position, done


def bob_eats(arrangement_now, bob_count, alice_last, alice_position, bob_position, done):
    print('   <<<<=====  BOB =====>>>>')
    print(arrangement_now, bob_count, alice_last, alice_position, bob_position)
    now_count = 0
    for i in range(bob_position,0,-1) :
        print(i)
        print(arrangement_now)
        print(arrangement_now[i-1], now_count)
        if bob_position > alice_position and (now_count < alice_last or now_count == 0):
            now_count += arrangement_now[i-1]
            bob_position = i-1
        else:
            if alice_position >= bob_position:
                done = 1
            break

    bob_last = now_count
    bob_count += now_count
    print('-----')
    print(alice_position, bob_position)
    print(bob_last)
    return  arrangement_now, bob_count, bob_last, bob_position, done

if __name__ == '__main__' :

    for _ in range(int(input())) :

        number = int(input())
        arrangement = list(map(int,input().split()))
        alice_last, bob_last = 0,0
        alice_count,bob_count = 0,0
        alice_position, bob_position = 0, len(arrangement)
        arrangement_now = arrangement
        count = 0
        steps = 0
        done = 0
        while not done and count<len(arrangement):

            if bob_position > alice_position:
                arrangement_now, alice_count, alice_last, alice_position, done = alice_eats(arrangement_now, alice_count, bob_last, alice_position, bob_position, done)
                print("<<<======>>>")
                print(" done :", done)
                print(arrangement_now, alice_count, alice_last)
                steps+=1
                if done:
                    break

            else:
                steps +=1
                break
            print('steps :', steps)
            if bob_position > alice_position :

                arrangement_now, bob_count, bob_last, bob_position, done = bob_eats(arrangement_now, bob_count, alice_last, alice_position, bob_position, done)
                print("<<<=======>>")
                print(" done :", done)
                print(arrangement_now, bob_count, bob_last)
                steps+=1
            else :
                steps +=1
            print('steps :', steps)


        print(steps, alice_count, bob_count)



#         # print(alice_eats([1, 4, 1, 5, 9, 2, 6, 5, 3],3,5))

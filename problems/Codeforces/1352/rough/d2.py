def alice_eats(arrangement, alice_count, bob_last, done, alice_now, bob_now):

    # print('<<<==== Alice ====>>')
    # print(arrangement, alice_count, bob_last, alice_now, bob_now)
    now_count = 0
    for element in range(alice_now, bob_now+1) :
        # print(element, arrangement[element], now_count)
        if (now_count <= bob_last or now_count == 0) and alice_now <= bob_now :
            now_count += arrangement[element]
            alice_now = element+1
        else:
            if alice_now > bob_now :
                done = 1
            break
    alice_last = now_count
    alice_count += now_count

    # print(alice_count, alice_last, done, alice_now, bob_now)
    return alice_count, alice_last, done, alice_now, bob_now


def bob_eats(arrangement, bob_count, alice_last, done, alice_now, bob_now):
    # print('<<<===== Bob =====>>>')
    # print(arrangement, bob_count, alice_last, alice_now, bob_now)
    now_count = 0
    for element in range(bob_now,alice_now-1,-1):
        # print(element, arrangement[element], now_count)
        if now_count <= alice_last and alice_now <= bob_now :
            now_count += arrangement[element]
            bob_now = element -1
        else :
            if alice_now > bob_now:
                done = 1
            break
    bob_count += now_count
    bob_last = now_count
    # print('------')
    # print(bob_count, bob_last, done, alice_now, bob_now)
    return bob_count, bob_last, done, alice_now, bob_now


if __name__ == '__main__':
    for _ in range(int(input())) :
        number = input()
        arrangement = list(map(int, input().split()))
        alice_count, bob_count = 0,0
        alice_last, bob_last = 0,0
        alice_now, bob_now = 0,len(arrangement)-1
        done = 0
        count = 0

        while not done and count<len(arrangement):
            # print('<<---------------------------->>>')
            alice_count, alice_last, done, alice_now, bob_now = alice_eats(arrangement, alice_count, bob_last, done, alice_now, bob_now)
            # print("<<<======>>>")
            # print(" done :", done)
            # print(arrangement, alice_count, alice_last)
            count+=1
            if done or bob_now < alice_now:
                break
            bob_count, bob_last, done, alice_now, bob_now = bob_eats(arrangement, bob_count, alice_last,done, alice_now, bob_now)
            # print("<<<======>>>")
            # print(" done :", done)
            # print(arrangement, bob_count, bob_last)
            count+=1
            if done or bob_now < alice_now:
                break
        print(count, alice_count, bob_count)
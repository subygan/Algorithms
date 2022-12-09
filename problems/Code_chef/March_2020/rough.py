import timeit, json
def my_function():
    my_dict = {"a" : 1,"a1" : 1,"a2" : 1,"a3" : 1,"a4" : 1,"a5" : 1,"a6" : 1,"a7" : 1,"as" : 1,"ad" : 1,"da" : 1,"adf" : 1,"asf" : 1,"af" : 1,"as4" : 1,"am" : 1,"aq" : 1,"ap" : 1,"ay" : 1,"a98" : 1,"a59" : 1,"a0" : 1,"a10" : 1,"a14y3" : 1,"a098" : 1,"a1341" : 1,"a54" : 1,"a13" : 1,"a[" : 1,"adfa" : 1}

    if "09383444" not in my_dict:
        print("yes")

print(timeit.timeit(my_function, number=100000))


def fun1():
    x=20

    def fun2():
        global x
        x=25

    print("Before calling fun2: ",x)
    print("calling function 2")
    fun2()
    print("after calling fun2: ",x)

fun1()
print("x in main: ",x)

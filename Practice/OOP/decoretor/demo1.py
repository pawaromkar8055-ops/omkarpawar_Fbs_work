# def demo():
#     print("I am in demo")
# #print(type(demo))
# #a=10
# #print(type(a))
# x=demo
# #demo
# x()
# ## 3rd step
# def fun(a):
#  a()
# def demo():
#     print("I am in demo")
# x=demo
# fun(x)
# #4 step
# def outer():
#     print("I am in outer function")
# def innerfun():
#     print("I am in inner function")
##closure 
# def outer():


# 28-9-2026
# 1 step 
# understand that your fuction is nothing but object of function class

# 2 step
#we can stored the function in variable....
# def demo():
#     print("I am in demo")
# x=demo
# demo()

# 3 step
# def demo(a):
#     a()
# def fun():
#     print("I am in tested fuction")
# demo(fun)

# 4 step
#return one function from other function
# def outerfun():
#     print("I am in outer")
#     def innerfun():
#         print("I am in innwe function")
#     return innerfun
# result=outerfun()
# result

#clours funtion
# is a function which pass everthing to its neber or other function
# def demo():
#     a="FBS"
#     def innerfun():
#         print("I am in innerfunction",a)
#     return innerfun
# res=demo()
# res()

##decoreter
def decore(a):
    # print("I am in decore")
    def innerfun(*args):
        print("Time started")
        print("Logger added")
        a(*args)
        print("Time stopeed")
        print("Logger removed")
    return innerfun   

@decore
def login():
    print("log in is Done")
    
@decore
def logout():
    print("logout in is Done")

# res=decore(login)
# res()
login()
# logout()
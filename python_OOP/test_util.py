# -*- coding: utf-8 -*-
# @Time    : 2022/1/14 14:36
# @Author  : lenny
# @desc    :a

# Python’s functions are objects


def shout(word="yes"):
    return word.capitalize() + "!"


print(shout())
scream = shout
del shout
try:
    print(shout())
except NameError as e:
    print(e)
    # outputs: "name 'shout' is not defined"

print(scream())


# they can be defined inside another function!
def talk():
    # You can define a function on the fly in "talk" ...
    def whisper(word="yes"):
        return word.lower() + "..."

    # ... and use it right away!
    print(whisper())


talk()


# can be assigned to a variable & can be defined in another function
# so, that means that a function can return another function
def getTalk(kind="shout"):
    # We define functions on the fly
    def shout(word="yes"):
        return word.capitalize() + "!"

    def whisper(word="yes"):
        return word.lower() + "..."

    # Then we return one of them
    if kind == "shout":
        # We don't use "()", we are not calling the function,
        # we are returning the function object
        return shout
    else:
        return whisper


talk1 = getTalk
print(talk1)
print(talk1())
print(talk1("whisper")())


# decorators are “wrappers”, which means that they let you execute code before and after the function they decorate
# without modifying the function itself.
# 装饰器是“包装器”，这意味着它们允许您在它们装饰的函数之前和之后执行代码，而不修改函数本身

# A decorator is a function that expects ANOTHER function as parameter
def my_shiny_new_decorator(a_function_to_decorate):
    # Inside, the decorator defines a function on the fly: the wrapper.
    # This function is going to be wrapped around the original function
    # so it can execute code before and after it.
    def the_wrapper_around_the_original_function():
        # Put here the code you want to be executed BEFORE the original function is called
        print("Before the function runs")

        # Call the function here (using parentheses)
        a_function_to_decorate()

        # Put here the code you want to be executed AFTER the original function is called
        print("After the function runs")

    # At this point, "a_function_to_decorate" HAS NEVER BEEN EXECUTED.
    # We return the wrapper function we have just created.
    # The wrapper contains the function and the code to execute before and after. It’s ready to use!
    return the_wrapper_around_the_original_function


# Now imagine you create a function you don't want to ever touch again.
def a_stand_alone_function():
    print("I am a stand alone function, don't you dare modify me")


a_stand_alone_function()
# outputs: I am a stand alone function, don't you dare modify me

# Well, you can decorate it to extend its behavior.
# Just pass it to the decorator, it will wrap it dynamically in
# any code you want and return you a new function ready to be used:

a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function_decorated()


# outputs:
# Before the function runs
# I am a stand alone function, don't you dare modify me
# After the function runs

@my_shiny_new_decorator
def another_stand_alone_function():
    print("Leave me alone")


another_stand_alone_function()


class C(object):

    @staticmethod
    def f():
        print("runoob")

C.f()
cobj = C()
cobj.f()

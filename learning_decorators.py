def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)

divide(1,0)
divide(5, 2.5)

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")

def do_twice(func):
    def wrapper_do_twice(victim):
        for i in range(10000):
            func(victim)
            func(victim)
    return wrapper_do_twice

@do_twice
def gorc(victim):
    print(f"Gorca GORCED {victim}")

gorc("Thomas")
gorc("Morca")

import math


def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))

print(approximate_e(10))

for t in int, float, dict, list, tuple, 3, 5.3, {"Name": "Gorca", "Hobby": "Gorcing"}, ["Gorca", "Thorca", "Corca"], (1,2,4):
     print(type(t))

def extra(self, arg):
    ...
def extras(Class):
    Class.extra = extra
class Client1: ...
extras(Client1)
class Client2: ...
extras(Client2)
class Client3: ...
extras(Client3)
X = Client1()
print(X.extra("1"))

class Meta(type):
    def __new__(meta, classname, supers, classdict):
        return type.__new__(meta, classname, supers, classdict)

class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new:', meta, classname, supers, classdict, sep='\n...')

class Eggs: pass

print('making class')

class Spam(Eggs, metaclass=MetaOne):
    data = 1
    def meth(self, arg):
        return self.data + arg
print('making instance')
# X = Spam()
# print('data:', X.data, X.meth(2))

class SuperMeta(type):
    def __call__(meta, classname, supers, classdict):
        print('In SuperMeta.call: ', classname, supers, classdict, sep='\n...')
        return type.__call__(meta, classname, supers, classdict)
    def __init__(Class, classname, supers, classdict):
        print('In SuperMeta init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))
print('making metaclass')
class SubMeta(type, metaclass=SuperMeta):
    def __new__(meta, classname, supers, classdict):
        print('In SubMeta.new: ', classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)
    def __init__(Class, classname, supers, classdict):
        print('In SubMeta init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))
class Eggs:
    pass
print('making class')
class Spam(Eggs, metaclass=SubMeta):
    data = 1
    def meth(self, arg):
        return self.data + arg

print('making instance')
def fibonacci(n):
    f = [0, 1]

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]

import datetime
time1 = (datetime.datetime.now().timestamp())
print(fibonacci(10000))
time2 = (datetime.datetime.now().timestamp())
print(str(time2-time1) + "seconds")

def best_sum(target_sum, numbers):
    memo = {}

    def helper(target_sum, numbers):
        if target_sum == 0:
            return []
        if target_sum in memo:
            return memo[target_sum]
        shortest_combination = None
        for num in numbers:
            remainder = target_sum - num
            if remainder >= 0:
                combination = helper(remainder, numbers)
                if combination is not None:
                    combination = combination + [num]
                    if shortest_combination is None or len(combination) < len(
                        shortest_combination
                    ):
                        shortest_combination = combination
        memo[target_sum] = shortest_combination
        return memo[target_sum]

    return helper(target_sum, numbers)

def mysum(nums):
    if nums == []:
        return 0
    else:
        return nums[0] + mysum(nums[1:])
    
mysum([1,2,3,4])

def add1_all(nums):
    if nums == []:
        return []
    else:
        return [nums[0] + 1] + add1_all(nums[1:])
    
add1_all([1,2,3])


class Person(object):
    def __init__(self, name):
        self.name = name
        
class Group(object):
    """Groups can contain Persons or more Groups."""
    def __init__(self, members, subgroups):
        self.members = members
        self.subgroups = subgroups
    
def get_all_members(group):
    sub_members = []
    for subgroup in group.subgroups:
        sub_members.extend(get_all_members(subgroup))
    return group.members + sub_members
    
group = Group(['Sam', 'Jessie'], [Group(['Reese', 'Taylor'], [])])
get_all_members(group)


def search(alist, target):
    for v in alist:
        if target == v:
            return True
    return False


def searchRecursive(alist, target):
    if len(alist) == 0:
        return False    # <-- base case
    
    if alist[0] == target:
        return True
    return searchRecursive(alist[1:], target)


def search(n, value):
    # Base Case
    if n is None:
        return False
    
    # Action and Recursive Step
    if n.value == value:
        return True
    return search(n.next, value)


def sumList(n):
    # Base case
    if n is None:
        return 0
    
    # Action and Recursive Step
    return n.value + sumList(n.next)


numbers = [9,3,4,6,7,8,2,3]
group = {2,3,5,7}

# helper function
def helper(x):
    if x in group:
        return(0, x)
    return(1, x)

numbers.sort(key=helper)
print(numbers)


# loop structures and booleans
# common structures

# post-test loop
# seeding with first iteration
number = -1
while number < 0:
    number = eval(input("Enter a positive number: "))
    
print("positive number was: {}".format(number))

# Enter a positive number: 1
# positive number was: 1

  
# loop and a half
# sentinel loop
"""
while True:
    Get next data item
    if the item is the sentinel: break
    process the item
"""
while True:
    number = eval(input("Enter a positive number: "))
    if number >=0: break
    print("The number was not positive.")
    
print("positive number was: {}".format(number))


# Enter a positive number: -1
# The number was not positive.
# Enter a positive number: 5
# positive number was: 5

# accumulator pattern in a function
def accumulate(n):
    sum = 0
    s = range(n)
    
    for i in s:
        sum = sum + s[i] 
    return sum

accumulate(5)


# rotate_left3([1, 2, 3]) → [2, 3, 1]
# rotate_left3([5, 11, 9]) → [11, 9, 5]
# rotate_left3([7, 0, 0]) → [0, 0, 7]

def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]

def reverse3(nums):
    n = []
    for i in nums[::-1]:
        n.append(i)
    return n

print(rotate_left3([7, 0, 0]))

print(reverse3([7, 0, 0]))


def half(alist):
    #             6 / 2
    mid = len(alist)//2
    print(mid)
    
    lefthalf = alist[:mid]
    righthalf = alist[mid:]
    
    return 'left: {}, right: {}'.format(lefthalf, righthalf)
    
a = [1,2,3,4,5,6]
half(a)



a = [0,2,3,2,1]

def duplicate(alist):
    d = dict()
    for i in alist:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d

a = [0,2,3,2,1]
duplicate(a)
# {0: 1, 1: 1, 2: 2, 3: 1}

# dictionary occurences
alist = ['AA', 'XOM', 'MCD', 'GE', 'DD', 'LULU', 'XOM', 'XOM']
d = {}

for a in alist:
    if a not in d:
        d[a] = 0
    d[a] += 1


alist = ['AA', 'XOM', 'MCD', 'GE', 'DD', 'LULU', 'XOM', 'XOM']
def add_letter(alist, target):
    n = []
    for a in alist:
        if target in a:
            x = '_'.join(a)
            n.append(x)
    return n

add_letter(alist, 'C')
# ['M_C_D']

def revlist(n):
    return n[::-1]

alist = [1,2,6,7,8]
x = revlist(alist)
x
# [8, 7, 6, 2, 1]


d = {'one':1, 'two':2, 'three':3, 'four':4}

dictlist = list()
for key, value in d.iteritems():
    temp = [key,value]
    dictlist.append(temp)
    
print dictlist


List of pairs to dictionary

string = [('limited', 1), ('all', 16), ('concept', 1), ('secondly', 1)]
my_dict = dict(string)
my_dict
{'all': 16, 'secondly': 1, 'concept': 1, 'limited': 1}

Example 3.25. The keys, values, and items Functions
>>> params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
>>> params.keys()   1
['server', 'uid', 'database', 'pwd']
>>> params.values() 2
['mpilgrim', 'sa', 'master', 'secret']
>>> params.items()  3
[('server', 'mpilgrim'), ('uid', 'sa'), ('database', 'master'), ('pwd', 'secret')]

>>> params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
>>> params.items()
[('server', 'mpilgrim'), ('uid', 'sa'), ('database', 'master'), ('pwd', 'secret')]
>>> [k for k, v in params.items()]                1
['server', 'uid', 'database', 'pwd']
>>> [v for k, v in params.items()]                2
['mpilgrim', 'sa', 'master', 'secret']
>>> ["%s=%s" % (k, v) for k, v in params.items()] 3
['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))
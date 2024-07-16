#collections:

##from collections import Counter
##print(Counter(["a","a","b","b"]))
##print(Counter({"a":2, "b":2}))
##print(Counter(a=2,b=2))

###ordered dic:
##from collections import OrderedDict
##print("This is a Dict:\n")
##d={}
##d['a']=1
##d['b']=2
##d['c']=3
##d['d']=4
##for key,value in d.items():
##    print(key,value)


##from collections import OrderedDict
##od = OrderedDict()
##od['a']=1
##od['b']=2
##od['c']=3
##od['d']=4
##print('Before Deleting')
##for key,value in od.items():
##    print(key,value)
##
##od.pop('a')
##od['a'] = 1
##print('\nAfter re-inserting')
##for key,value in od.items():
##    print(key,value)

###default:
##from collections import defaultdict
##d=defaultdict(list)
##for i in range(5):
##    d[i].append(i)
##print("Dictinary with values as list:")
##print(d)


###chain map:
##from collections import ChainMap
##d1 = {'a' : 1, 'b' : 2}
##d2 = {'c' : 3, 'd' : 4}
##d3 = {'e' : 5, 'f' : 6}
##c=ChainMap(d1,d2,d3)
##print(c)


###named typle:
##from collections import namedtuple
##Student = namedtuple('Student', ['name','age','dob'])
##S=Student("Mukilan",18,"13-11-2006")
##print("The student data is: ",S)
##

###deque:
##from collections import deque
##queue = deque(['name','age','dob'])
##print(queue)















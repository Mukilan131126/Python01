##a=1
##b=2
##print(a+b)

###tuple:
##my_tuple=("apple","banana","orange")
##print(my_tuple)

###allow duplicates:
##my_tuple=("apple","orange","pineapple","mango", "apple","grapes")
##print(my_tuple)

###tuple length:
##my_tuple=("apple","orange","pineapple","mango", "apple","grapes")
##print(len(my_tuple))

###tuple:
##my_list=(1,)
##print(my_list)

###tuple constructor:
##my_tuple=tuple(("apple","banana","cherry"))
##print(my_tuple)

###acess tuple:
##my_tuple=("apple","mango","banana")
##print(my_tuple[1])

###negative indexing:
##my_tuple=("apple","banana","cheery")
##print(my_tuple[-2])

###range of index:

##my_tuple=("apple","orange","pineapple","mango", "apple","grapes")
##print(my_tuple[2:5])

##my_tuple=("apple","orange","pineapple","mango", "apple","grapes")
##print(my_tuple[2:])


##my_tuple=("apple","mango","banana")
##if "apple" in my_tuple:
##    print("Yes, 'apple' is in the fruits tuple")

###update tuple:
##x=("apple","banana","cherry")
##y=list(x)
##y[1]="kiwi"
##x=tuple(y)
##print(x)


###add:
##my_tuple=("apple","mango","grapes")
##y=("orange",)
##my_tuple +=y
##print(my_tuple)


###remove:
##my_tuple=("apple","mango","grapes")
##y=list(my_tuple)
##y.remove("apple")
##my_tuple= tuple(y)
##print(my_tuple)

###unpack tuple:
##my_tuple=("apple","banana","cherry")
##print(my_tuple)

##my_tuple=("apple","banana","cherry")
##(red,yellow,green)=my_tuple
##print(red)
##print(yellow)
##print(green)

###loop:
##my_tuple=("apple","banana","cherry")
##for x in my_tuple:
##    print(x)

##my_tuple=("apple","banana","cherry")
##for i in range(len(my_tuple)):
##    print(my_tuple[i])


###join two tuples:
##tuple1=("a","b","c","d")
##tuple2=(1,2,3,4)
##tuple3 = tuple1 + tuple2
##print(tuple3)

###multiple tuple:
##fruits=("apple","banana","cherry")
##my_tuple=fruits*2
##print(my_tuple)

#tuple methods:
###count:
##my_tuple=(1,2,3,4,5,6)
##x=my_tuple.count(5)
##print(x)

###index:
##my_tuple=(1,3,5,7,9,2,4,6,8,10)
##x=my_tuple.index(6)
##print(x)

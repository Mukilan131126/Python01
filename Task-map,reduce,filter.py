###Square all numbers in a list:
##
##def double(n):
##    return n*2
##numbers = [1,2,3,4,5]
##result = map(double,numbers)
##print(list(result))

###covert all strings to upper case in list:
##def str(n):
##    return n.upper()
##list_1=["mukilan","thirumurugan"]
##res=map(str,list_1)
##print(list(res))


###Add 10 to each number in a list:
##def add(n):
##    return n+10
##list_1=[1,2,3,4,5,6,7,8,9,10]
##res=map(add,list_1)
##print(list(res))

###double each number in a list:
##def double(n):
##    return n*2
##numbers=[1,2,34,5,6]
##result=map(double,numbers)
##print(list(result))


###capatilize:
##def cap(n):
##    return n.capitalize()
##str=["mukilan","thiru"]
##capitalize_str=list(map(cap,str))
##print(capitalize_str)


###filter even numbers from the list:
##def even(n):
##    return n%2==0
##numbers=[1,2,3,4,5,6,7,89]
##even_numbers=filter(even,numbers)
##print("even numbers:",list(even_numbers))

###shorter than four character:
##def chara(n):
##    return len(n)<=4
##x=["mukilan","thiru","hari","sum"]
##res=filter(chara,x)
##print(list(res))

###numbers greater than 10:
##def num(n):
##    return n>10
##x=[1,2,7,11,14,67,90]
##res=filter(num,x)
##print(list(res))



###strings contain letter a:
##def letter(n):
##    return "a" in n
##a=["mukilan","thiru","hari"]
##res=filter(letter,a)
##print(list(res))

###numbers not divisible by 3:
##def num(n):
##    return a%3!=0
##numbers=[1,3,4,6,7,8,82,31]
##res=filter(lambda x:x%3!=0,numbers)
##print(list(res))

###negative numbers:
##def num(n):
##    return n<0
##x=[1,2,3,4,5-2,-4,-6]
##res=filter(num,x)
##print(list(res))

###all numbers in a list:
##import functools
##num=[1,3,5,6,7]
##product=functools.reduce(lambda x,y:x*y,num)
##print("product of list elements:",product)

###concatenate a list of string:
##import functools
##strings=["mukilan","world","python"]
##res= functools.reduce(lambda x,y:x+y, strings)
##print("concatenate a list of a string:",res)

###maximum number  in a list:
##import functools 
##num=[2,4,5,45,7,23]
##max_num= functools.reduce(lambda a,b:a if a>b else b,num)
##print(max_num)

### sum of squares the numbers:
##import functools
##num=[1,2,3,4,5]
##sum= functools.reduce(lambda a,x:a+x**2,num,0)
##print(sum)

###factorial of the number in a list:
##import functools
##def fact(n):
##    global x
##    x=functools.reduce(lambda x,y:x*y,range(1,n+1),1)
##num=5
##res=fact(num)
##print("factorial of a number",x)
##
##




   

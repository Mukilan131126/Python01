#break,continue,pause:

###numbers from 1 to 10:
##
##for i in range(1,11):
##    if i==5:
##        break
##    print(i)

###negative number in the list:
##a=[2,4,-6,-1,8,9]
##for i in a:
##    if i<0:
##        break
##print(i)

###encounter a zero:
##
##a=[1,4,6,9,0,-1,2,3]
##for i in a:
##    if i==0:
##        break
##    print(i)


###numbers grom 1 to  10,skipping 5:
##for i in range(1,11):
##    if i==5:
##        continue
##    print(i)


###iterate over a list and skip negative numbers:
##a=[1,2,3,4,5,6,-8,-6,7,8,-9]
##for i in a:
##    if i<0:
##        continue
##    print(i)

###characters of a string skipping vowels:
##a="Mukilan"
##vowels="aeiouAEIOU"
##for i in a:
##    if i in vowels:
##        continue
##    print(i)


###numbers from 1 to 20,skip multiples of 3:
##for i in range(1,21):
##    if i%3==0:
##        continue
##    print(i)


###iterate over a list and use pass for future implementation:
##numbers=[1,2,3,4,5,6,7,8]
##for i in numbers:
##    if i%2==0:
##        pass
##    print(i)


###numbers from 1 to 10,skip 5 and stop at 8:
##for i in range(1,11):
##    if i==5:
##        continue
##    elif i==8:
##        break
##    else:
##        print(i)
        

###only odd numbers from 1 to 10,but use pass for even numbers:
##for i in range(1,11):
##    if i%2==0:
##        continue
##    print(i)
##

###iterate over a list,skip negatives,print positives,stop at zero:
##a=[1,2,3,4,5,-6,-1,-2,-3,0,12,14,16]
##for i in a:
##    if i<0:
##        continue
##    elif i==0:
##        break
##    else:
##        print(i)
##        pass


###skip the first half of the list,process the second half,use pass for future:
##num=[1,2,3,4,5,6,7,8,9,10]
##midpoint = len(num)//2
##for i in range (midpoint,len(num)):
##    pass
##    print(num[i])
##























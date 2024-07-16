#logic:

##def cigar_party(cigars, is_weekend):
##  if is_weekend:
##    return cigars>=40
##  else:
##    return 40<=cigars <=60
##print(cigar_party(30, False))



##def date_fashion(you, date):
##  if you <=2 or date<=2:
##    return 0
##  elif you >=8 or date >=8:
##    return 2
##  else:
##    return 1
##print(date_fashion(5, 10))



##def caught_speeding(speed, is_birthday):
##  if is_birthday:
##    speed-=5
##  if speed <=60:
##    return 0
##  elif 61<=speed<=80:
##    return 1
##  else:
##    return 2
##print(caught_speeding(60, False))




##def sorta_sum(a, b):
##  sum=a+b
##  if 10<=sum<=19:
##    return 20
##  else:
##    return sum
##print(sorta_sum(3,4))


##def alarm_clock(day, vacation):
##  if vacation:
##    if day==0 or day==6:
##      return'off'
##    else:
##      return"10:00"
##  else:
##    if day==0 or day==6:
##      return"10:00"
##    else:
##      return "7:00"
##print(alarm_clock(1, False))
##





##def love6(a, b):
##  return a==6 or b==6 or a+b==6 or abs (a-b)==6
##love6(6, 4) 
##love6(4, 5) 
##love6(1, 5) 
##print(love6(6,4))



##def in1to10(n, outside_mode):
##  if outside_mode:
##    return n<=1 or n>=10
##  else:
##    return 1<=n <=10
##print(in1to10(5,False))

##def near_ten(num):
##  return num%10<=2 or num%10>=8
##near_ten(12) 
##near_ten(17) 
##near_ten(19)
##print(near_ten(12))



















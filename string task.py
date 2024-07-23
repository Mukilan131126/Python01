##def hello_name(name):
##
##       print("Hello "+ name + "!")
##
##hello_name("Bob")
##
##
##
##def make_abba(a,b):
##       return a+b+b+a
##print(make_abba("hi","bye"))
##
##
##
##def make_tags(tag, word):
##    return "<"+tag+">"+word+"</"+tag+">"
##    
##print(make_tags('i', 'Yay'))
##
##
##
##
##def make_out_word(out, word):
##    return out[:2]+word+out[2:]
##    
##print(make_out_word('<<>>', 'Yay'))
##
##
##
##
##def extra_end(str):
##    return str[-2:]*3
##print(extra_end("Hello"))
##
##
##
##
##
##def first_half(str):
##    a=len(str)/2
##    print(str[0:a])
##
##
##
##first_half('WooHoo')


##def without_end(str):
##  return str[1:-1]
##print(without_end('Hello'))





##def combo_string(a, b):
##  if len(a)<len(b):
##    short=a
##    long=b
##  else:
##    short=b
##    long=a
##  return short+long+short
##combo_string('Hello','hi')
##combo_string('hi','Hello')
##combo_string('aaa','b')
##print(combo_string('Hello','hi'))




##def non_start(a, b):
##  return a[1:] + b[1:]
##non_start('Hello','There')
##non_start('java','code')
##non_start('shotl','java')
##print(non_start('Hello','There'))







##def left2(str):
##   return str[2:] + str[:2]
##left2('Hello')
##left2('java')
##left2('Hi')
##print(left2('Hello'))













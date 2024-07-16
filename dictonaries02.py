##a=2
##b=1
##print(a+b)
##
##
##my_student = {
##    "student1" : {
##        "name" : "mukilan",
##        "year" : 2006
## },
##    "student2" : {
##        "name" : "thiru murugan",
##        "year" : 2007
## },
##    "student3" : {
##        "name" : "kavi",
##        "year" : 2005
## },
##}
##
####print(my_student)
##
##    
##student1 = {
##        "name" : "mukilan",
##        "year" : 2006
## }
##student2 = {
##        "name" : "thiru murugan",
##        "year" : 2007
## }
##student3 = {
##        "name" : "kavi",
##        "year" : 2005
## }
##
##my_student = {
##    "student1" : student1,
##    "student2" : student2,
##    "student3" : student3
##}
##
##print(my_student)
    


##my_student = {
##    "student1" : {
##        "name" : "mukilan",
##        "year" : 2006
## },
##    "student2" : {
##        "name" : "thiru murugan",
##        "year" : 2007
## },
##    "student3" : {
##        "name" : "kavi",
##        "year" : 2005
## }
##}
##print(my_student["student2"]["name"])
##


###nested:
##my_student = {
##    "student1" : {
##        "name" : "mukilan",
##        "year" : 2006
## },
##    "student2" : {
##        "name" : "thiru murugan",
##        "year" : 2007
## },
##    "student3" : {
##        "name" : "kavi",
##        "year" : 2005
## }
##}
##for x , obj in my_student.items():
##    print(x)
##
##    for y in obj:
##        print(y + ':', obj[y])
##

#methods:
###clear:
##student = {
##        "name" : "mukilan",
##        "year" : 2006
## }
##student.clear()
##print(student)
    

###copy:
##student = {
##        "name" : "mukilan",
##        "year" : 2006
## }
##student.copy()
##print(student)


###formkeys:
##student = ("name" , "mukilan", "year" , 2006)
##teachers = 0
##thisdict = dict.fromkeys(student,teachers)
##print(thisdict)


#get:

##student = {
##        "name" : "mukilan",
##        "year" : 2006
## }
##student.get("year")
##print(student)



##student = {
##        "name" : "mukilan",
##        "year" : 2006
## }
##x=student.items()
##print(x)
##
##
##
##student = {
##        "name" : "mukilan",
##        "year" : 2006
## }
##x = student.keys()
##print(x)


###pop:
##student = {
##        "name" : "mukilan",
##        "year" : 2006
## }
##student.pop("name")
##print(student)

###popitem:
##student = {
##        "name" : "mukilan",
##        "year" : 2006
## }
##student.popitem()
##print(student)


#####setdefault:
####student = {
####        "name" : "mukilan",
####        "year" : 2006
#### }
####x = student.setdefault("year",2007)
####print(x)

##update:
##student = {
##        "name" : "mukilan",
##        "year" : 2006
## }
##student.update({"batch" : 24})
##print(student)

####values:
##student = {
##        "name" : "mukilan",
##        "year" : 2006
## }
##x = student.values()
##print(x)










#BRUTE FORCE:
# a=['s','u','p','r','a','j','e']
#
# def isUnique(a):
#     for i in range(0,len(a)):
#         ele=a[i]
#         for j in range(i+1,len(a)):
#             if ele==a[j] :
#                 return "NOT UNIQUE"
#     return "unique"
#
#
# print(isUnique(a))
# dict={'a':1,'b':2}
# v=dict.keys()
a=['s','u','p','r','a','j','e']
dic={}

def Datastructure(a,dic):
    for i in range(0,len(a)):
        if(a[i] not in dic):
                dic[a[i]]= 0
        else:
            val=dic[a[i]]
            dic[a[i]]=val+1
Datastructure(a,dic)

def checkForUnique(dic):
    for i in dic:
        if(dic[i]>0):
            return 'not unique'
    return "unique"
print(checkForUnique(dic))

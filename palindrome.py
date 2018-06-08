def palindrome(s):
    dic={}
    for i in range(0,len(s)):
        if(s[i] not in dic):
            dic[s[i]]=1
        else:
            val=dic[s[i]]
            dic[s[i]]=val+1
    return dic
def check(d):
    count=0
    for i in d :
        if(d[i]%2!=0):
            count= count+1
        if(count>1):
            return "not palindrome"
    return "palindrome"
d=palindrome("ssuupprraj")
print(check(d))

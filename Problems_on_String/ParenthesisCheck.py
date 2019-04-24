#code
class stack:
    def __init__(self):
        self.__lis=['-1']   
    def push(self,val):
        self.__lis.append(val)
    def pop(self):
        self.__lis.pop()
    def get(self):
        return self.__lis[-1]
    def check(self,one,two):
        if (one=='('and two==')') or (one=='[' and two==']') or (one=='{' and two=='}'):
            return True
        else:
            return False
s='{{{{{{}()}}}}'

l=list(s)
o=stack()
i=0
while len(l)!=0:
    if o.check(o.get(),l[0])==True:
        o.pop()
    else:
        o.push(l[0])
    l.pop(0)
if o.get()=='-1':
    print("balanced")
else:
    print("unbalanced")

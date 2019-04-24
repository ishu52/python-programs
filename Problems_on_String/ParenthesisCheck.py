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


T = int(input())
for _ in range(T):
    l=list(input())
    o=stack()
    while len(l)!=0:
        if (o.get()=='('and l[0]==')') or (o.get()=='[' and l[0]==']') or (o.get()=='{' and l[0]=='}')==True:
            o.pop()
        else:
            o.push(l[0])
        l.pop(0)
    if o.get()=='-1':
        print("balanced")
    else:
        print("not balanced")

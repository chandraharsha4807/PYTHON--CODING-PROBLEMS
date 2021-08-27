class UserMainCode(object):
    @classmethod
    def removeDuplicate(cls, input1):
        t = ""
        for i in input1:
            if(i in t):
                pass
            else:
                t=t+i 
        return (t)


        
s = input()
ob1 = UserMainCode()

print(ob1.removeDuplicate(s))
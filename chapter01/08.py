class cipher:
    def encode(self,s):
        arr=[]
        for s_ in s:
            if(s_ in  alphabet):
                arr.append(219-ord(s_))
            else:
                arr.append(s_)
        return arr
    def decode(self,s):
        arr=[]
        for s_ in s:
            try:
              arr.append(chr(219-int(s_)))
            except:
                arr.append(s_)
        return arr
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
s=list(input())
c=cipher()
d=c.encode(s)
print(d)
print(c.decode(d))

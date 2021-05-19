import random
x="I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind."
y=x.replace(",","").replace(".","").replace(":","").split()


def shuffler(s):
    z=""
    for s in y:
        if(len(s)<=4):
            z+=s+" "
        else:
            head=s[0]
            tail=s[-1]
            arr=list(s[1:-1])
            random.shuffle(arr)
            z+=head+str("".join(arr))+tail+" "
    return z
print(shuffler(y))
        

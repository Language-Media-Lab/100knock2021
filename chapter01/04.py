a="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
a=a.split(" ")
outpt={}
single=[t[0] for t in a[::2]]
double=[t[:2] for t in a[1::2]]
cnt=1
for i in range(len(single)):
    outpt[single[i]]=cnt
    cnt=cnt+1
    outpt[double[i]]=cnt
    cnt=cnt+1

print(outpt)
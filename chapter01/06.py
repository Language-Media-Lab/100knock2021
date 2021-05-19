import _05

a="paraparaparadise"
b="paragraph"

X=set(_05.Ngram(2,a))
Y=set(_05.Ngram(2,b))
print("和",X|Y)
print("積",X&Y)
print("差",X-Y)
print(("s","e") in X)
print(("s","e") in Y)

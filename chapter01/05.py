def Ngram(n,array):
    ans=[]
    for i in range(0,len(array)-1):
        ans.append((array[i],array[i+1]))
    return ans

txt="I am an NLPer"
#単語bigram
print(Ngram(2,txt.split(" ")))
#文字bigram
print(Ngram(2,list(txt.replace(" ",""))))

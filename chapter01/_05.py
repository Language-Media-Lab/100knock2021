def Ngram(n,array):
    ans=[]
    for i in range(0,len(array)-1):
        ans.append((array[i],array[i+1]))
    return ans


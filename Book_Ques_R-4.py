import math
def find_max(l,ind,maxx):                                                                                 #4.1
    if ind==len(l):
        return maxx
    else:
        maxx=max(maxx,l[ind])
        return find_max(l,ind+1,maxx)
    
def find_power(n,p):                                                                                      #4.2
    if p==0:
        return 1
    else:
        partial=find_power(n,p//2)
        result=partial*partial
        if p%2==1:
            result*=n
        return result

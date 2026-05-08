import math

def second_min(l,i=0,c=math.inf,l2=[]):                                                                  #4.8
    l2.append(c)
    if len(l)==0:
        return c
    elif i==len(l):
        return l2[len(l2)-3]
    else:
        c=min(l[i],c)
        return second_min(l,i+1,c,l2)
    
def remainder(m,n):                                                                                      #4.10
    if m>n:
        return n
    else:
        n-=m
        return remainder(m,n)
    
def is_vowel(s):
    if s=="a" or s=="A" or s=="e" or s=="E" or s=="i" or s=="I" or s=="o" or s=="O" or s=="u" or s=="U":
        return True
    
def compare_vowel(s,ind=0,cv=0,cc=0):                                                                    #4.14
    if s==None:
        return "Enter a String"
    elif ind==len(s) and cv>cc:
        return True
    elif ind==len(s) and cc>cv:
        return False
    else:
        if is_vowel(s[ind]):
            cv+=1
        else:
            cc+=1
        return compare_vowel(s,ind+1,cv,cc)
    
def is_odd(n):
    if n%2==1:
        return True     

def arrange_odd_first(i,ind=0,odd="",even=""):                                                           #4.15
    if ind==len(str(i)):
        return int(odd+even)
    else:
        if is_odd(int(str(i)[ind])):
            odd+=str(i)[ind]
        else:
            even+=str(i)[ind]
        return arrange_odd_first(i,ind+1,odd,even)
            
def arrange(n,k,ind=0,small="",large=""):                                                                #4.16
    if ind==len(str(n)):
        return int(small+large)
    else:
        if int(str(n)[ind])<=k:
            small+=str(n)[ind]
        else:
            large+=str(n)[ind]
        return arrange(n,k,ind+1,small,large)
            
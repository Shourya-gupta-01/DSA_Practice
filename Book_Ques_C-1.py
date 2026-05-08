import random

def reverse_list(l):                                                                                   #1.10
    if len(l)==0:
        print("Enter the Elements:")
    else:
        print(l[::-1])
    
def consecutive_even_product(l):                                                                        #1.11
    i=0
    if len(l)>=2:
        while i<len(l)-1:
            if (l[i]*l[i+1])%2==0:
                p=(l[i],l[i+1])
                print(f"The expected consecutive pair is {p}")
            i+=1
        else:
            print(f"No such pair Found")
    else:
        print("Enter atleast 2 Integers")
        
def count_unique(l):                                                                                     #1.12
    c=0
    if len(l)>=1:
        for i in range(len(l)):
            x=l.pop(0)
            if x not in l:
                c+=1
        print(f"There are {c} unique numbers")
    else:
        print("Enter the Elements")
        
def my_shuffle(l):                                                                                       #1.15
    l1=[]
    if len(l)>=2:
        for i in range(len(l)):
            x=random.randint(0,len(l)-1)
            l1.append(l[x])
            y=l.pop(x)
        print(f"The new order is {l1}")
    else:
        print("Enter atleast 2 integers")
        
def dot_product(l1,l2):                                                                                  #1.17
    l3=[]
    if len(l1)==len(l2):
        for i in range(len(l1)):
            c=l1[i]*l2[i]
            l3.append(c)
        print("The dot product of 2 array\n",l3)
    else:
        print("The Array are not of same length")
        
def remove_punc(s):                                                                                      #1.19
    p=[]
    for i in range(33,48):
        p.append(chr(i))
    for i in range(58,65):
        p.append(chr(i))
    for i in range(91,97):
        p.append(chr(i))
    for i in range(123,127):
        p.append(chr(i))
    for i in p:
        if i in s:
            x=s.replace(i,'')
            s=x
    print(s)
    
def norm(v,p=2):                                                                                         #1.22
    v=list(v)
    Euclidean_norm=0
    try:
        if p>=0:
            for i in v:
                Euclidean_norm+=(i**p)
            Euclidean_norm**=(1/p)
        elif p<0:
            print("Power must be positive")
    except:
        print("Vectors and Power must be in integer form")
    if v!=2:
        print(f"{p} norm value of {tuple(v)} is {Euclidean_norm}")
    else:
        print(f"Euclidean norm of {tuple(v)} is {Euclidean_norm}")
             
try:     
    a=eval(input("Enter the vector:"))
    b=int(input("Enter the Power:"))
    norm(a,b)
except:
    print("Vectors and Power must be in integer form")
    
def is_multiple(n,m):                                                                                    #1.1
    try:
        if n%m==0:
            i=1
            while m*i==n:
                i+=1
            print(f"{n} is the multiple of {m}\n\n{m}X{i}={n}")
        else:
            print(f"{n} is not the multiple of {m}")
    except:
        print("Input Error")
        
def is_even(n):                                                                                          #1.2
    i=0
    if n<0:
        while n<i:
            i-=2
            if i==n:
                print(f"{n} is even")
            elif i<n:
                print(f"{n} is odd")
    elif n==0:
        print(f"The number is neither even nor odd")
    else:
        while n>i:
            i+=2
            if i==n:
                print(f"{n} is even")
            elif i>n:
                print(f"{n} is odd") 
                
def minmax(data):                                                                                        #1.3
    if len(data)==0:
        min=None
        max=None
        print(a)
    elif len(data)==1:
        min=data[0]
        max=data[0]
        print(a)
    elif len(data)==2:
        if data[0]>data[1]:
            min=data[1]
            max=data[0]
        elif data[0]<data[1]:
            min=data[0]
            max=data[1]
    else:
        min=data[0]
        max=data[0]
        for i in range(len(data)):
            if min>data[i]:
                min=data[i]
            elif max<data[i]:
                max=data[i]
    a=(min,max)
    print(a)  
    
def sum_even(n):                                                                                         #1.4
    if n<=0:
        print(f"Please enter a positive integer")
    elif n>0:
        i=0
        s=0
        while i<n: 
            if i%2==0:
                s+=(i**2)
            i+=1
        print(f"The expected sum is {s}")
                      
try:    
    a=int(input("Enter the number:"))
    b=int(input("Enter a number:"))
    is_multiple(a,b)
except:
    print(f"Error Found")
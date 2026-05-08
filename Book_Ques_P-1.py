def all_possible(chars,steps=0):                                                                         #1.23
    if steps==len(chars):
        print(''.join(chars))
        return
    for i in range(steps,len(chars)):
        swapped_chars=[c for c in chars]
        swapped_chars[steps],swapped_chars[i]=swapped_chars[i],swapped_chars[steps]
        all_possible(swapped_chars,steps+1)

def compute(n):                                                                                          #1.24
    i=0
    N=n
    if n>2:
        while n>=2:
            n/=2
            i+=1
        print(f"{N} is divided by 2 {i} times")
    else:
        print("integer Must be greater than 2")
    
try:
    a=eval(input("Enter a list of characters:"))
    all_possible(a)
except:
    print("Please enter a list of only characters")
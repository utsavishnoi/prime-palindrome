'''__________________________________________________________PYTHON MINI PROJECT______________________________________________________________'''
'''function to check prime palindrome number'''

def primePalindrome(n):
    ''' prime checking'''
    c=0 #counter for counting number of factors
    for i in range(1,n+1):
        if n%i==0: # checking for factor
            c=c+1
    '''palindrome checking'''
    r=0
    t=n #back up variable
    while t>0:
        d=t%10
        r=r*10+d #making reverse of number
        t//=10
    if c==2 and r==n: # checking if number is both prime and palindrome
        return True
    else:
            return False

n= int(input("Enter the value of n: "))
c=0
i=1

''' finding nth prime palindrome number'''
while True:
    if primePalindrome(i): # prime palindrome checking
        c=c+1
    if c==n: # checking if i is nth prime palindrome number
        print(f"{n}th prime palindrome number is {i}")#printing nth prime palindrome number
        break
    i=i+1

'''____________________________________________________________________ THE END _______________________________________________________________'''




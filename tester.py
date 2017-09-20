
#Palindrome

a=True
while(a==True):
    x=input("input word: ")
    x=x.casefold()
    reversex=reversed(x)

    if (list(x) == list(reversex)):
        print ("True")
    else:
        print ("False")
    k= input("Run again? Yes/No: ").lower()
    if(k =='yes'):
        a=True
    else:
        a=False
print("thankyou")





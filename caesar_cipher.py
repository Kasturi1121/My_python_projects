def cipher(num):
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    res=""
    Type=input("Type 'encrypt' for encryption,type 'decrypt' for decryption:")
    if Type=="encrypt":
        mess=input("Type your message:")
        n=int(input("Type the shift number:"))
        for i in mess:
            if i in alpha:
                x=alpha.index(i)
                e=(x+n)%26
                res+=alpha[e]
            else:
                res+=i
        print("Here is the encrypted result:",res)           
    else:
        mess=input("Type your message:")
        n=int(input("Type the shift number:"))
        for i in mess:
            if i in alpha:
                x=alpha.index(i)
                e=(x-n)%26
                res+=alpha[e]
            else:
                res+=i
            
        print("Here is the decrypted result:",res)
    again=input("Type 'Yes' if you want to go again.Otherwise type 'no'.")
    if again=='YES' or again=='yes':
        cipher(3)
    else:
        print("Goodbye")           
cipher(3)

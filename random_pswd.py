#random password generator
def random_password_generator(strength,letter,symbol,number):
    import random
    pswd=""
    alp=['a','b','c','d','e','f','g','h','i','j','k','l',
         'm','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
         'R','S','T','U','V','W','X','Y','Z']
    sym=['!','@','#','$','%','^','&','*','(',')']
    no=['1','2','3','4','5','6','7','8','9','0']
    for _ in range(letter):
        pswd=pswd+random.choice(alp)
    #print(pswd)
    for _ in range(symbol):
        pswd=pswd+random.choice(sym)

    #for numbers
    for _ in range(number):
        pswd=pswd+random.choice(no)
    #final password is ready
    if strength=="strong":
        password=[]
        for i in pswd:
            password.append(i)
        #print(password)
        random.shuffle(password)
        pswd=""
        for j in range (len(password)):
            pswd=pswd+password[j]
        return pswd
    else:
        return pswd


if __name__=="__main__":
    print("You can generate your password Here!")
    print("how strong you need password(type'strong','weak')")
    strength=input()
    print("enter no of letters you needed")
    letters=int(input())
    print("enter no of symbols you needed")
    symbols=int(input())
    print("enter no of numbers you needed")
    numbers=int(input())
    result=random_password_generator(strength,letters,symbols,numbers)
    print("your genrated is",result)

def factorial(number):
    
    value=1
    if number!=0:
        for i in range(1,number + 1):
            value=value*i
        print( value)
    else:
        print(1)
  
factorial(number=int(input("which number do you want to take the factorial of: ")))
while True:
    soru = input("yine,yeni,yeniden?(e,h)").lower()
    if soru == "e":
        factorial(number=int(input("which number do you want to take the factorial of: ")))
    elif soru == "h" :
        print("yallah ar*bistana")
        exit()
    else:
        print("dümbelek misin evladım yanlış girdin. Az iç!!!")

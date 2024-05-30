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
    question = input("whould you want to try again? (e,h)").lower()
    if question == "e":
        factorial(number=int(input("which number do you want to take the factorial of: ")))
    elif question == "h" :
        print("your process completed. ")
        exit()
    else:
        print("You entered wrong answer, please try again")

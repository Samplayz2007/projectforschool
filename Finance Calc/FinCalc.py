import math
# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# This function calculates the simple intrest
def simple_interest(p, r, t):
    print('Amount: ', p)
    print("Rate of Interest (Per Annum)", r)
    print("Time (In Years): ",t)
    si=(p*r*t)/100
    a= p+si
    print("Final Amount: ", a)
    print("Simple Interest: ", si)

#compound interest
def compound_interest(p,r,t):
    print('Amount: ', p)
    print("Rate of Interest (Per Annum)", r)
    print("Time (In Years): ",t)
    a= p*((1+r/100)**t)
    ci= a-p
    print("Final Amount: ", a)
    print("Compound Interest: ", ci)

# Purchasing power
def pur_power(p,r,t):
    print("Initial Amount: ",p)
    print("Annual Inflation Rate: ",r)
    print("Time in years:", t)
    a= p* ((100/(100+r))**t)
    print("Final amount after",t,"years of inflation: ", a)

#compound annual growth rate
def CAGR(p,a, t ):
    print("Initial value of money: ",p)
    print('Final value of money: ',a)
    print("Time in years: ", t)
    t_inv=1/t
    cagr_rate= (((a/p)**t_inv)  -1)*100
    print("Compound Annual Growth Rate (CAGR): ", cagr_rate)

#monthly EMI calculation
def EMI(p,r,n):
    print("Total Loan Amount: ",p)
    print("Rate of Interest: ",r)
    print("Number of installments: ",n)
    r_mon=  r/(12*100)
    emi = p * r_mon * ((1+r_mon)**n)/((1+r_mon)**n - 1)
    print("EMI for",n,"months: ",emi )

#doubling time calculation
def double(r):
    print("Rate of Interest: ",r)
    t= math.log(2)/math.log(1+ (r/100))
    print("Time taken in years to double money at",r,"percent PA: ", t)

def menu():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("4.Divide")
    print("5.Simple Interest")
    print("6.Compound Interest")
    print("7.Purchasing Power")
    print("8.Compound annual growth rate")
    print("9.Monthly EMI calculation")
    print("10.Doubling time calculation")


while True:
    #menu
    menu()
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):

        if choice == '1':
            num1 = eval(input("Enter first number: "))
            num2 = eval(input("Enter second number: "))
            print(num1, "+", num2, "=", add(num1, num2),sep='')

        elif choice == '2':
            num1 = eval(input("Enter first number: "))
            num2 = eval(input("Enter second number: "))
            print(num1, "-", num2, "=", subtract(num1, num2),sep='')

        elif choice == '3':
            num1 = eval(input("Enter first number: "))
            num2 = eval(input("Enter second number: "))
            print(num1, "X", num2, "=", multiply(num1, num2),sep=' ')

        elif choice == '4':
            num1 = eval(input("Enter first number: "))
            num2 = eval(input("Enter second number: "))
            print(num1, "/", num2, "=", divide(num1, num2),sep='')
        elif choice == '5':
            p=eval(input('Enter The Amount: '))
            r=eval(input('Enter The Rate OF interest: '))
            t=eval(input('Enter The Time (In Years): '))
            print(simple_interest(p, r, t))
        elif choice == '6':
            p=eval(input('Enter The Amount: '))
            r=eval(input('Enter The Rate OF interest: '))
            t=eval(input('Enter The Time (In Years): '))
            print(compound_interest(p, r, t))
        elif choice == '7':
            p=eval(input('Enter The Initial Amount: '))
            r=eval(input('Enter The Rate of Annual Inflation: '))
            t=eval(input('Enter The Time (In Years): '))
            pur_power(p,r,t)
        elif choice == '8':
            p=eval(input('Enter The Initial value of money: '))
            a=eval(input('Enter The Final value of money: '))
            t=eval(input('Enter The Time (In Years): '))
            CAGR(p,a,t )
        elif choice == '9':
            p=eval(input('Enter The Total LOAN Amount: '))
            r=eval(input('Enter The Rate OF Interest: '))
            n=eval(input('Enter The number of installments: '))
            EMI(p,r, n)
        elif choice == '10':
            r=eval(input("Enter The Rate of Interest: "))
            double(r)


        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
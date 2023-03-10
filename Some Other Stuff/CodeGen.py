#Importing Required Modules
import random
import string
Lmao=True
while Lmao:  #Main Loop
    #Menu
    idk=int(input("""
    **********************************************************
    *                                                        *
    *  Choose if your code should be alphabetic,numeric or   *
    *  Symbots                                               *
    *                                                        *
    *   1.Alphabets                                          *
    *   2.Numeric                                            *
    *   3.Mixed                                              *
    *   4.Exit                                               *
    *                                                        *
    **********************************************************
    Enter Your Choice:"""))
    #Generate Alphabetic Code
    if idk==1:
        max_length = int(input("Enter The Maximum Length of your Alphabetic Code:")) #Get The Maximum Size OF the code
        str1 = "" #Create a string
        for i in range(random.randint(1, max_length)): #For Loop for making the Loop
            str1 += random.choice(string.ascii_letters) #Constructing the Code
        print("The Generated Code is:",str1) #Print the Generated Code
    #Generate Numeric Code
    elif idk==2:
        max_length = int(input("Enter The Maximum Length of your Alphabetic Code:")) #Get The Maximum Size OF the code
        str1 = "" #Create a string
        for i in range(random.randint(1, max_length)): #For Loop for making the Loop
            str1 += random.choice(string.digits) #Constructing the Code
        print("The Generated Code is:",str1) #Print the Generated Code
    #Generate Mixed Code
    elif idk==3:
        max_length = int(input("Enter The Maximum Length of your Alphabetic Code:")) #Get The Maximum Size OF the code
        str1 = "" #Create a string
        for i in range(random.randint(1, max_length)): #For Loop for making the Loop
            str1 += random.choice(string.ascii_uppercase + string.digits) #Constructing the Code
        print("The Generated Code is:",str1) #Print the Generated Code
    #Exit Loop
    elif idk==4:
        print("Exiting...")
        Lmao=False #break loop
    #Check if loop is Invalid
    else:
        print("Invalid Choice")

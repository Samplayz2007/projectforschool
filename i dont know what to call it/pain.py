

def explain_variables():
    # Variables
    print("In Python, variables are used to store values. You can assign a value to a variable using the = operator. For example:")
    print("x = 5")
    print("y = 'Hello, world!'")
    print("print(x)")
    print("print(y)")
    print("This will output 5 and 'Hello, world!' respectively.")

def explain_arithmetic_operators():
    # Arithmetic operators
    print("In Python, you can use arithmetic operators to perform mathematical operations. The following arithmetic operators are available in Python:")
    print("+ (addition)")
    print("- (subtraction)")
    print("* (multiplication)")
    print("/ (division)")
    print("% (modulo)")
    print("For example:")
    print("a = 10")
    print("b = 3")
    print("print(a + b)") # Addition
    print("print(a - b)") # Subtraction
    print("print(a * b)") # Multiplication
    print("print(a / b)") # Division
    print("print(a % b)") # Modulo

def explain_strings():
    # Strings
    print("In Python, strings are used to represent text. You can create a string by enclosing text in quotes. For example:")
    print("name = 'John'")
    print("print('My name is ' + name)")
    print("This will output 'My name is John'.")

def explain_lists():
    # Lists
    print("In Python, lists are used to store multiple items in a single variable. You can create a list by enclosing items in square brackets, separated by commas. For example:")
    print("my_list = ['apple', 'banana', 'cherry']")
    print("print(my_list)")
    print("print(my_list[1])") # Accessing an item in the list
    print("my_list.append('orange')") # Adding an item to the list
    print("print(my_list)")

def explain_functions():
    # Functions
    print("In Python, functions are used to perform specific tasks. You can define a function using the def keyword, followed by the function name and any parameters. For example:")
    print("def greet(name):")
    print("print('Hello, ' + name)")
    print("greet('John')") # Calling the function with an argument
    print("This will output 'Hello, John'.")
def explain_if_statements():
    # If statements
    print("In Python, you can use if statements to execute code if a certain condition is true. For example:")
    print("x = 5")
    print("if x > 0:")
    print("    print('x is positive')")
    print("This will output 'x is positive' since the condition x > 0 is true.")

    print("You can also use else statements to execute code if the condition is false. For example:")
    print("x = -2")
    print("if x > 0:")
    print("    print('x is positive')")
    print("else:")
    print("    print('x is negative')")
    print("This will output 'x is negative' since the condition x > 0 is false.")

    print("You can also use elif statements to check multiple conditions. For example:")
    print("x = 0")
    print("if x > 0:")
    print("    print('x is positive')")
    print("elif x == 0:")
    print("    print('x is zero')")
    print("else:")
    print("    print('x is negative')")
    print("This will output 'x is zero' since the condition x == 0 is true.")

def explain_loops():
    # Loops
    print("In Python, you can use loops to repeat a set of statements a certain number of times or until a certain condition is met. There are two types of loops: for loops and while loops. For example:")
    print("for i in range(5):")
    print("    print(i)")
    print("This will output the numbers 0 to 4.")

    print("You can also use while loops to repeat statements until a certain condition is met. For example:")
    print("i = 0")
    print("while i < 5:")
    print("    print(i)")
    print("    i += 1")
    print("This will also output the numbers 0 to 4.")

def explain_classes():
    # Classes
    print("In Python, you can use classes to define your own custom types. A class can have attributes and methods. For example:")
    print("class Person:")
    print("    def __init__(self, name, age):")
    print("        self.name = name")
    print("        self.age = age")
    print("")
    print("    def greet(self):")
    print("        print('Hello, my name is ' + self.name + ' and I am ' + str(self.age) + ' years old.')")
    print("")
    print("# Create a Person object")
    print("person = Person('Alice', 25)")
    print("")
    print("# Call the greet method")
    print("person.greet()")
    print("This will output 'Hello, my name is Alice and I am 25 years old.'")

def explain_importing_modules():
    # Importing modules
    print("In Python, you can use modules to organize your code into separate files. You can import a module using the import keyword. For example:")
    print("import math")
    print("# Use the sqrt function from the math module")
    print("x = math.sqrt(25)")
    print("This will assign the value 5 to the variable x.")

def explain_basic_modules():
    # Basic modules
    print("Python comes with many built-in modules that you can use to perform common tasks. Some of the basic modules include:")
    print("- math: for mathematical functions")
    print("- random: for generating random numbers")
    print("- datetime: for working with dates and times")
    print("- os: for interacting with the operating system")
    print("- sys: for interacting with the Python interpreter")
    print("- math: Provides functions for mathematical operations.")
    print("- random: Generates random numbers and other random data.")
    print("- datetime: Provides classes for working with dates and times.")
    print("- os: Provides a way to interact with the operating system.")
    print("- sys: Provides information about the Python interpreter.")
    print("- csv: Provides classes for reading and writing CSV files.")
    print("- json: Provides functions for working with JSON data.")
    print("- re: Provides support for regular expressions.")
    print("Would you like to learn more about a specific module? Or do u want to learn about everything? (y/n):")
    choice = input()
    if choice.lower() == "y":
        def explain_math():
            print("The math module provides many useful mathematical functions, such as:")
            print("- sqrt(x): Returns the square root of x.")
            print("- pow(x, y): Returns x raised to the power of y.")
            print("- sin(x): Returns the sine of x (x is in radians).")
            print("- cos(x): Returns the cosine of x (x is in radians).")
            print("- tan(x): Returns the tangent of x (x is in radians).")
            print("- pi: Returns the mathematical constant pi (3.14159...).")
        def explain_random():
            print("The random module provides functions for generating random data, such as:")
            print("- random(): Returns a random float between 0 and 1.")
            print("- randint(a, b): Returns a random integer between a and b (inclusive).")
            print("- choice(seq): Returns a random element from the given sequence.")
            print("- shuffle(seq): Shuffles the elements of the given sequence in place.")
        def explain_datetime():
            print("The datetime module provides classes for working with dates and times, such as:")
            print("- datetime.date(year, month, day): Returns a date object representing the given year, month, and day.")
            print("- datetime.time(hour=0, minute=0, second=0, microsecond=0): Returns a time object representing the given time.")
            print("- datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0): Returns a datetime object representing the given date and time.")
            print("- datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0): Represents a duration of time.")
        def explain_os():
            print("The os module provides a way to interact with the operating system, such as:")
            print("- os.getcwd(): Returns the current working directory.")
            print("- os.listdir(path='.'): Returns a list of files and directories in the given path.")
            print("- os.path.exists(path): Returns True if the given path exists.")
            print("- os.makedirs(name, mode=0o777, exist_ok=False): Creates a new directory with the given name.")
        def explain_sys():
            print("The sys module provides information about the Python interpreter, such as:")
            print("- sys.argv: A list of command-line arguments passed to the Python script.")
            print("- sys.path: A list of directories where Python modules can be found.")
            print("- sys.version: The version of Python currently running.")
        def explain_sys():
            print("The sys module provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter.")
            print("Here are a few examples of what you can do with the sys module:")
            print("- Get the version of Python currently running: sys.version")
            print("- Get the system path: sys.path")
            print("- Get the command line arguments passed to the script: sys.argv")

        def explain_csv():
            print("The csv module provides classes for working with comma-separated values (CSV) files.")
            print("Here are a few examples of what you can do with the csv module:")
            print("- Read a CSV file: csv.reader(file)")
            print("- Write to a CSV file: csv.writer(file)")
            print("- Use a custom delimiter: csv.reader(file, delimiter='|')")

        def explain_json():
            print("The json module provides functions for working with JavaScript Object Notation (JSON) data.")
            print("Here are a few examples of what you can do with the json module:")
            print("- Encode a Python object into JSON format: json.dumps(obj)")
            print("- Decode a JSON string into a Python object: json.loads(str)")
            print("- Print JSON data in a more human-readable format:")
            print("    json.dumps(obj, indent=4)")

            # example JSON data
            example_data = {"name": "John", "age": 30, "city": "New York"}

            # encode to JSON format and pretty print
            encoded_data = json.dumps(example_data, indent=4)
            print("\nHere's an example of encoding and pretty printing JSON data:")
            print(encoded_data)

        def explain_re():
            print("The re module provides support for regular expressions.")
            print("Here are a few examples of what you can do with the re module:")
            print("- Search for a pattern in a string: re.search(pattern, string)")
            print("- Replace a pattern in a string: re.sub(pattern, replacement, string)")
            print("- Split a string using a pattern as the delimiter: re.split(pattern, string)")
        yay=True
        while yay:
                print('Enter The name of module u want to learn about:')
                module=input()
                if module.lower() == "random":
                    explain_random()
                    print('Do u want to learn about any other module?:')
                    damn=input()
                    if damn.lower=='y' or damn.lower=='yes':
                        continue
                    elif damn.lower=='n' or damn.lower == 'no':
                        yay=False
        
                elif module.lower == "math" or "maths":
                    explain_math()
                    print('Do u want to learn about any other module?:')
                    damn=input()
                    if damn.lower=='y' or damn.lower=='yes':
                        continue
                    elif damn.lower=='n' or damn.lower == 'no':
                        yay=False

                elif module.lower() == "datetime":
                    explain_datetime()
                    print('Do u want to learn about any other module?:')
                    damn=input()
                    if damn.lower=='y' or damn.lower=='yes':
                        continue
                    elif damn.lower=='n' or damn.lower == 'no':
                        yay=False

                elif module.lower() == "os":
                    explain_os()
                    print('Do u want to learn about any other module?:')
                    damn=input()
                    if damn.lower=='y' or damn.lower=='yes':
                        continue
                    elif damn.lower=='n' or damn.lower == 'no':
                        yay=False

                elif module.lower() == "sys":
                    explain_sys()
                    print('Do u want to learn about any other module?:')
                    damn=input()
                    if damn.lower=='y' or damn.lower=='yes':
                        continue
                    elif damn.lower=='n' or damn.lower == 'no':
                        yay=False

                elif module.lower() == "csv":
                    explain_csv()
                    print('Do u want to learn about any other module?:')
                    damn=input()
                    if damn.lower=='y' or damn.lower=='yes':
                        continue
                    elif damn.lower=='n' or damn.lower == 'no':
                        yay=False

                elif module.lower() == "json":
                    explain_json()
                    print('Do u want to learn about any other module?:')
                    damn=input()
                    if damn.lower=='y' or damn.lower=='yes':
                        continue
                    elif damn.lower=='n' or damn.lower == 'no':
                        yay=False

                elif module.lower() == "re":
                    explain_re()
                    print('Do u want to learn about any other module?:')
                    damn=input()
                    if damn.lower=='y' or damn.lower=='yes':
                        continue
                    elif damn.lower=='n' or damn.lower == 'no':
                        yay=False


                else:
                    print(f"Sorry, the {module} module is not included in this basic module tutorial.")
    elif choice.lower == "n":
        print("Alright I Will explain All the modules")
        explain_math()
        explain_random()
        explain_datetime()
        explain_os()
        explain_sys()
        explain_csv()
        explain_json
        explain_re()
    else:
        print("Okay, moving on to the next topic!")

def explain_error_handling():
    # Error handling
    print("In Python, error handling is used to catch and handle exceptions that might occur in your code. You can use the try-except block to catch an exception and handle it gracefully. For example:")
    print("try:")
    print("    x = 1 / 0 # This will raise a ZeroDivisionError") 
    print("except ZeroDivisionError:")
    print("    print('Cannot divide by zero.')")
    print("This will output 'Cannot divide by zero.'.")
def main():
    # Ask user what they want to learn about
    while True:
        # Ask the user what they want to learn about
        print("Welcome to the Python basics tutorial. What would you like to learn about?")
        print("1. Variables")
        print("2. If statements")
        print("3. Loops")
        print("4. Functions")
        print("5. Classes")
        print("6. Importing modules")
        print("7. Basic modules")
        print("8. Error handling")
        print("9. Everything")
        print("10. Exit")
        print("Enter a number (1-10):")
        choice = input()

        # Call the appropriate function based on the user's choice
        if choice == "1":
            explain_variables()
        elif choice == "2":
            explain_if_statements()
        elif choice == "3":
            explain_loops()
        elif choice == "4":
            explain_functions()
        elif choice == "5":
            explain_classes()
        elif choice == "6":
            explain_importing_modules()
        elif choice == "7":
            damn = True
            while damn:
                explain_basic_modules()
                print('Do u want to learn about any other module? (y/n)')
                wellll=input()
                if wellll.lower == "n":
                    damn = False
                else:
                    damn=True
        elif choice == "8":
            explain_error_handling()
        elif choice == "9":
            explain_variables()
            explain_functions()
            explain_if_statements()
            explain_loops()
            explain_classes()
            explain_importing_modules()
            damn = True
            while damn:
                explain_basic_modules()
                print('Do u want to learn about any other module? (y/n)')
                wellll=input()
                if wellll.lower == "n":
                    damn = False
                else:
                    damn=True
            explain_error_handling()
        elif choice == "10":
            print("Come back again when u want to learn something about Python")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")
main()  
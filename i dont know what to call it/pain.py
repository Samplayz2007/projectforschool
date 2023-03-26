from time import sleep
def typeit(words):
    for char in words:
        sleep(0.04)
        print(char, end='', flush=True)
    print()



def explain_variables():
    # Variables
    typeit("In Python, variables are used to store values. You can assign a value to a variable using the = operator. For example:")
    typeit("x = 5")
    typeit("y = 'Hello, world!'")
    typeit("print(x)")
    typeit("print(y)")
    typeit("This will output 5 and 'Hello, world!' respectively.")

def explain_arithmetic_operators():
    # Arithmetic operators
    typeit("In Python, you can use arithmetic operators to perform mathematical operations. The following arithmetic operators are available in Python:")
    typeit("+ (addition)")
    typeit("- (subtraction)")
    typeit("* (multiplication)")
    typeit("/ (division)")
    typeit("% (modulo)")
    typeit("For example:")
    typeit("a = 10")
    typeit("b = 3")
    typeit("print(a + b)") # Addition
    typeit("print(a - b)") # Subtraction
    typeit("print(a * b)") # Multiplication
    typeit("print(a / b)") # Division
    typeit("print(a % b)") # Modulo

def explain_strings():
    # Strings
    typeit("In Python, strings are used to represent text. You can create a string by enclosing text in quotes. For example:")
    typeit("name = 'John'")
    typeit("print('My name is ' + name)")
    typeit("This will output 'My name is John'.")

def explain_lists():
    # Lists
    typeit("In Python, lists are used to store multiple items in a single variable. You can create a list by enclosing items in square brackets, separated by commas. For example:")
    typeit("my_list = ['apple', 'banana', 'cherry']")
    typeit("print(my_list)")
    typeit("print(my_list[1])") # Accessing an item in the list
    typeit("my_list.append('orange')") # Adding an item to the list
    typeit("print(my_list)")

def explain_functions():
    # Functions
    typeit("In Python, functions are used to perform specific tasks. You can define a function using the def keyword, followed by the function name and any parameters. For example:")
    typeit("def greet(name):")
    typeit("print('Hello, ' + name)")
    typeit("greet('John')") # Calling the function with an argument
    typeit("This will output 'Hello, John'.")
def explain_if_statements():
    # If statements
    typeit("In Python, you can use if statements to execute code if a certain condition is true. For example:")
    typeit("x = 5")
    typeit("if x > 0:")
    typeit("    print('x is positive')")
    typeit("This will output 'x is positive' since the condition x > 0 is true.")

    typeit("You can also use else statements to execute code if the condition is false. For example:")
    typeit("x = -2")
    typeit("if x > 0:")
    typeit("    print('x is positive')")
    typeit("else:")
    typeit("    print('x is negative')")
    typeit("This will output 'x is negative' since the condition x > 0 is false.")

    typeit("You can also use elif statements to check multiple conditions. For example:")
    typeit("x = 0")
    typeit("if x > 0:")
    typeit("    print('x is positive')")
    typeit("elif x == 0:")
    typeit("    print('x is zero')")
    typeit("else:")
    typeit("    print('x is negative')")
    typeit("This will output 'x is zero' since the condition x == 0 is true.")

def explain_loops():
    # Loops
    typeit("In Python, you can use loops to repeat a set of statements a certain number of times or until a certain condition is met. There are two types of loops: for loops and while loops. For example:")
    typeit("for i in range(5):")
    typeit("    print(i)")
    typeit("This will output the numbers 0 to 4.")

    typeit("You can also use while loops to repeat statements until a certain condition is met. For example:")
    typeit("i = 0")
    typeit("while i < 5:")
    typeit("    print(i)")
    typeit("    i += 1")
    typeit("This will also output the numbers 0 to 4.")

def explain_classes():
    # Classes
    typeit("In Python, you can use classes to define your own custom types. A class can have attributes and methods. For example:")
    typeit("class Person:")
    typeit("    def __init__(self, name, age):")
    typeit("        self.name = name")
    typeit("        self.age = age")
    typeit("")
    typeit("    def greet(self):")
    typeit("        print('Hello, my name is ' + self.name + ' and I am ' + str(self.age) + ' years old.')")
    typeit("")
    typeit("# Create a Person object")
    typeit("person = Person('Alice', 25)")
    typeit("")
    typeit("# Call the greet method")
    typeit("person.greet()")
    typeit("This will output 'Hello, my name is Alice and I am 25 years old.'")

def explain_importing_modules():
    # Importing modules
    typeit("In Python, you can use modules to organize your code into separate files. You can import a module using the import keyword. For example:")
    typeit("import math")
    typeit("# Use the sqrt function from the math module")
    typeit("x = math.sqrt(25)")
    typeit("This will assign the value 5 to the variable x.")

def explain_basic_modules():
    # Basic modules
    typeit("Python comes with many built-in modules that you can use to perform common tasks. Some of the basic modules include:")
    typeit("- math: for mathematical functions")
    print("- random: for generating random numbers")
    typeit("- datetime: for working with dates and times")
    typeit("- os: for interacting with the operating system")
    typeit("- sys: for interacting with the Python interpreter")
    typeit("- math: Provides functions for mathematical operations.")
    typeit("- random: Generates random numbers and other random data.")
    typeit("- datetime: Provides classes for working with dates and times.")
    typeit("- os: Provides a way to interact with the operating system.")
    typeit("- sys: Provides information about the Python interpreter.")
    typeit("- csv: Provides classes for reading and writing CSV files.")
    typeit("- json: Provides functions for working with JSON data.")
    typeit("- re: Provides support for regular expressions.")
    typeit("Would you like to learn more about a specific module? Or do u want to learn about everything? (y/n):")
    choice = input()
    if choice.lower() == "y":
        def explain_math():
            typeit("The math module provides many useful mathematical functions, such as:")
            typeit("- sqrt(x): Returns the square root of x.")
            typeit("- pow(x, y): Returns x raised to the power of y.")
            typeit("- sin(x): Returns the sine of x (x is in radians).")
            typeit("- cos(x): Returns the cosine of x (x is in radians).")
            typeit("- tan(x): Returns the tangent of x (x is in radians).")
            typeit("- pi: Returns the mathematical constant pi (3.14159...).")
        def explain_random():
            typeit("The random module provides functions for generating random data, such as:")
            typeit("- random(): Returns a random float between 0 and 1.")
            typeit("- randint(a, b): Returns a random integer between a and b (inclusive).")
            typeit("- choice(seq): Returns a random element from the given sequence.")
            typeit("- shuffle(seq): Shuffles the elements of the given sequence in place.")
        def explain_datetime():
            typeit("The datetime module provides classes for working with dates and times, such as:")
            typeit("- datetime.date(year, month, day): Returns a date object representing the given year, month, and day.")
            typeit("- datetime.time(hour=0, minute=0, second=0, microsecond=0): Returns a time object representing the given time.")
            typeit("- datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0): Returns a datetime object representing the given date and time.")
            typeit("- datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0): Represents a duration of time.")
        def explain_os():
            typeit("The os module provides a way to interact with the operating system, such as:")
            typeit("- os.getcwd(): Returns the current working directory.")
            typeit("- os.listdir(path='.'): Returns a list of files and directories in the given path.")
            typeit("- os.path.exists(path): Returns True if the given path exists.")
            typeit("- os.makedirs(name, mode=0o777, exist_ok=False): Creates a new directory with the given name.")
        def explain_sys():
            typeit("The sys module provides information about the Python interpreter, such as:")
            typeit("- sys.argv: A list of command-line arguments passed to the Python script.")
            typeit("- sys.path: A list of directories where Python modules can be found.")
            typeit("- sys.version: The version of Python currently running.")
        def explain_sys():
            typeit("The sys module provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter.")
            typeit("Here are a few examples of what you can do with the sys module:")
            typeit("- Get the version of Python currently running: sys.version")
            typeit("- Get the system path: sys.path")
            typeit("- Get the command line arguments passed to the script: sys.argv")

        def explain_csv():
            typeit("The csv module provides classes for working with comma-separated values (CSV) files.")
            typeit("Here are a few examples of what you can do with the csv module:")
            typeit("- Read a CSV file: csv.reader(file)")
            typeit("- Write to a CSV file: csv.writer(file)")
            typeit("- Use a custom delimiter: csv.reader(file, delimiter='|')")

        def explain_json():
            typeit("The json module provides functions for working with JavaScript Object Notation (JSON) data.")
            typeit("Here are a few examples of what you can do with the json module:")
            typeit("- Encode a Python object into JSON format: json.dumps(obj)")
            typeit("- Decode a JSON string into a Python object: json.loads(str)")
            typeit("- Print JSON data in a more human-readable format:")
            typeit("    json.dumps(obj, indent=4)")

            # example JSON data
            example_data = {"name": "John", "age": 30, "city": "New York"}

            # encode to JSON format and pretty print
            encoded_data = json.dumps(example_data, indent=4)
            typeit("\nHere's an example of encoding and pretty printing JSON data:")
            typeit(encoded_data)

        def explain_re():
            typeit("The re module provides support for regular expressions.")
            typeit("Here are a few examples of what you can do with the re module:")
            typeit("- Search for a pattern in a string: re.search(pattern, string)")
            typeit("- Replace a pattern in a string: re.sub(pattern, replacement, string)")
            typeit("- Split a string using a pattern as the delimiter: re.split(pattern, string)")
        while True:
                typeit('Enter The name of module u want to learn about:')
                module=input()
                if module.lower() == "random":
                    explain_random()
                    typeit('Do u want to learn about any other module?:')
                    damn=input()
                    if damn.lower=='y' or damn.lower=='yes':
                        continue
                    elif damn.lower=='n' or damn.lower == 'no':
                        break
        
                elif module.lower == "math" or "maths":
                    explain_math()
                    typeit('Do u want to learn about any other module?:')
                    damn=input()
                    if damn.lower=='y' or damn.lower=='yes':
                        continue
                    elif damn.lower=='n' or damn.lower == 'no':
                        break

                elif module.lower() == "datetime":
                    explain_datetime()
                    typeit('Do u want to learn about any other module?:')
                    damn=input()
                    if damn.lower=='y' or damn.lower=='yes':
                        continue
                    elif damn.lower=='n' or damn.lower == 'no':
                        break

                elif module.lower() == "os":
                    explain_os()
                    typeit('Do u want to learn about any other module?:')
                    damn=input()
                    if damn.lower=='y' or damn.lower=='yes':
                        continue
                    elif damn.lower=='n' or damn.lower == 'no':
                        break

                elif module.lower() == "sys":
                    explain_sys()
                    typeit('Do u want to learn about any other module?:')
                    damn=input()
                    if damn.lower=='y' or damn.lower=='yes':
                        continue
                    elif damn.lower=='n' or damn.lower == 'no':
                        break

                elif module.lower() == "csv":
                    explain_csv()
                    typeit('Do u want to learn about any other module?:')
                    damn=input()
                    if damn.lower=='y' or damn.lower=='yes':
                        continue
                    elif damn.lower=='n' or damn.lower == 'no':
                        break

                elif module.lower() == "json":
                    explain_json()
                    typeit('Do u want to learn about any other module?:')
                    damn=input()
                    if damn.lower=='y' or damn.lower=='yes':
                        continue
                    elif damn.lower=='n' or damn.lower == 'no':
                        break

                elif module.lower() == "re":
                    explain_re()
                    typeit('Do u want to learn about any other module?:')
                    damn=input()
                    if damn.lower=='y' or damn.lower=='yes':
                        continue
                    elif damn.lower=='n' or damn.lower == 'no':
                        break


                else:
                    print(f"Sorry, the {module} module is not included in this basic module tutorial.")
    elif choice.lower == "n":
        typeit("Alright I Will explain All the modules")
        explain_math()
        explain_random()
        explain_datetime()
        explain_os()
        explain_sys()
        explain_csv()
        explain_json
        explain_re()
    else:
        typeit("Okay, moving on to the next topic!")

def explain_error_handling():
    # Error handling
    typeit("In Python, error handling is used to catch and handle exceptions that might occur in your code. You can use the try-except block to catch an exception and handle it gracefully. For example:")
    typeit("try:")
    typeit("    x = 1 / 0 # This will raise a ZeroDivisionError") 
    typeit("except ZeroDivisionError:")
    typeit("    print('Cannot divide by zero.')")
    typeit("This will output 'Cannot divide by zero.'.")
def main():
    # Ask user what they want to learn about
    while True:
        # Ask the user what they want to learn about
        typeit("Welcome to the Python basics tutorial. What would you like to learn about?")
        typeit("1. Variables")
        typeit("2. If statements")
        typeit("3. Loops")
        typeit("4. Functions")
        typeit("5. Classes")
        typeit("6. Importing modules")
        typeit("7. Basic modules")
        typeit("8. Error handling")
        typeit("9. Everything")
        typeit("10. Exit")
        typeit("Enter a number (1-10):")
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
                typeit('Do u want to learn about any other module? (y/n)')
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
                typeit('Do u want to learn about any other module? (y/n)')
                wellll=input()
                if wellll.lower == "n":
                    damn = False
                else:
                    damn=True
            explain_error_handling()
        elif choice == "10":
            typeit("Come back again when u want to learn something about Python")
            break
        else:
            typeit("Invalid choice. Please enter a number from 1 to 8.")
main()  
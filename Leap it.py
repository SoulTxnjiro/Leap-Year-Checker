print("Welcome to Leap It. Here you can find a year was, is or will be leap")
while True:
    # Taking Input
    a = input("Please type in a year \n")
    try:
        # making the input an integer
        a = int(a)
        # if input divide by 4 gives 0 or input divide by 400 gives 0 it will work
        if a%4 == 0 or a%400 == 0:
            print("It is a Leap Year!!")
        else:
            print("It is not a Leap Year")
    except Exception as e:
        print("Write Correct Year")

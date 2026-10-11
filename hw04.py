# ------------------------------------------------------
#        Name: Annie Lischer
#       Peers: N/A
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ The func asks for an input then checks to see if
        secret_word, "dog", or "Dog" is a part of the input.
        If it is it checks to see which it is and responds
        accordingly before changing the varible cont to false
        which ends the while loop. If they are not present the
        func prints "Try again" and the while loop continues.
        
        cont is a boolean used to control the while loop
        guess is a str inputted by the user """
    
    #This varible acts as a switch for the while loop (cont is short for continue)f
    cont=True
    
    #run until the cont "switch" is flipped
    while cont == True:      
        #asks for input, taken as a str
        guess = input("Give me a sentence: ")        
        #do the following code if what we are looking for is found
        if secret_word in guess or "dog" in guess or "Dog" in guess:            
            #if secret_word is present, inform user and "flip the switch" of the while loop
            if secret_word in guess:
                print("You used the secret word!")
                cont = False           
            #if "dog" or "Dog" is present, inform user and "flip the switch" of the while loop
            if "dog" in guess or "Dog" in guess:
                print("You used the word \"dog\" or the word \"Dog\"!")
                cont = False        
        #if there is nothing to be found, print "Try again" and return to looping
        else:
            print("Try again")

# Task 2
def check_greater():
    """ The func takes in two ints and checks to see
        if they are equal. If they are it loops and
        continues to ask for numbers. If they are not
        it compares them and informs the user which
        is greater
        
        cont is a boolean used to control the while loop
        num1 is an int given by the user
        num2 is an int give by the user"""
    
    #The switch for the while loop
    cont = True
    
    #runs while "switched on"
    while cont == True:       
        #asks for user input
        num1=int(input("Give me a number: "))
        num2=int(input("Give me another: "))        
        #checks to see if nums are equal
        if num1 != num2:
            #if num1>num2 informs user of such and switches flip "off"
            if num1>num2:
                print("First is Greater")
                cont = False
            #if num2>num1 informs user of such and switches flip "off"
            if num2>num1:
                print("Second is Greater")
                cont = False
        #loop continues if nums are equal
        else:
            print("Try again")


# Task 3
def get_special_numbers():
    """ Add your docstring """
    
    for num in range(1,41):
        if num%2 != 0 and num%3 == 0 and num%5 != 0:
            print(num)
    
    pass


# Task 4.a
def my_for_loop():
    """ Add your docstring """
    pass

# Task 4.b
def my_while_loop():
    """ Add your docstring """
    pass

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")

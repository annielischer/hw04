# ------------------------------------------------------
#        Name: Annie Lischer
#       Peers: N/A
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ cont is a boolean used to control the while loop
        guess is a str inputted by the user
        
        The func asks for an input then checks to see if
        secret_word, "dog", or "Dog" is a part of the input.
        If it is it checks to see which it is and responds
        accordingly before changing the varible cont to false
        which ends the while loop. If they are not present the
        func prints "Try again" and the while loop continues. """
    
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
    """ Add your docstring """
    pass



# Task 3
def get_special_numbers():
    """ Add your docstring """
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

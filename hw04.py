# ------------------------------------------------------
#        Name: Annie Lischer
#       Peers: N/A
#  References: Python Docs to figure out sys.exit() [I forgot the parathesis]
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
    
    #This varible acts as a switch for the while loop (cont is short for continue)
    cont=True
    
    #run until the cont "switch" is flipped
    while cont == True:      
        guess = input("Give me a sentence: ")
        
        #do the following code if what we are looking for is found
        if secret_word in guess or "dog" in guess or "Dog" in guess:            
            
            #print relevant output
            if secret_word in guess:
                print("You used the secret word!")
                #"flip switch" to end while loop
                cont = False           
            
            #print relevant output
            if "dog" in guess or "Dog" in guess:
                print("You used the word \"dog\" or the word \"Dog\"!")
                #"flip switch" to end while loop
                cont = False        

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

        num1=int(input("Give me a number: "))
        num2=int(input("Give me another: "))        
        
        #checks to see if nums are equal
        if num1 != num2:
 
            if num1>num2:
                print("First is Greater")
                #"switches off" while loop
                cont = False

            if num2>num1:
                print("Second is Greater")
                #"switches off" while loop
                cont = False

        else:
            print("Try again")


# Task 3
def get_special_numbers():
    """ The func prints number between 1 and 40 (inclusive)
        if it is odd, a multiple of 3 and not a multiple of 5 """
    
    #runs 40 times
    for num in range(1,41):
        #runs if the number is odd, a multiple of 3 and not a multiple of 5
        if num%2 != 0 and num%3 == 0 and num%5 != 0:
            print(num)

# Task 4.a
def my_for_loop():
    """ The func takes in a 2-5 long str with no spaces
        then goes letter by letter and tells the user if it
        is a vowel or a consonant
        
        word is a str inputted by the user
        vowels is a list with all the vowels for checking purposes
        """
    #defining our important variables
    word = input("Give me a word between 2-5 letters long: ")
    vowels = ["a","e","i","o","u","y","A","E","I","O","U","Y"]
    
    #does nothing if str is too long or too short
    if len(word)<2 or len(word)>5:
        print("bad word")
        return
    #does nothing if str has a space
    elif " " in word:
        print("bad word")
        return
    else:
        #goes letter by letter to check if its a vowel and prints the correct output
        for let in range(len(word)):
            if word[let] in vowels:
                print(f"{word[let]} is a vowel")
            else:
                print(f"{word[let]} is a consonant")

# Task 4.b
def my_while_loop():
    """ The func loops indefinately until
        either b or c is choosen.
        
        query is a string inputted by the user"""

    while True:
        query = input("Choose a, b, or c: ")
        if query == "a":
            continue
        #breaks out of the while loop (and thus the func)
        elif query == "b":
            print("Goodbye")
            break
        #stops the code entirely
        elif query == "c":
            sys.exit()
        else:
            print("try again")
            continue


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

# - [X] you added your name to the top comments of the python file
# - [X] runs without syntax errors (or -50%)
# - [X] adds a few small but informative comments (or -5%)
# - [X] adds docstrings to each function (or -5%)
# - [X] Passes all tests (or lose points per missed test). If you do not pass all tests, do not check this box
# - [X] You checked the correct boxes

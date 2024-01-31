#Global currency value which ends the game if you reach 0
currency = 1000

#In Progress variable which helps change the words
inprogress = False

#Import randint from random (only needs randint from the module)
from random import randint
from time import sleep

#Ask to start the game
def ask(starter, bet):
    global currency
    #Globally call the inprogress variable
    global inprogress
    
    #Declare words
    words = None
    
    
    if not inprogress:
        words = "\nYou start with "
        inprogress = True
    else:
        words = "\nCurrent face values are "
    
    hand = input(words + str(starter) + ". Would you like to hit, stand, double down, or surrender? \n").lower()
        
    if hand == "hit":
        hit(starter, bet)
            
    elif hand == "stand":
        win = dealerlogic(starter)
        
        if win:
            currency += bet
            print("\nYou win, " + str(bet) + " has been added to your currency. \nCurrent Currency: " + str(currency)  + "\n")
            game()
        else:
            currency -= bet
            print("\nYou lost! " + str(bet) + " has been removed from your currency. \nCurrent Currency: " + str(currency) + "\n")
            game()
            
    elif hand == "double down":
        doubledown(starter, bet)
            
    elif hand == "surrender":
        surrender(bet)
        
    else:
        print("Incorrect response.")
        ask(starter, bet)

#Dealer's logic and Desicion making
def dealerlogic(starter):
    global currency
    dv = 0
    print("")
    
    while dv < 18:
        dd = randint(1, 10)
        
        dv += dd
        print("Dealer drew a " + str(dd) + ". Current face values: " + str(dv) + ".")
        sleep(1)
    
    if dv > 21:
        return True
    
    if dv == starter:
        print("\nYou both tied! Nobody loses anything!")
        game()
    else:
        return (dv < starter)
     

#Hit logic
def hit(starter, bet):
    global currency
    
    nv = starter + randint(1, 10)
    
    if nv > 21:
        lc = currency
        
        currency = lc - bet
        
        
        print("Bust, " + str(nv - 21) + " over 21! You lose " + str(bet) + ". Current currency is " + str(currency) + ".\n")
        game()
    
    elif nv == 21:
        print("Perfect 21! \n")
        
        win = dealerlogic(nv)
        
        if win:
            currency += bet
            print("\nYou win, " + str(bet) + " has been added to your currency. \nCurrent Currency: " + str(currency)  + "\n")
            game()
        else:
            currency -= bet
            print("\nYou lost! " + str(bet) + " has been removed from your currency. \nCurrent Currency: " + str(currency) + "\n")
            game()
        
    else:
        ask(nv, bet)
        
#Double down logic
def doubledown(starter, bet):
    option = input("Are you sure you want to double down? (Yes or No)\n(Doubling down makes you double your bet and makes you draw a card.\nCurrent bet: " + str(bet) + "\nDouble Down Bet: " + str(min(bet * 2, currency)) + "\n").lower()
    
    if option == "yes":
      nb = min(bet * 2, currency)
      hit(starter, nb)
    elif option == "no":
       print("Understandable! \n")
       ask(starter, bet)
    else:
        print("Either yes or no!")
        doubledown(starter, bet)
    
    
def surrender(bet):
    global currency
    lc = currency
    
    currency = lc - (bet/2)
    
    print("Okay! You lose " + str(bet/2) + ". Current currency at " + str(currency))
    game()

#Start the game
def game():
    global inprogress
    
    if currency > 0:
        try:
            bet = int(input("How much would you like to bet? \nCurrent Currency: " + str(currency) + "\n")) 
        except ValueError:
            print("Not a proper response!\n")
            game()
    
        if bet > 0:
            if bet > currency: #bet too much
                print("You can't bet more than you have! \n")
        
                game()
    
            else: #game runs
                starter = randint(1, 10)
        
                ask(starter, bet)
        else:
            print("You have to bet a valid amount! \n")
            
            game()
    else:
        print("You are completely out of money!")
        return
    
game()
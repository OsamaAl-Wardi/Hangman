#Author: Osama Al-Wardi
#Github: https://github.com/OsamaAl-Wardi
#Date: 08/November/2018 
#Time: 02:47am
import io

#importing the random word library
from random_word import RandomWords
r = RandomWords()

##### ASCII ARTS #####
win = """
 __     ______  _    _  __          _______ _   _   _ 
 \ \   / / __ \| |  | | \ \        / /_   _| \ | | | |
  \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| | | |
   \   /| |  | | |  | |   \ \/  \/ /   | | | . ` | | |
    | | | |__| | |__| |    \  /\  /   _| |_| |\  | |_|
    |_|  \____/ \____/      \/  \/   |_____|_| \_| (_)                                                      
"""

lose = """
 __     ______  _    _   _      ____   _____ ______   _ 
 \ \   / / __ \| |  | | | |    / __ \ / ____|  ____| | |
  \ \_/ / |  | | |  | | | |   | |  | | (___ | |__    | |
   \   /| |  | | |  | | | |   | |  | |\___ \|  __|   | |
    | | | |__| | |__| | | |___| |__| |____) | |____  |_|
    |_|  \____/ \____/  |______\____/|_____/|______| (_)                                                                                    
"""

logo = """
 __          __  _                            _          _    _                                           _ 
 \ \        / / | |                          | |        | |  | |                                         | |
  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __   | |
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  | |
    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |  | | (_| | | | | (_| | | | | | | (_| | | | | |_|
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| (_)
                                                                             __/ |                          
                                                                            |___/                                             
"""

hang_stages = [
"""
   _________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """,

"""
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    H""",

"""
   _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___                       
    HA""",

"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    HAN""",


"""
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    HANG""",


"""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    HANGM""",



"""
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    HANGMA""",


"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    HANGMAN"""

]

#Game Function
def hangman ():
    misses = 0
    #Generate random word that is common
    word = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb",
                             minCorpusCount=145051, maxCorpusCount=1022775, minLength=4, maxLength=7)
    #The word displayed to the player with - covering the undiscovered characters
    display_word = ["-" for i in range(len(word))]
    print (*display_word)

    #Game loop
    while True:
        guess = input ("Please enter a guess character: ")
        #If the guess is right replace - by the guess
        if (guess in word):
            print("You found a character")
            #Finding which indicies are discovered by the player
            indicies = [i for i,j in enumerate(word) if j == guess]
            #Replacing -'s by the guess
            for i in range(len(display_word)):
                for j in indicies: 
                    if (i == j):
                        display_word[i] = guess
        else:
            misses += 1
            print("Wrong guess", "\n", hang_stages[misses], "\n")

        print(*display_word)

        #Checking if the player won
        if ("-" not in display_word):
            print("\n\n", win, "\n\n")
            break
        #Checking if the player lost
        if (misses == 7):
            print ("The word is :", word,"\n\n", lose, "\n\n")
            break

#Welcome to the game loop
print ("Welcome to \n \n", logo,"\n")
while True:
    game = input("enter s to play or q to quit: ")
    if game == "s":
        hangman()
    else:
        quit()
        

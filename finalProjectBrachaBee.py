import Draw 
import random 
import time 

#"I hereby certify that this program is solely the result of my own work and is in compliance with the Academic Integrity policy of the course syllabus and the academic integrity policy of the CS department. Racheli Schachter”

# [  0: 'food name to be displayed', 1: '300.gif', 2:bracha, 3:score, 4:explanation, 5: alternate ranking for two fruits (5/6) alternate food name ]
#I will add more cards. I already spent a lot of time downloading and resizing the images for the game and creating the number system. 
cards = [ ['           a bagel', 'bagel300.gif', 'hamotzi', 990, ' '],
          ['       wheat bread', 'bread300.gif', 'hamotzi', 990, ' '],
          ['      spelt bread', 'bread300.gif', 'hamotzi', 960, ' '],  
          ['     1000 pretzels', 'pretzel300.gif', 'hamotzi', 790, 'because pretzels are pat haba b\'kisnin and are hamotzi when \nenough pretzels are eaten'],
          ['       10 pancakes', 'pancakes300.gif', 'hamotzi', 790, 'because they are made from a runny batter and cooked with dry heat \nso they are considered pat haba b\'kisnin and is hamotzi when enough are eaten' ],
          ['   1 big croissant', 'croissant300.gif', 'hamotzi', 790, 'because it is pat haba b\'kisnin and is hamotzi when enough is \neaten'],
          ['   5 cinnamon buns', 'cinnamonbun300.gif', 'hamotzi', 790, 'because they are pat haba b\'kisnin and are hamotzi when enough is eaten'],
          ['        5 pretzels', 'pretzel300.gif', 'mezonot', 780, ' '],
          ['          Cheerios', 'cereal300.gif', 'mezonot', 740, ' '],
          ['         a cupcake', 'cupcake300.gif', 'mezonot', 780, ' '],
          ['           2 Oreos', 'oreo300.gif', 'mezonot', 780, ' '],
          ['         1 pancake', 'pancakes300.gif', 'mezonot', 780, ' '],
          ['           1/2 of a \n     cinnamon bun', 'cinnamonbun300.gif', 'mezonot', 770, ' ',"1/2 of a cinnamon bun"],
          ['           oatmeal', 'oatmeal300.gif', 'mezonot', 740, ' '],
          ['           pasta', 'pasta300.gif', 'mezonot', 750, ' '],
          ['    mushroom barley\n                soup', 'soup300.gif', 'mezonot', 745, 'because the barley is considered the ikar',"mushroom barley soup",],
          ['      grape juice', 'grapeJuice300.gif', 'hagafen', 690, ' '],
          ['               rice', 'rice300.gif', 'mezonot (for rice)', 650, 'according to most poskim'],
          ['     Rice Krispies', 'cereal300.gif', 'mezonot (for rice)', 650, 'according to most poskim'], 
          ['          an apple', 'apple300.gif', 'ha\'eitz', 580, ' ', 550],
          ['         avocado', 'avocado300.gif', 'ha\'eitz', 580, ' ', 550],
          ['             mango', 'mango300.gif', 'ha\'eitz', 580, ' ', 550],
          ['           an orange', 'orange300.gif', 'ha\'eitz', 580, ' ', 550],
          ['      sliced apple', 'apple300.gif', 'ha\'eitz', 520, ' ',520],
          ['           chunky \n       guacamole', 'avocado300.gif', 'ha\'eitz', 520, 'because the avocado is recognizable', 520, "chunky guacamole"],
          ['         homestyle \n        applesauce', 'applesauce300.gif', 'ha\'eitz', 520, 'because the apple is recognizable', 520, "homestyle applesauce"],
          ['      pomegranate', 'pomegranate300.gif', 'ha\'eitz', 590, ' ',590],
          ['             dates', 'date300.gif', 'ha\'eitz', 597, ' ', 597],
          ['            olives', 'olives300.gif', 'ha\'eitz', 599, ' ', 599],
          ['            grapes', 'grape300.gif', 'ha\'eitz', 595, ' ',595],
          ['     1/2 of a date', 'date300.gif', 'ha\'eitz', 547, ' ', 577],
          ['     1/2 of a grape', 'grape300.gif', 'ha\'eitz', 545, ' ', 575],
          ['          tomato', 'tomato300.gif', 'ha\'adama', 560, ' '],
          ['    chopped lettuce', 'lettuce300.gif', 'ha\'adama', 500, ' '],
          ['         a banana', 'banana300.gif', 'ha\'adama', 560, 'because no roots remain on the tree from year to year'],
          ['      a cucumber', 'cucumber300.gif', 'ha\'adama', 560, ' '],
          ['          pineapple', 'pineapple300.gif', 'ha\'adama', 560, 'because no roots remain on the tree from year to year'],
          ['      a strawberry', 'strawberry300.gif', 'ha\'adama', 560, 'because no roots remain on the tree from year to year'], 
          [' chunky vegetable\n               soup', 'soup300.gif', 'ha\'adama', 500, 'because the vegetables are recognizable', 'chunky vegetable soup'],
          ['     potato chips', 'chips300.gif', 'ha\'adama', 500, 'because they are still considered potatoes'],
          ['   mashed potatoes', 'rice300.gif', 'ha\'adama', 500, 'because it is still recognizable that it is made of potatoes '],
          ['   sweet potato \n            chips', 'sweetPotato300.gif', 'ha\'adama', 500, 'because they are still considered \nsweet potatoes', 'sweet potato chips'],
          ['         popcorn', 'popcorn300.gif', 'ha\'adama', 500, 'because it is still considered corn'],
          ['         American \n       Cornflakes', 'cereal300.gif', 'ha\'adama', 500, 'because they are made from whole kernels', 'American cornflakes'],
          ['      cooked lettuce', 'lettuce300.gif', 'shehakol' , 490, 'because this is not the normal way of eating lettuce'],
          ['frozen grape juice', 'grapeIces300.gif', 'shehakol', 480, 'because some maintain that it loses its chashivut in this form'],
          ['        a cooked \n        cucumber', 'cucumber300.gif', 'shehakol', 490, 'because this is not the normal way of eating a cucumber', "a cooked cucumber"],
          ['          mushrooms', 'mushroom300.gif', 'shehakol', 490, 'because they get nutrients from the air, not the ground'],
          ['Israeli cornflakes', 'cereal300.gif', 'shehakol', 490, 'because they are made from corn flour'], 
          ['          salmon', 'salmon300.gif', 'shehakol', 490, ' '],
          ['            smooth \n        applesauce', 'appleSauce300.gif', 'shehakol', 480, 'because the fruit is not recognizable', "smooth applecauce"],
          ['         cookie dough', 'cookieDough300.gif', 'shehakol', 490, 'because raw flour is shehakol'], 
          ['           ice cream', 'icecream300.gif', 'shehakol', 480, ' '],
          ['    smooth peanut \n           butter', 'peanutButter300.gif', 'shehakol', 490, 'because some say that the peanuts are not recognizable', "smooth peanut butter"],
          ['      chunky peanut \n              butter', 'peanutButter300.gif', 'shehakol', 490, 'because the chunks are secondary to the peanut butter\n which is shehakol', "chunky peanut butter"],
          ['        apple juice', 'appleJuice300.gif', 'shehakol', 470, 'because fruit juice is usually shehakol'], 
          ['      chicken soup \n             broth', 'soup300.gif', 'shehakol', 470, ' ', "chicken soup broth"], 
          ['  pureed vegetable \n               soup', 'soup300.gif', 'shehakol', 480, 'because the vegetables are not recognizable', "pureed vegetable soup"], 
          ['            coffee', 'coffee300.gif', 'shehakol', 470, ' '],
          ['           ice cubes', 'iceCube300.gif', 'shehakol', 480, ' ']
          ]   

#the first screen that you say displays the rules of the game and returns the player's level choice 

def intro():
    #first screen with the rules 
    Draw.picture("openingSlide.gif", 0, 0)
    Draw.show()
    #determine player's level choice. returns e for easy and h for hard 
    
    while True:
        if Draw.hasNextKeyTyped():
            key = Draw.nextKeyTyped()          # see if key was tapped 
            if key == "e" or key == "E":       # only respond if key was e or h. 
                ##is it more efficient to do key.lower? does it make a dif? 
                return "e"                     
            elif key == "h" or key == "H":
                return "h"                     #return the answer to be used in select cards 

# this function is a loop that runs through all of the cards to test them. This code takes parameter "round" based on what round of the game it is. round is set later in the main code
def testCards(round):
    card1 = cards[round]
    card2 = cards[round+10]   
    return card1,card2

def selectCards(mode):
#randomly choose two cards from the deck/list that the player will be asked to compare. this function takes 1 parameter- the mode that was selected in the intro function. This function returns card1 and card2.
    #randomly choose 2 cards 
    card1 = cards[random.randint(0,len(cards)-1)]            
    card2 = cards[random.randint(0,len(cards)-1)]
    
    #for easy mode, ensure that the cards are differnet levels by making sure the level starts with a different digit
    if mode == "e":                                         
        while card1[3]//100 == card2[3]//100:                # if levels are the same (rank starts with the same first digit)
            card2 = cards[random.randint(1,len(cards)-1)]    # continue to choose a new card until the levels are different 
            
    #for hard mode, ensure that cards are close in level- start with similar first digits- within 1       
    elif mode == "h":                                       
        while card1[3] == card2[3] \
              or abs(card1[3]//100-card2[3]//100) >= 2 \
              or int(card1[3]) + int(card2[3]) == 950 \
              or int(card1[3]) + int(card2[3]) == 970:      # safeik if some foods are food or drink, so these foods will not be compared to other shehakol foods. 
                                                            # those cards are ranked at 580, so they will not be compared to a 570 or 590
            card2 = cards[random.randint(1,len(cards)-1)]   # choose a new card until the two are close / no safeik           

    return card1, card2           

# this function draws the board. it takes 3 parameters- card 1 and card 2 from selectCards, and score 
def drawBoard(card1, card2, score):
    #draw the header
    Draw.picture("brachaBee800.gif",100,0)      
    
    #draws the score on the bottom of the board 
    Draw.setColor(Draw.BLACK)
    Draw.setFontFamily('BM Jua')
    Draw.setFontSize(30)
    Draw.string("SCORE: "+ str(score), 750,700)
    
    #draw the cards with text under
    #card 1 
    Draw.picture(card1[1],100 ,200 )
    Draw.string(card1[0].upper(),100,550) 
    #card 2 
    Draw.picture(card2[1],600 ,200 )
    Draw.string(card2[0].upper(),600,550)   

# this function gathers and returns the players response- either left or right 
def getInput ():    
    while True:                                      # see if a key is typed 
        if Draw.hasNextKeyTyped():
            key = Draw.nextKeyTyped()                # if the key is the right or left key, return it 
            if key == "Left" or key == "Right":        
                return key
        
# this function determines if the player got the answer correctly. it takes 3 parameters- the player's response and the two cards. This function returns the results of the round- roundScore. 
def evaluate(playerAns, card1, card2): 
    #initially set the score to 0 for that round 
    roundScore = 0              
    
    # if you have two fruits, the "rankings" change. usually shalem takes precendence but when comparing two fruits, 7 minim takes precedence regardless of if it is whole. if this is the case, an alternate ranking (element []) is looked at instead of the usual ranking in [3]. 
    if ('eitz' in card1[2] and 'eitz' in card2[2]): 
        if card1[5] > card2[5]:
            correctAns = "Left" 
        else: 
            correctAns = "Right"    

    #if it is not two fruits, evaluate the normal ranking in [3]. 
    else:
        if card1[3] > card2[3]:
            correctAns = "Left" 
        else: 
            correctAns = "Right"
            
    #see if player is correct  
    if playerAns == correctAns:                      # if player's answer is the correct answer
        Draw.picture("greatJob500.gif",250,200)      # display success message 
        roundScore += 1                              # and increment score 
    else:                                            # if wrong,  
        Draw.picture("goodTry500.gif", 250, 200)     # sorry message 
        
    Draw.show()
    time.sleep(1)                                    # show display message for one second 
    
    return roundScore                                # return results of the round- round score will be 1 if the person won 

#this function explains why the answer to the previous round. takes 2 parameters- card1 and card2. it doesn't return anything, only displays things
def explanation(card1,card2):
    Draw.clear()
    Draw.setFontSize(20)  
    Draw.picture("brachaBee800.gif",100,0) 
    
    #make sure that it prints the name of the food with out the spaces for formatting 
    if "\n" in card1[0]:              # for card 1, if there is spaces in the formatting (shown by \n)
        name1 = card1[-1]             # print alternate name in [-1]  
    else: 
        name1 = card1[0].strip()      # no spaces- use regular name, stripped of preceeding spaces
    
    if "\n" in card2[0]:              # same for card 2
        name2 = card2[-1]
    else: 
        name2 = card2[0].strip()              
    
    # print statement: the bracha on food x is y because z 

    bracha1 = "The bracha on " +  name1 + " is " + card1[2] + " " + card1[4]
    bracha2 = "The bracha on " +  name2 + " is " + card2[2] + " " + card2[4]  
    
    # draw the brachot for each food 
    Draw.string(bracha1, 15,300)
    Draw.string(bracha2, 15,400) 
    
    #explanations for each
    
    #fruit vs. fruit   
    if "ha'eitz" in card1[2] and "ha'eitz" in card2[2]:
        Draw.string("Fruits from the 7 minim come first in the following order: olives, dates, grapes, figs, pomegranate. \nWhole fruits come before broke fruits", 15, 500)  
   
    #fruit vs. vegetable 
    elif  ("ha'eitz" in card1[2] or "ha\'adama" in card1[2])\
        and ("ha'eitz" in card2[2] or "ha\'adama" in card2[2]):
        Draw.string("Whole foods come before broken foods, 7 minim come before not 7 minim, ha\'eitz comes before ha\'adama", 15, 500)
    
    # two different brachot (other than eitz vs. adama)    
    elif card1[2] != card2[2]:
        if card1[3] > card2[3]:
            greaterBracha = card1[2]
            lowerBracha = card2[2]
        else:
            greaterBracha = card2[2]
            lowerBracha = card1[2]
        Draw.string("The bracha of " + greaterBracha + \
                " comes before the bracha of " + lowerBracha, 15, 500)     
        
    #if two foods are both hamotzi 
    elif "hamotzi" in card1[2] and "hamotzi" in card2[2]:
        Draw.string("For bread, regular bread comes before pat haba b\'kisnin. Between different grains, the order is as follows: \nwheat, barley, spelt, rye, oat", 15, 500)
    
    #if two foods are both mezonot 
    elif "mezonot" in card1[2] and "mezonot" in card2[2]:
        Draw.string("For mezonot, baked items go before cooked items, and whole items are before broken items. \nBetween different grains, the order is as follows: wheat, barley, spelt, rye, oat. Mezonot on rice comes last.", 15, 500)   
    
    # shehakol vs. shehakol      
    elif "shehakol" in card1[2] and "shehakol" in card2[2]:
        Draw.string("Many hold that shehakol on foods comes before a shehakol on drinks", 15, 500) 
        
 
    # space bar to continue 
    Draw.string("PRESS THE SPACE BAR TO CONTINUE", 350,750)
    Draw.show()
    while True:
        if Draw.hasNextKeyTyped():        # if space bar is tapped, return to next step in the loop
            key = Draw.nextKeyTyped()    
            if key == "space":  
                return 

# this function displays the ending screen of the game. it takes one parameter- the total score, and it displays this on the screen. 
def ending(score):
    Draw.picture("finishSlide.gif") 
    Draw.setFontSize(50)
    Draw.string(score, 600, 425)
    Draw.setFontSize(15)
    Draw.string("\tFor further study on the order of berachot, see Shulchan Aruch and Aruch HaShulchan siman 211, \n\t\tChayei Adam klal 57 and The Halachos of Brachos by R' Bodner pg. 166-171",100,725)
    
    #If the player wants to play again, tap the space bar 
    while True:
        if Draw.hasNextKeyTyped():        # if space bar is tapped, return to the top of main
            key = Draw.nextKeyTyped()    
            if key == "space":  
                return 
    Draw.show()

#main code!     
def main():
    #set canvas size 
    Draw.setCanvasSize(1000,800)
    #round = 0   #this is used to establish the round when on testCode instead of the regular random card selection
    
    #game loop 
    while True:         # forever loop for the entire game 
        mode = intro()  # show the intro screen and get the player's mode preference (easy or hard)#show the intro screen and get the player's mode preference (easy or hard)
        score = 0       # set initial score to 0                  
        
        # for 10 rounds- in each round:  
        for i in range(10):
            Draw.clear()           
            card1, card2 = selectCards(mode)            # choose 2 cards. store as the variables "card1" and "card2"
            #card1, card2 = testCards(round)                 # choose 2 cards based on round. this is invoked instead of regular select cards when testing
            drawBoard(card1, card2, score)              # draw header, card 1, card 2, current total score 
            Draw.show()                                 # display the board
            playerAns = getInput()                      # see player's answer. store as the variable "playerAns"
            score += evaluate(playerAns, card1, card2)  # evaluate the player's answer. increment the total score accordingly 
            explanation(card1, card2)                   # show explanation/answer. what each bracha is and why one comes before the other 
            #round +=1                                       # this increments the round when in testCard mode
        
        #at the end of ten rounds, display ending message and final score. if player chooses to play agian, go back to top of forever loop. 
        ending(score)
main() 

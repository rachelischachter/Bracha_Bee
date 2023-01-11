import random 
import Draw 

def numberSelectionTest ():
    mode = random.randint(0,1) 
    
    for i in range(10):
        card1 = random.randint(1,500)
        card2 = random.randint(1,500) 
        if mode == 0:
            while card1//100 == card2//100: 
                card2 = random.randint(1,500)  
        elif mode == 1: 
            while card1 == card2 or abs(card1//100-card2//100) >= 1:
                card2 = random.randint(1,500)      
        print (mode, card1//100, card2//100) 
        
     
cards = [ ['           a bagel', 'bagel300.gif', 'hamotzi', 990, ' '],
          ['       wheat bread', 'bread300.gif', 'hamotzi', 990, ' '],
          ['      spelt bread', 'bread300.gif', 'hamotzi', 960, ' '],  
          ['     100 pretzels', 'pretzel300.gif', 'hamotzi', 790, 'because pretzels are pat haba b\'kisnin and are hamotzi when \nenough pretzels are eaten'],
          ['       10 pancakes', 'pancakes300.gif', 'hamotzi', 790, 'because they are made from a runny batter and cooked with dry heat \nso they are considered pat haba b\'kisnin and is hamotzi when enough is eaten' ],
          ['   1 big croissant', 'croissant300.gif', 'hamotzi', 790, 'because it is pat haba b\'kisnin and is hamotzi when enough is eaten'],
          ['   5 cinnamon buns', 'cinnamonbun300.gif', 'hamotzi', 790, 'they are pat haba b\'kisnin and are hamotzi when enough is eaten'],
          ['        5 pretzels', 'pretzel300.gif', 'mezonot', 780, ' '],
          ['          Cheerios', 'cereal300.gif', 'mezonot', 760, ' '],
          ['         a cupcake', 'cupcake300.gif', 'mezonot', 780, ' '],
          ['           2 Oreos', 'oreo300.gif', 'mezonot', 780, ' '],
          ['         1 pancake', 'pancakes300.gif', 'mezonot', 780, ' '],
          ['           1/2 of a \n     cinnamon bun', 'cinnamonbun300.gif', 'mezonot', 770, ' ',"1/2 of a cinnamon bun"],
          ['           oatmeal', 'oatmeal300.gif', 'mezonot', 740, ' '],
          ['           pasta', 'pasta300.gif', 'mezonot', 750, ' '],
          ['    mushroom barley\n                soup', 'soup300.gif', 'mezonot', 745, 'because the barley is considered the ikar',"mushroom barley soup",],
          ['      grape juice', 'grapeJuice300.gif', 'hagafen', 690, ' '],
          ['               rice', 'rice300.gif', 'mezonot (for rice)', 650, 'according to most poskim'],
          ['     rice Krispies', 'cereal300.gif', 'mezonot (for rice)', 650, 'according to most poskim'], 
          ['          an apple', 'apple300.gif', 'ha\'eitz', 580, ' ', 550],
          ['         avocado', 'avocado300.gif', 'ha\'eitz', 580, ' ', 550],
          ['             mango', 'mango300.gif', 'ha\'eitz', 580, ' ', 550],
          ['           an orange', 'orange300.gif', 'ha\'eitz', 580, ' ', 550],
          ['      sliced apple', 'apple300.gif', 'ha\'eitz', 580, ' ',520],
          ['           chunky \n       guacamole', 'avocado300.gif', 'ha\'eitz', 520, 'because the avocado is recognizable', 520, "chunky guacamole"],
          ['         homestyle \n        applesauce', 'applesauce300.gif', 'ha\'eitz', 520, 'because the apple is recognizable', 520, "homestyle applesauce"],
          ['      pomegranate', 'pomegranate300.gif', 'ha\'eitz', 590, ' ',590],
          ['             dates', 'date300.gif', 'ha\'eitz', 597, ' ', 597],
          ['            olives', 'olives300.gif', 'ha\'eitz', 599, ' ', 599],
          ['            grapes', 'grape300.gif', 'ha\'eitz', 595, ' ',595],
          ['     1/2 of a date', 'date300.gif', 'ha\'eitz', 547, ' ', 577],
          ['     1/2 of a grape', 'grape300.gif', 'ha\'eitz', 545, ' ', 575],
          ['          tomato', 'tomato300.gif', 'ha\'adama', 560, ' '],
          ['    chopped Lettuce', 'lettuce300.gif', 'ha\'adama', 500, ' '],
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
          ['        apple juice', 'appleJuice300.gif', 'shehakol', 470, 'because fruit juice is shehakol'], 
          ['      chicken soup \n             broth', 'soup300.gif', 'shehakol', 470, ' ', "chicken soup broth"], 
          ['  pureed vegetable \n               soup', 'soup300.gif', 'shehakol', 480, 'because the vegetables are not recognizable', "pureed vegetable soup"], 
          ['            coffee', 'coffee300.gif', 'shehakol', 470, ' '],
          ['           ice cubes', 'iceCube300.gif', 'shehakol', 480, ' ']
          ]         
def explanationTest():
    card1 = cards[0]            
    card2 = cards[1]     
def centerText():
    Draw.setCanvasSize(1000,800)
    
    card1 = cards[59]            
    card2 = cards[60]
   
    Draw.setColor(Draw.BLACK)
    Draw.setFontFamily('BM Jua')
    Draw.setFontSize(30) 
    
    #draw the cards with text under
    #card 1 
    Draw.picture(card1[1],100 ,200 )
    Draw.string(card1[0].upper(),100,550) 
    #card 2 
    Draw.picture(card2[1],600 ,200 )
    Draw.string(card2[0].upper(),600,550)     
        
centerText()

def cardTest():
    mode = random.randint(0,1)   
    for i in range(10):
        card1 = cards[random.randint(0,len(cards)-1)]
        card2 = cards[random.randint(0,len(cards)-1)]
        
        #for easy mode 
        #if mode == 0:                                           # ensure that the cards are differnet levels by making sure the level starts with a different digit
            #while card1[3]//100 == card2[3]//100:                # if leves are the same  
                #card2 = cards[random.randint(1,len(cards)-1)]    # continue to choose a new card until the levels are different 
        if mode == 0:
            while abs(card1[3]//100-card2[3]//100) <= 2:
                card2 = cards[random.randint(1,len(cards)-1)]
        #for hard mode,         
        elif mode == 1:                                                        # ensure that cards are close in level- start with similar first digits- within 2          
            while card1[3] == card2[3] \
                  or abs(card1[3]//100-card2[3]//100) >= 2 \
                  or int(card1[3]) + int(card2[3]) == 950 \
                  or int(card1[3]) + int(card2[3]) == 970:                       # safeik if some foods are food or drink, so these foods will not be compared to other shehakol
                card2 = cards[random.randint(1,len(cards)-1)]                    # choose a new card until the two are close / no safeik  
        
        print (mode, "\t", "Card 1:", card1[0].strip(), ",", card1[3], "\tCard 2:", card2[0].strip(), ",", card2[3])


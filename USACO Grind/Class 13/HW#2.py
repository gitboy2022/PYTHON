#HW#20

#FOR THIS HW, you will not be assigned a grade
#IF you don't do it

#Please submit your HW to get at least 80% : 
#Doing at least 1 of the problems and getting it correct.

#NOTE: This is due at 12AM EST of the next time / day we meet!!!
#NOTE2: Please submit your USACO / Codeforces answer to the website 
#If it does not pass ALL test cases, your answer will be considered
#INCORRECT!!!


#Requirements to get +10% :
#  Correctly answer AT LEAST 2 questions for #1.  Leetcode Questions

#Requirements to get +20% :
#  Correctly answer ALL questions for #1.  Leetcode Questions (There are 3 Questions)




#1.  Leetcode Questions

#Solve the following Leetcode Questions
#as was given in the instructions from HW#9 / HW#10



#a.  Minimum Average of Smallest and Largest Elements

# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/description/

###COPY / PASTE Minimum Average of Smallest and Largest Elements


###END Minimum Average of Smallest and Largest Elements





#b.  Find the Winning Player in Coin Game

# https://leetcode.com/problems/find-the-winning-player-in-coin-game/description/


###COPY / PASTE Find the Winnning Player in Coin Game

class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        turn = 0
        while True:
            x -= 1; y -= 4
            if x >= 0 and y >= 0:
                turn +=1
            elif turn % 2 == 0:
                return "Bob"
            else:
                return "Alice"

###END Find the Winnning Player in Coin Game




#c.  Harshad Number

# https://leetcode.com/problems/harshad-number/description/

###COPY / PASTE Harshad Number


###END Harshad Number






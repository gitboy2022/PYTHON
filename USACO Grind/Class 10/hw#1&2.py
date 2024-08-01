#HW#17

#Remember, you get 80% for submitting your
#classwork before the session ends.
#See below to see the requirements for getting +10% and +20%

#NOTE: This is due at 12AM EST of the next time / day we meet!!!
#NOTE2: Please submit your USACO / Codeforces answer to the website 
#If it does not pass ALL test cases, your answer will be considered
#INCORRECT!!!


#Requirements to get +10% :
#  Correctly answer AT LEAST 2 questions for #1.  Leetcode Questions

#Requirements to get +20% :
#  Correctly answer >= 4 questions for #1.  Leetcode Questions
#  Correctly answer #2.  USACO - Watching Mooloo



#1.  Leetcode Questions

#Solve the following Leetcode Questions
#as was given in the instructions from HW#9 / HW#10


#a.  Final Value of Variable After Performing Operations

# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/


###COPY / PASTE Final Value of Variable After Performing Operations

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for o in operations:
            if o == "X++":
                x += 1
            elif o == "++X":
                x += 1
            else:
                x -= 1
        return x


###END Final Value of Variable After Performing Operations




#b.  Count Common Words With One Occurrence

# https://leetcode.com/problems/count-common-words-with-one-occurrence/description/


###COPY / PASTE Count Common Words With One Occurrence

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count = 0
        for w in words1:
            if words1.count(w) == 1 and words2.count(w) == 1:
                count += 1
        return count


###END Count Common Words With One Occurrence




#c.  Find the Middle Index in Array

# https://leetcode.com/problems/find-the-middle-index-in-array/description/

###COPY / PASTE Find the Middle Index in Array


###END Find the Middle Index in Array




#d.  Check If Every Row and Column Contains All Numbers

# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/description/


###COPY / PASTE Check If Every Row and Column Contains All Numbers


###END Check If Every Row and Column Contains All Numbers




#e.  Minimum Common Value

# https://leetcode.com/problems/minimum-common-value/description/

###COPY / PASTE Minimum Common Value


###END Minimum Common Value




#2.  USACO - Watching Mooloo

#Please answer the following USACO question below.

#MAKE SURE TO SUBMIT YOUR FILE / SOLUTION to USACO
#AND CHECK IT WORKS COMPLETELY!

#IF IT DOESN'T WORK COMPLETELY (AS IN PASSES ALL TEST CASES)
#YOU DO NOT RECEIVE CREDIT FOR THIS PROBLEM!!!

#GOOD LUCK!

# https://usaco.org/index.php?page=viewproblem2&cpid=1301
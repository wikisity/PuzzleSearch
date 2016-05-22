# Auhtor: ARNOLD EPANDA
# Date: 5/2/2016
# E-mail: aepanda1@umbc.edu
# Description: The lines of code below are a python project called a Recursive Word Search
               # A word search is a 2-dimensional grid or matrix of letters which contains 'hidden words.'
               # The person working the puzzle is given a list of words that are hidden in the matrix and is
               # asked to locate and circle them. The fun part is that the word my appear horizontally,
               # vertically or diagollany in the grid. Horizontal words may be written left-to-right or right-to-left.
               # Vertically oriented words may be written top-down or bottom-up. Similarly for diagonally oriented words.
              
              
               
# searchLetter(): takes in 4 parameters and outputs True if the first character of
                  # the word we are looking for is found. False,  otherwise. It also ouputs a list
                  # of index where the character is found.

# Input: 4 parameters which are the first character of the word, the puzzle list to
         # search the character in, a counter to update lines of the puzzle list where we
         # last found this first character, another counter to update columns of the puzzle list
         # where we have last seen this character

# Output: returns TRUE and the index list if character is found, FALSE and the index list if character
          # is not found
          
def searchLetter(aChar, thePuzzleList, thisCounter1, thisCounter2):
    indexList = []
    foundChar = False
    for i in range(thisCounter1, len(thePuzzleList)): # variable 'thisCounter1' tells what line we are in as we search through columns
        for j in range(thisCounter2, len(thePuzzleList[i])): # variable 'thisCounter2' updates the column we r in as we look for the character
            if thePuzzleList[i][j] == aChar:
                indexList.append(i)
                indexList.append(j)
                foundChar = True
                return foundChar, indexList

            else:
                if j == (len(thePuzzleList[i]) - 1): # We did not find the character, we look for the character in the next line
                    thisCounter2 = 0 # As we go to the next line, we want to start searching at column zero of the line

    return foundChar, indexList
    
    

# searchWord(): First off, this is a recursive function. Assuming we search the word in only one direction, this function
                # takes in 5 parameters
                # and returns TRUE and the DIRECTION the word was found. Returns FALSE and an empty DIRECTION otherwise.
                # Since we have to branch into 8 DIRECTIONS while searching the word, then this function takes 26 parameters

# Input: Assuming we search to only one direction, then this function takes in parameters line and column to where to start
         # the search of the word. A parameter puzle list to search the word, a parameter  word to search in, and a counter parameter
         # to update the letter of the word to compare/search. Now that we branch to 8 DIRECTIONS, we include 8 different lines and columns
         # variable, we include the puzzle list to search the word, the word to search, and 8 different counters that are bounded to each and only
         # each DIRECTION. The pair (line, coulmn) and counter variable are bounded to each direction.

# Ouput: Returns TRUE and the DIRECTION if we find the word. FALSE and empty DIRECTION, otherwise.

def searchWord(indexi1, indexj1, indexi2, indexj2, indexi3, indexj3, indexi4, indexj4, indexi5, indexj5, indexi6, indexj6, indexi7, indexj7, indexi8, indexj8, thisPuzz\
leList, thisWord, counter1, counter2, counter3, counter4, counter5, counter6, counter7, counter8):

    direction = ""
    puzzle_found = False

    if thisWord[counter1] == thisPuzzleList[indexi1][indexj1]:
        if counter1 == (len(thisWord) - 1): # We stop our recursion call, once we reach the length of the word
            puzzle_found = True
            direction = "up"
            return puzzle_found, direction
        elif counter1 < (len(thisWord) - 1):
            if indexi1 - 1 >= 0: # Here we are still in the range of the word's length and we want to make sure to be in the range of the puzzle
                return searchWord(indexi1 - 1, indexj1, indexi2, indexj2, indexi3, indexj3, indexi4, indexj4, indexi5, indexj5, indexi6, indexj6, indexi7, indexj7, ind\
exi8, indexj8, thisPuzzleList, thisWord, counter1 + 1, counter2, counter3, counter4, counter5, counter6, counter7, counter8)

    #Below, variable 'counter2', 'indexi2', 'indexj2' are bounded to their direction. They get update if the search is kept into
    # the same direction while other variables like: 'counter1', 'indexi1', 'indexj1' ...etc, are held constant
    if thisWord[counter2] == thisPuzzleList[indexi2][indexj2]:
        if counter2 == (len(thisWord) - 1):
            puzzle_found = True
            direction = "diagonally up and right"
            return puzzle_found, direction
        elif counter2 < (len(thisWord) - 1):
            if (indexi2 - 1 >= 0) and (indexj2 + 1 < len(thisPuzzleList[indexi2])):
                return searchWord(indexi1, indexj1, indexi2 - 1, indexj2 + 1, indexi3, indexj3, indexi4, indexj4, indexi5, indexj5, indexi6, indexj6, indexi7, indexj7,\
 indexi8, indexj8, thisPuzzleList, thisWord, counter1, counter2 + 1, counter3, counter4, counter5, counter6, counter7, counter8)
 
    if thisWord[counter3] == thisPuzzleList[indexi3][indexj3]:
        if counter3 == (len(thisWord) - 1):
            puzzle_found = True
            direction = "right"
            return puzzle_found, direction
        elif counter3 < (len(thisWord) - 1):
            if indexj3 + 1 < len(thisPuzzleList[indexi3]):
                return searchWord(indexi1, indexj1, indexi2, indexj2, indexi3, indexj3 + 1, indexi4, indexj4, indexi5, indexj5, indexi6, indexj6, indexi7, indexj7, ind\
exi8, indexj8, thisPuzzleList, thisWord, counter1, counter2, counter3 + 1, counter4, counter5, counter6, counter7, counter8)

    if thisWord[counter4] == thisPuzzleList[indexi4][indexj4]:
        if counter4 == (len(thisWord) - 1):
            puzzle_found = True
            direction = "diagonally down and right"
            return puzzle_found, direction
        elif counter4 < (len(thisWord) - 1):
            if (indexi4 + 1 < len(thisPuzzleList)) and (indexj4 + 1 < len(thisPuzzleList[indexi4])):
                return searchWord(indexi1, indexj1, indexi2, indexj2, indexi3, indexj3, indexi4 + 1, indexj4 + 1, indexi5, indexj5, indexi6, indexj6, indexi7, indexj7,\
  indexi8, indexj8, thisPuzzleList, thisWord, counter1, counter2, counter3, counter4 + 1, counter5, counter6, counter7, counter8)
  
    if thisWord[counter5] == thisPuzzleList[indexi5][indexj5]:
        if counter5 == (len(thisWord) - 1):
            puzzle_found = True
            direction = "down"
            return puzzle_found, direction
        elif counter5 < (len(thisWord) - 1):
            if indexi5 + 1 < len(thisPuzzleList):
                return searchWord(indexi1, indexj1, indexi2, indexj2, indexi3, indexj3, indexi4, indexj4, indexi5 + 1, indexj5, indexi6, indexj6, indexi7, indexj7, ind\
exi8, indexj8, thisPuzzleList, thisWord, counter1, counter2, counter3, counter4, counter5 + 1, counter6, counter7, counter8)

    if thisWord[counter6] == thisPuzzleList[indexi6][indexj6]:
        if counter6 == (len(thisWord) - 1):
            puzzle_found = True
            direction = "diagonally down and left"
            return puzzle_found, direction
        elif counter6 < (len(thisWord) - 1):
            if (indexi6 + 1 < len(thisPuzzleList)) and (indexj6 - 1 >= 0):
                return searchWord(indexi1, indexj1, indexi2, indexj2, indexi3, indexj3, indexi4, indexj4, indexi5, indexj5, indexi6 + 1, indexj6 - 1, indexi7, indexj7,\
 indexi8, indexj8, thisPuzzleList, thisWord, counter1, counter2, counter3, counter4, counter5, counter6 + 1, counter7, counter8)
 
    if thisWord[counter7] == thisPuzzleList[indexi7][indexj7]:
        if counter7 == (len(thisWord) - 1):
            puzzle_found = True
            direction = "backwards left"
            return puzzle_found, direction
        elif counter7 < (len(thisWord) - 1):
            if indexj7 - 1 >= 0:
                return searchWord(indexi1, indexj1, indexi2, indexj2, indexi3, indexj3, indexi4, indexj4, indexi5, indexj5, indexi6, indexj6, indexi7, indexj7 - 1, ind\
exi8, indexj8, thisPuzzleList, thisWord, counter1, counter2, counter3, counter4, counter5, counter6, counter7 + 1, counter8)

    if thisWord[counter8] == thisPuzzleList[indexi8][indexj8]:
        if counter8 == (len(thisWord) - 1):
            puzzle_found = True
            direction = "diagonally up and left"
            return puzzle_found, direction
        elif counter8 < (len(thisWord) - 1):
            if (indexi8 - 1 >= 0) and (indexj8 - 1 >= 0):
                return searchWord(indexi1, indexj1, indexi2, indexj2, indexi3, indexj3, indexi4, indexj4, indexi5, indexj5, indexi6, indexj6, indexi7, indexj7, indexi8\
 - 1, indexj8 - 1, thisPuzzleList, thisWord, counter1, counter2, counter3, counter4, counter5, counter6, counter7, counter8 + 1)
 
     return puzzle_found, direction
     

def main():
    word_list = []
    puzzle_list = []
    found_word = False
    found_char = False

    print("Welcome to the Word Search")
    print("For this, you will import two files: 1. The puzzle board, and 2. The word list.")

    puzzle_file = input("What is the puzzle file you would like to import?: ")
    this_file1 = open(puzzle_file)
    for line in this_file1:
        puzzle_list.append(line.strip().split())
    this_file1.close()


    word_file = input("What is the word list file you would like to import?: ")
    this_file2 = open(word_file)
    for line in this_file2:
        word_list.append(line.strip())
    this_file2.close()

    for k in range(len(word_list)):
        counter_puzzle_line = 0
        counter_puzzle_column = 0

        while counter_puzzle_line < len(puzzle_list):
            found_char, index_list = searchLetter(word_list[k][0], puzzle_list, counter_puzzle_line, counter_puzzle_column)

            if found_char:
                this_indexi1 = index_list[0]
                this_indexj1 = index_list[1]
                counter_char1 = 0

                this_indexi2 = index_list[0]
                this_indexj2 = index_list[1]
                counter_char2 = 0

                this_indexi3 = index_list[0]
                this_indexj3 = index_list[1]
                counter_char3 = 0

                this_indexi4 = index_list[0]
                this_indexj4 = index_list[1]
                counter_char4 = 0

                this_indexi5 = index_list[0]
                this_indexj5 = index_list[1]
                counter_char5 = 0

                this_indexi6 = index_list[0]
                this_indexj6 = index_list[1]
                counter_char6 = 0

                this_indexi7 = index_list[0]
                this_indexj7 = index_list[1]
                counter_char7 = 0

                this_indexi8 = index_list[0]
                this_indexj8 = index_list[1]
                counter_char8 = 0

                found_word, direction = searchWord(this_indexi1, this_indexj1, this_indexi2, this_indexj2, this_indexi3, this_indexj3, this_indexi4, this_indexj4, this\
_indexi5, this_indexj5, this_indexi6, this_indexj6, this_indexi7, this_indexj7, this_indexi8, this_indexj8, puzzle_list, word_list[k], counter_char1, counter_char2, co\
unter_char3, counter_char4, counter_char5, counter_char6, counter_char7, counter_char8)

                if not(found_word):
                    if (this_indexj1 + 1) < len(puzzle_list[this_indexi1]): #If we are still in the range of line's length
                        counter_puzzle_column = this_indexj1 + 1  # Then keep searching through that line
                        counter_puzzle_line = this_indexi1

                    else: # We are out of the range of a line, then go to next line and start searching at column zero
                        counter_puzzle_line = this_indexi1 + 1 # We pass the variable on the left of this operation to searchLetter()
                        counter_puzzle_column = 0 # This is a variable that we pass as a parameter to the function searchLetter()

                elif found_word:
                    print("The word", word_list[k], "starts in", this_indexi1, ",", this_indexj1, "and goes", direction)
                    counter_puzzle_line = len(puzzle_list)
            elif not(found_char):
                counter_puzzle_line = len(puzzle_list)


        if not(found_word):
            print("The word", word_list[k], "does not appear in the puzzle.")


main()

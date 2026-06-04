class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Explore
        #The idea is to see whether one string is technically just another
        #but in a different order of characters
        #CQ - can both strings be empty or none? what is the max size of string possible?
        #Brainstorm
        #FI - sort both strings and then check if their equal Time- O(n) space- O(1) if it's inplace
        #O(n) if it isn't in place
        #SI - make one string into a list of characters then loop through
        #the characters of the second string and check against the original list of characters
        #until you find a unique one. 
        #Plan
        #Implement
        if len(s) != len(t):
            return False
        
        myDict = {}
        for char in s:
            myDict[char] = myDict.get(char, 0) + 1

        for char in t:
            if char not in myDict or myDict[char] <= 0:
                return False
            myDict[char] -= 1
        return True
        #Verify
        
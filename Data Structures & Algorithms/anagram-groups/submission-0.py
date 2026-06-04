class Solution:
    def makeFrequencyTuple(self, word: str) -> tuple:
        result = [0] * 26
        for char in word:
            index = ord(char) - ord('a')
            result[index] += 1
        return tuple(result)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Explore
        #The idea is to group a list of strings into lists of their anagrams.
        #CQ-Can the list be empty?
        #Brainstorm
        #FI-Loop through the list for each string word. Using a double for loop
        #Compare every word in the list to every other word and if they are anagrams of each other remove
        #all of them from the original list
        #SI-Sort each word and use the sorted word as a key in a dictionary. Then the values would be the
        #list of anagram words. 
        #TI-Same idea as the second except this time the key is tuple of the frequency count of letters
        #Plan
        #Using TI
        #Time complexity- O(n*k)
        #Space complexity - O(k)
        #Implement
        freq_dictionary = {}
        if not strs:
            return None
        for word in strs:
            freq_key = self.makeFrequencyTuple(word)
            if freq_key not in freq_dictionary:
                freq_dictionary[freq_key] = [word]
            else:
                freq_dictionary[freq_key].append(word)
        return list(freq_dictionary.values())
        #Verify

         
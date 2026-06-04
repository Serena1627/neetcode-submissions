class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Explore
        #the idea is to return true when you see a duplicate
        #CQ- Can the array be empty or None? If so you would return false right?

        #Brainstorm
        #Easiest way to do it, loop through and add each unique element to a set,
        #If the element is in the set already return True else if all the elements
        #get added to the set without fail i.e. you reach the end of the array without duplicates,
        #return False

        #Plan
        #What happens if the array is None? return False
        #Since we only need to find the first duplicate, 
        #we can return early when we find one element that doesn't fit the set

        #Implement
        nums_set = set()
        if not nums:
            return False
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False



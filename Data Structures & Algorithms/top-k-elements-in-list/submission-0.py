class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # so we need basically to list the unique elements in the array, count their frequancies and then return the k highest frequencies array

        # brute force, for each element we check the whole vector for duplicate and count and store this is O(n2) - we don't likey

        # the first idea that comes to my mind is to build a a hash with element->countand then sort efficiently the count vector, and return the k elements.

         # Counter creates easy a dic with that in O(n)

        c = Counter(nums)

        # then how do we sort it? 
        return [ x for x, _ in c.most_common(k)]
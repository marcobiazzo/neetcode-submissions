class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # so we need basically to list the unique elements in the array, count their frequancies and then return the k highest frequencies array

        # brute force, for each element we check the whole vector for duplicate and count and store this is O(n2) - we don't likey

        # the first idea that comes to my mind is to build a a hash with element->countand then sort efficiently the count vector, and return the k elements.

         # Counter creates easy a dic with that in O(n)

        c = Counter(nums)

        # we are now trying not to use the most common, and sorting count in O(n), remember that a comparing sort is minimum O(nlogn), so we need to resort to something different. A suggestion is to use the count itself as an index, so if we store it in like a dic, storing it will be O(n) and the sorting will be free (I have still no idea how). 

        # Lets first think about the right key to store the count, it has to be a tuple since it is the only multi value type that can be a key and we definitely need that since different numbers can have the same count.
        # in the tuple we will encode also the number itself - how?
        # It's a given that the count's number can be maximum len(nums)

        # option 1: can we store it actually in a single number? I believe the bucket's hashes will be monotone since the keys are actual numbers, so if we combine the key + count but then it will be hard to decompose them after
        # Option 2: let's think about the tuple option, we store (num, count) as key of a dictionary right? then how do we sort it? and get the biggest k?

        # create the list that has as index the number of times that specific number is repeated. This list can hold more that one element. We will loop the counter and fill the list up in teh appropriate index
        l = [[] for _ in range(len(nums) + 1)]

        # for loop on the counter c
        for num, cnt in c.items():
            l[cnt].append(num)
        
        elem = 0 # count of elements added, stops at k
        result = []
        for i in range(len(l) - 1, 0, -1):
            if l[i]:
                elem += len(l[i])
                result.extend(l[i])
            if elem >= k: 
                break

        # then how do we sort it? 
        return result
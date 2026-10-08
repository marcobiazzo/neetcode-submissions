class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # So just to recap last times we have been finding if 2 words are anagrams by creating a dic for each word that has one column the letter and the other the number of times it appears if the dics are the same then the words are anagrams. We have been working on that and proved that that is O(1). 
        # Were there more efficient ways? i rememebr the se, if we create a set with the word, what is it stored in the set? the set is a dic with no value only key, but in this case we need both. 

        # We had a super fast way to check that that was Counter(s) or somethign like that that creates a dic already? yes it's Counter(s) how can we use that? Lets go back to that in a second

        # Our problem brute force if we assume that counter() is O(1) would be to check each element in the input with every other element and add them to the anagram list if they are anagrams. This would have complexity O(n2). We can start by applying that. No smart ideas come to mind right now let's do the scrppy version

        anagrams = []
        dic = {}
        for s in strs:   
            
            # build the list (then tuple bc immutable) 
            count = [0] * 26
            for l in s:
                count[ord(l)-ord('a')] += 1
            
            # we have one key per anagram
            key = tuple(count)
            if key in dic:
                dic[key].append(s)
            else:
                dic[key]=[s]

        return list(dic.values())

# ok this should work, let's think about the edge case exaple 3 empty string

# ok now we should solve the efficiency problem, the code is too slow. 
# So is possible to 

# I think the worst thing about this is that we build a counter n2 times - that give a complecity of actually n (k) because building a counter is O(k). But here the problem is the n2, because we are going to deal with long ass string lists 

# Can we do it in one pass?

        
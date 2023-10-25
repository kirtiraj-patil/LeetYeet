import queue

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        if not s:
            return 0

        d = {}
        q = queue.Queue()
        currentLength = 0

        for c in s:
            if c in d:
                if maxLength < currentLength:
                    maxLength = currentLength
                
                removeUntil = q.get()
                d.pop(removeUntil)
                while removeUntil != c:
                    removeUntil = q.get()
                    d.pop(removeUntil)
                
                currentLength = len(q.queue)

            q.put(c)
            d[c] = 0
            currentLength += 1

        if maxLength < currentLength:
            maxLength = currentLength
        
        return maxLength


            

            
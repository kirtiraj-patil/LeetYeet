class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        self.heights = heights
        self.names = names
        self.quickSort(0, len(heights) - 1)
        return names

    def quickSort(self, start, end):
        if start >= end:
            return
        pivot = self.heights[end]
        i = start - 1
        j = start
        while j < end:
            if self.heights[j] > pivot:
                i += 1
                self.heights[i], self.heights[j] = self.heights[j], self.heights[i]
                self.names[i], self.names[j] = self.names[j], self.names[i]

            j += 1

        i += 1
        self.heights[i], self.heights[end] = self.heights[end], self.heights[i]
        self.names[i], self.names[end] = self.names[end], self.names[i]
        self.quickSort(start, i - 1)
        self.quickSort(i + 1, end)

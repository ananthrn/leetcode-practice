class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # cache = dict()
        @cache
        def backtrack(bookIndex: int, currentShelfHeight: int, remainingWidth: int) -> int:
            if remainingWidth < 0:
                return math.inf
            if bookIndex == len(books):
                return currentShelfHeight
            
            # if (bookIndex, currentShelfHeight, remainingWidth) in cache:
            #     return cache[(bookIndex, currentShelfHeight, remainingWidth)]

            bookWidth, bookHeight = books[bookIndex]
            sameShelfHeight = backtrack(bookIndex + 1, max(currentShelfHeight, bookHeight), remainingWidth - bookWidth)
            nextShelfHeight = currentShelfHeight + backtrack(bookIndex + 1, bookHeight, shelfWidth - bookWidth)
            # print("bookIndex, currentShelfHeight, remainingWidth: ", bookIndex, currentShelfHeight, remainingWidth)
            # print("Answer: ", min(sameShelfHeight, nextShelfHeight))

            # cache[(bookIndex, currentShelfHeight, remainingWidth)] = min(sameShelfHeight, nextShelfHeight)
            return min(sameShelfHeight, nextShelfHeight)

        ans = backtrack(0, 0, shelfWidth)

        print("Cache Info: ", backtrack.cache_info())
        return ans
        
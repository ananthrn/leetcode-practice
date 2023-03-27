# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def getHostName(url: str) -> str:
            return url.split("/")[2]
        
        Q = collections.deque([startUrl])
        seen = set()

        urlList = []

        mainHostName = getHostName(startUrl)

        while len(Q) > 0:
            tp = Q.pop()
            # print("tp: ")
            # print("getHostName of tp: ", getHostName(tp))
            if tp not in seen:
                seen.add(tp)
                urlList.append(tp)

                for nextUrl in htmlParser.getUrls(tp):
                    if nextUrl not in seen and getHostName(nextUrl) == mainHostName:
                        Q.appendleft(nextUrl)

        return urlList
#
# @lc app=leetcode id=535 lang=python3
#
# [535] Encode and Decode TinyURL
#

# @lc code=start
import random
import string


class Codec:
    alphabets = string.ascii_letters + '0123456789'
    urlToCode = {}
    codeToUrl = {}
  
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while longUrl not in self.urlToCode:
            code = ''.join(random.choice(self.alphabets) for _ in range(6))
            if code not in self.codeToUrl:
                self.codeToUrl[code] = longUrl
                self.urlToCode[longUrl] = code
        return 'http://tinyurl.com/' + self.urlToCode[longUrl]


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.codeToUrl[shortUrl[-6:]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end


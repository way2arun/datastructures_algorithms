"""
Encode and Decode TinyURL
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

"""
from random import choices, random


class Codec:
    def __init__(self):
        # Solution 1 - 28 ms
        """
        self.long_short = {}
        self.short_long = {}
        self.alphabet = "abcdefghijklmnopqrstuvwzyz"
        """
        # Solution 2 - 16 ms
        self.db = {}
        self.prefix = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        # Solution 1 - 28 ms
        """
        while longUrl not in self.long_short:
            code = "".join(choices(self.alphabet, k=6))
            if code not in self.short_long:
                self.short_long[code] = longUrl
                self.long_short[longUrl] = code
        return 'http://tinyurl.com/' + self.long_short[longUrl]
        """
        # Solution 2 - 16 ms
        aux = longUrl.split("/")
        coded = str(len(aux))
        for s in aux:
            if len(s) > 0:
                coded += s[0]

        while coded in self.db:
            rand = chr(random.randint(65, 90))
            coded += rand

        self.db[coded] = longUrl
        return self.prefix + coded

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        # Solution 1 - 28 ms
        """
        return self.short_long[shortUrl[-6:]]
        """
        # Solution 2 - 16 ms
        key = shortUrl.split("/")[-1]
        if key in self.db:
            return self.db[key]


# Main Call
url = "https://leetcode.com/problems/design-tinyurl"
codec = Codec()
shortned_url = codec.encode(url)
print(shortned_url)
original_url = codec.decode(shortned_url)
print(original_url)
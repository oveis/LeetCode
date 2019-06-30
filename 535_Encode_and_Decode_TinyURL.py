class Codec:
    BASE_URL = 'http://tinyurl.com/'
    url_map = dict()
    
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        alphnumeric_list = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(alphnumeric_list) for _ in range(6))
        tiny_url = self.BASE_URL + random_string
        self.url_map[tiny_url] = longUrl
        return tiny_url
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.url_map[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

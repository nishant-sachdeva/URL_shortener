import pyshorteners

def generateShortUrl(longUrl):
	urlShortener = pyshorteners.Shortener()
	shortUrl = urlShortener.tinyurl.short(longUrl)
	return shortUrl
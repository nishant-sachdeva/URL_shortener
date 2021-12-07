from shorteners import generateShortUrl


if __name__ == '__main__':
	longURl = input("Please enter the URL you wish to shorten => ")
	shortUrl = generateShortUrl(longURl)
	print(shortUrl)


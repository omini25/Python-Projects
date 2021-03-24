import pyshorteners

url = input('Enter url to be shortened: ')
shortener = pyshorteners.Shortener()
shorts = shortener.tinyurl.short(url)
print(shorts)
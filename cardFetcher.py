import requests
from bs4 import BeautifulSoup


parsedCardName = ''
cardImg = ''
cardOracle = ''

def parseCardName(card):
	url = "+".join( card.split() )
	return url



cardName = raw_input("Which Card do you want the image for? ")
 
parsedCardName = parseCardName(cardName)



r = requests.get("http://magiccards.info/query?q=%21" + parsedCardName)
parsed = BeautifulSoup(r.text,'html.parser')

for image in parsed.find_all('img', {'height':445}):
	cardImg = image['src']
for name in parsed.find_all('p', {'class':'ctext'}):
	cardOracle = name.string


print cardImg
print '\n'
print cardOracle
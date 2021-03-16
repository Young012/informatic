from bs4 import BeautifulSoup
import requests

def parse():
	url = "https://tproger.ru/explain/how-cpu-works/"
	heads = {
	  'User-Agent': ''
	}
	
	# get html page
	response = requests.get(url, headers = heads)
	soup = BeautifulSoup(response.content, 'html.parser')
	
	# parsed content
	content = soup.find('div', class_ = 'entry-content')
	
	# get headings from page
	print( "headings: " )
	h2 = content.findAll('h2')
	
	for h in h2:
		print( h.get_text(strip = True) )
		
	h3 = content.findAll('h3')
	
	for h in h3:
		print( h.get_text(strip = True) )
		
	# get other text from page	
    
	
	print( "other text from page: " )
	
	p = content.findAll('p')
	
	for txt in p:
		print( txt.get_text(strip = True) )
		
parse()
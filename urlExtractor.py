from urllib import request,parse,error
import ssl
from bs4 import BeautifulSoup

def urlExtractor(url, https=None):
    
    # fake headers 

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

    # preparing the request 
    req = request.Request(url=url,headers=headers)


    if https is not None : resp = request.urlopen(req)
    else : 
        # ignore SSL certificate error
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        resp = request.urlopen(req,context=ctx)

    htmlPage = resp.read()
    soup = BeautifulSoup(htmlPage, 'html.parser')
    
    linkTags  = soup.find_all('a')

    #linkTags = list(filter(lambda e: 'i.reddit' in e ,linkTags))

    # TODO : test this part ans assure that it returns the good link to the image 
    for link in linkTags :
        if 'i.reddit' in link or 'preview' in link :
            print(link.get('href'))



urlExtractor('https://www.reddit.com/',https=True)

    
    

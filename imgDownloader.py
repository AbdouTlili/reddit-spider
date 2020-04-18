from urllib.request import  Request,urlopen
import urllib.error

import string, random


def randomStr(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

    

def imgDownload(url,name=None,path=None):

    # preparing the request with fake headers 
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    req = Request(headers=headers,url= url)
    '''
    fetching the url 
    '''
    imgBin = urlopen(req).read()

    '''
    saving the image file
    '''

    if name is None : name = randomStr() 

    with open(name,'wb') as f:
        f.write(imgBin)

    return name
    
imgDownload('https://miro.medium.com/max/1200/1*mk1-6aYaf_Bes1E3Imhc0A.jpeg')
print(randomStr())



from bs4 import BeautifulSoup
import cloudscraper

scraper = cloudscraper.create_scraper() # returns a CloudScraper instance

baseURL = 'https://readcomiconline.to'

def web_scraper(url):
    search_page = scraper.get(url)  # sends a GET request to the page

    soup = BeautifulSoup(search_page.content,'html.parser')

    div_id = soup.find(id = 'container') # finds the id
    return div_id

def info(self):
    thumb_list=[]

    url = baseURL + '/Search/Comic/' + self.title()

    data = web_scraper(url)
    tags = data.find_all('td') # img tag is contained in an atr of <td>
    for src in tags:
        try: # some elements did'nt had the 'title' atr
            l = []

            soup = BeautifulSoup(src['title'], 'html.parser')

            img = soup.find('img')
            p = soup.find('p')
            a = soup.find('a')

            if 'blogspot' not in img: # some links are not from readcomicsonline.to
                img = baseURL + img['src']

            l=[img, p.text.strip(), baseURL+a['href'], a.text]
            thumb_list.append(l)
        except:
            continue
    return thumb_list

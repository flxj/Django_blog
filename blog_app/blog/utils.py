#爬取图书图片
from blog_app.settings import MEDIA_ROOT
from bs4 import BeautifulSoup
import requests


def get_book_info(book_name):
    if not book_name:
        return "default_book.jpg", "佚名", "0000"
    #通过书名进行搜索，结果可能包含多个版本，简单取第一个结果
    search=requests.get("https://www.douban.com/search/",params={"q":book_name,"cat":1001}) #1001表示搜书，1002搜电影
    sop=BeautifulSoup(search.content,"html.parser")

    res=sop.find('div',attrs={'class':'result'})
    if not res:
        return "default_book.jpg","佚名", "0000"
    img_url=res.find('img')['src']
    if not img_url:
        return "default_book.jpg","佚名", "0000"
    img_name = img_url.split("/")[-1]
    img = requests.get(img_url)
    with open(MEDIA_ROOT + '/img/' + img_name, 'wb') as f:
        f.write(img.content)

    book_info=res.find('span',attrs={'class':"subject-cast"}).string
    auth_name=book_info.split('/')[0]
    pub_date=book_info.split('/')[-1]

    return img_name,auth_name,pub_date


#print(get_book_info("杀死一只知更鸟"))

def get_film_info(film_name):
    if not film_name:
        return "default_film.jpg", "卢米埃尔兄弟", "1895-12-28(巴黎首映)",'https://movie.douban.com/subject/1867742/'
    search = requests.get("https://www.douban.com/search/", params={"q": film_name, "cat": 1002})
    sop = BeautifulSoup(search.content, "html.parser")
    res = sop.find('div', attrs={'class': 'result'})
    if not res:
        return "default_film.jpg", "卢米埃尔兄弟", "1895-12-28(巴黎首映)",'https://movie.douban.com/subject/1867742/'

    #保存图片
    img_url = res.find('img')['src']
    if not img_url:
        return "default_film.jpg", "卢米埃尔兄弟", "1895-12-28(巴黎首映)",'https://movie.douban.com/subject/1867742/'
    img_name = img_url.split("/")[-1]
    img = requests.get(img_url)
    with open(MEDIA_ROOT + '/img/' + img_name, 'wb') as f:
        f.write(img.content)

    #获取其他信息
    film_url=res.find('a')['href']
    film=requests.get(film_url)
    soup = BeautifulSoup(film.content, "html.parser")
    film_info = soup.find('div', attrs={'id': 'info'})

    director=film_info.find('a',attrs={'rel':"v:directedBy"}).string
    release_date=film_info.find('span',attrs={'property':"v:initialReleaseDate"}).string

    return img_name, director,release_date,film_url

#print(get_film_info("肖申克的救赎"))
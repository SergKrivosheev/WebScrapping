import bs4
import requests
from fake_headers import Headers

URL = "https://habr.com/ru"
KEYWORDS = ['Python', 'Web', 'Сегодня', 'Дизайн', 'Samsung']
HEADERS = Headers(
    browser="chrome",
    os="win",
    headers=True
).generate()

response = requests.get(URL, headers=HEADERS)
text = response.text
soup = bs4.BeautifulSoup(text, features="html.parser")
articles = soup.find_all(class_='tm-articles-list__item')
for article in articles:
    flag = False #флаг о проверке - выводилось ли название статьи
    time = article.find('time').get('title')
    title = article.find('h2').find('span').text
    href = article.find('h2').find('a').get('href')

    # если слово встречается в заголовке
    for word_ in KEYWORDS:
        if word_ in title.split():
            flag = True
            print(f'{time} - {title} - {URL}{href}')
            break

    # поиск по хабам
    if flag == False:
        hubs = article.find_all(class_='tm-article-snippet__hubs-item')
        for hub in hubs:
            word_ = hub.find('a').find('span').text
            if word_ in KEYWORDS:
                flag == True
                print(f'{time} - {title} - {URL}{href}')
                break

    if flag == False:
        #если слово встречается в preview
        preview = article.find_all(class_=
            'article-formatted-body article-formatted-body article-formatted-body_version-2')
        for text_ in preview:
            text_ = text_.find('p').text.split()
            for word in text_:
                if word in KEYWORDS:
                    print(f'{time} - {title} - {URL}{href}')
                    break
import requests
from rich import print
from bs4 import BeautifulSoup


def parserr(domain):
    url = 'http://{}'.format(domain)
    req = requests.get(url)
    links = []
    if ('https' not in req.url):
        links = get_links(baseUrl=url, urls='/')
    else:
        url = "https://{}".format(domain)
        links = get_links(url, '/')
    return links


def get_links(baseUrl, urls):
    """
    Finding all links from the Website and appending them to list named initial_links
    """
    initial_links = []
    for i in urls:
        reqq = requests.get(baseUrl+i)
        soup = BeautifulSoup(reqq.text, "html.parser")
        link = soup.find_all('a', href=True)
        for i in link:
            if i['href'] == '#' or i['href'] == "":
                pass
            else:
                initial_links.append(i['href'])
    sorted_links = []
    for i in initial_links:
        if (i not in sorted_links):
            sorted_links.append(i)
    return sorted_links

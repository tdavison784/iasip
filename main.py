import requests
from bs4 import BeautifulSoup
import re
from models.format_csv import enter_data

base_url = "https://transcripts.foreverdreaming.org/"

episode_urls = ["https://transcripts.foreverdreaming.org/viewforum.php?f=104",
                "https://transcripts.foreverdreaming.org/viewforum.php?f=104&start=25",
                "https://transcripts.foreverdreaming.org/viewforum.php?f=104&start=50",
                "https://transcripts.foreverdreaming.org/viewforum.php?f=104&start=75",
                "https://transcripts.foreverdreaming.org/viewforum.php?f=104&start=100",
                "https://transcripts.foreverdreaming.org/viewforum.php?f=104&start=125"
                "https://transcripts.foreverdreaming.org/viewforum.php?f=104&start=150"]


def get_episode_names():
    """Function that gets episode names and returns a list of lists"""

    episode_urls = ["https://transcripts.foreverdreaming.org/viewforum.php?f=104",
                    "https://transcripts.foreverdreaming.org/viewforum.php?f=104&start=25",
                    "https://transcripts.foreverdreaming.org/viewforum.php?f=104&start=50",
                    "https://transcripts.foreverdreaming.org/viewforum.php?f=104&start=75",
                    "https://transcripts.foreverdreaming.org/viewforum.php?f=104&start=100",
                    "https://transcripts.foreverdreaming.org/viewforum.php?f=104&start=125"
                    "https://transcripts.foreverdreaming.org/viewforum.php?f=104&start=150"]

    soup_data = []
    for url in episode_urls:
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        soup_data.append(soup)

    episode_names_list = []
    for data in soup_data:
        episode_data = data.find('table', attrs={'class': 'tablebg'}).find_all('a')
        for x in episode_data:
            episode_names_list.append(x.text)

    return episode_names_list


def get_episode_hrefs():
    """Function that gets all episode hrefs and returns list"""

    episode_urls = ["https://transcripts.foreverdreaming.org/viewforum.php?f=104",
                    "https://transcripts.foreverdreaming.org/viewforum.php?f=104&start=25",
                    "https://transcripts.foreverdreaming.org/viewforum.php?f=104&start=50",
                    "https://transcripts.foreverdreaming.org/viewforum.php?f=104&start=75",
                    "https://transcripts.foreverdreaming.org/viewforum.php?f=104&start=100",
                    "https://transcripts.foreverdreaming.org/viewforum.php?f=104&start=125"
                    "https://transcripts.foreverdreaming.org/viewforum.php?f=104&start=150"]
    soup_data = []
    for urls in episode_urls:
        resp = requests.get(urls)
        soup = BeautifulSoup(resp.text, 'html.parser')
        soup_data.append(soup)

    episode_href_data = []
    for x in soup_data:
        for link in x.find('table', attrs={'class': 'tablebg'}).find_all('a', attrs={'href':
                                                                                        re.compile("^.\/viewtopic.*")}):
            episode_href_data.append(link.get('href'))

    return episode_href_data



def test():
    #This is how to get a episode season and name.
    resp = requests.get(url='https://transcripts.foreverdreaming.org/viewforum.php?f=104')
    soup = BeautifulSoup(resp.text, 'html.parser')
    data = soup.find('table', attrs={'class': 'tablebg'}).find_all('a')
    for x in data:
        print(x.text)


def main():



    hrefs = get_episode_hrefs()
    episodes = get_episode_names()

    seasons = []
    episode_names = []
    for name in episodes:
        seasons.append(name.split('-')[0])
        episode_names.append(name.split('-')[-1])

    combined_data = zip(hrefs, seasons, episode_names)

    new_data = []
    for href, season, ep_name in combined_data:
        data = [ep_name, season, base_url+href]
        new_data.append(data)

    enter_data(new_data)


if __name__ == '__main__':
    main()

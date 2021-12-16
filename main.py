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



    episode_data_list = []
    for data in soup_data:
        episode_data = data.find('table', attrs={'class': 'tablebg'}).find_all('a')
        episode_data_list.append(episode_data)

    for ep_data in episode_data_list:
        

    return episode_data_list


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



def main():



    hrefs = get_episode_hrefs()
    episodes = get_episode_names()


    combined_data = zip(hrefs, all_episodes)

    new_data = []
    for href, name in combined_data:
        print(f'{href}, {name[-1]}, {name[0]}')
        data = [name[-1], name[0], base_url+href]
        new_data.append(data)

    enter_data(new_data)


if __name__ == '__main__':
    main()

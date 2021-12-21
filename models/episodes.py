import requests
import re
from bs4 import BeautifulSoup
from models.format_csv import enter_data


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


def generate_csv():
    """Function that will create a csv file with all
    always sunny data."""

    base_url = "https://transcripts.foreverdreaming.org/"
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


def get_transcript_text(url):
    """Function to get all text from the transcripts"""

    transcript_data = {
        'damnits': [],
        'bitches': []
    }
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    data = soup.find('div', attrs={'class': 'postbody'}).find_all('p')
    find_words = ['God Dammit', 'god dammit', 'You Bitch', 'you bitch', 'Goddamn it', 'GodDamn it', 'goddamn it']
    for line in data:
        for word in find_words:
            if word in line.text:
                if word.__contains__('God') or word.__contains__('god'):
                    transcript_data['damnits'].append(line.text)
                elif word.__contains__('You Bitch') or word.__contains__('you bitch'):
                    transcript_data['bitches'].append(line.text)

    return transcript_data

from models.episodes import generate_csv, get_transcript_text, get_episode_names, get_episode_hrefs
import pandas as pd


def main():

    base_url = "https://transcripts.foreverdreaming.org/"
    # generate_csv()
    transcripts_list = []
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
    df = pd.DataFrame(new_data, columns=['name', 'season_episode', 'href'])

    for url in df['href']:
        transcript_text = get_transcript_text(url)
        print(transcript_text)



if __name__ == '__main__':
    main()

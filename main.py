from models.episodes import generate_csv, get_transcript_text, get_episode_names, get_episode_hrefs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

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

    all_swear_text = []
    for url in df['href']:
        all_swear_text.append(get_transcript_text(url))

    damnits_length = []
    bitches_length = []
    for text in all_swear_text:
        for k, v in text.items():
            if k == 'damnits':
                damnits_length.append(len(v))
            else:
                bitches_length.append(len(v))

    df['damnits'] = damnits_length
    df['bitches'] = bitches_length

    bar_width = 0.25
    fig = plt.subplots(figsize=(12, 8))

    br1 = np.arange(len(df['damnits']))
    br2 = [x + bar_width for x in br1]

    plt.bar(br1, df['damnits'], color='r', width=bar_width,
            edge_color='grey', label='Damnits')
    plt.bar(br2, df['bitches'], color='b', width=bar_width,
            edge_color='grey', label='bitches')

    plt.show()






    print(df)

if __name__ == '__main__':
    main()

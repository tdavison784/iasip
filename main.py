from models.episodes import generate_csv, get_transcript_text, get_episode_names, get_episode_hrefs
import pandas as pd
from models.format_csv import save_to_csv
import numpy as np
from pathlib import Path
import plotly.express as px
import plotly.io as pio
import matplotlib.pyplot as plt

def main():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    if Path('./always_sunny-data.csv').exists():
        df = pd.read_csv('./always_sunny-data.csv')

        df["name"].str.contains('|'.join('Read'))

        fig = px.bar(df, x='season_episode', y=['god_dammit', 'you_bitch'], height=400, barmode='group',
                     hover_data=['name', 'season_episode'])
        pio.write_html(fig, file='index.html', auto_open=True)

    else:
        base_url = "https://transcripts.foreverdreaming.org/"
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

        df['god_dammit'] = damnits_length
        df['you_bitch'] = bitches_length
        df["name"].str.contains('|'.join('Read'))

        df.to_csv('./always_sunny-data.csv')

        fig = px.bar(df, x='season_episode', y=['god_dammit', 'you_bitch'], height=400, barmode='group',
                     hover_data=['name', 'season_episode'])
        fig.show()


if __name__ == '__main__':
    main()

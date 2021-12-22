import csv
import pandas as pd
from pathlib import Path


def enter_data(data):
    """Function that enters data into csv sheet
    :param data: API data to enter into csv"""

    fields = ['name', 'season/episode', 'transcript_url']

    filename = 'always_sunny_data.csv'
    with open(filename, 'w+') as csv_obj:
        csv_writer = csv.writer(csv_obj)

        # Create the feild names
        csv_writer.writerow(fields)

        csv_writer.writerows(data)
    csv_obj.close()


def save_to_csv(dataframe, filename, dest, column_names):
    """Function that saves a data frame to a csv file"""

    if Path(dest+filename).exists():
        return "File already exists"
    else:
        Path(dest).mkdir()
        dataframe.to_csv(dest+filename, columns=column_names)
import csv


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

from models.episodes import generate_csv, get_transcript_text


def main():

    generate_csv()

    print(get_transcript_text('https://transcripts.foreverdreaming.org/./viewtopic.php?f=104&t=15474&sid=35a4d5ff291e5886458e3568bca76797'))


if __name__ == '__main__':
    main()

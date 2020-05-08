import json
from youtube_transcript_api import YouTubeTranscriptApi, _errors
from csv_reader import FileExplorer
from normalizer import stop_words_removal, UkrainianStemmer


def collect_data():
    """
    () -> ()
    Saves all files with subtitles in 'data' folder
    """
    file = FileExplorer()
    ids = file.id_retriever()
    for i in ids:
        if i != 'NaN':
            try:
                f = f'data/{i}.json'
                transcript_list = YouTubeTranscriptApi.list_transcripts(i)
                transcript = transcript_list.find_transcript(['uk'])
                if not transcript.is_generated:
                    with open(f, 'w', encoding='utf-8') as f:
                        data = data_cleaner(
                            YouTubeTranscriptApi.get_transcripts([i], languages=['uk']))
                        json.dump(data, f, ensure_ascii=False)
            except _errors.NoTranscriptFound:
                continue
            except _errors.VideoUnavailable:
                continue
            except _errors.TranscriptsDisabled:
                continue


def data_cleaner(f):
    """
    () -> ()
    Returns a file with clean information
    """
    text = []
    for line in f[0]:
        for i in f[0][line]:
            i['text'] = i['text'].replace('\n', ' ')
            text += [i['text']]
    text = ' '.join(text)
    text = stop_words_removal(text)
    for word in range(len(text)):
        text[word] = UkrainianStemmer(text[word]).stem_word()
    text = ' '.join(text)
    f[0][line] = text
    return f


if __name__ == '__main__':
    collect_data()

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def print_word_freq(file):
    words_count = {}

    with open(file) as open_file:
        text = open_file.read()
        
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for ele in text:
            if ele in punctuations:
                text = text.replace(ele, "")
        text = text.replace("\n", " ")
        

        text =text.lower()
        text_list = text.split()
        text_list_copy = text_list.copy()
        

        for word in text_list:
            if word in STOP_WORDS:
                text_list_copy.remove(word)
            elif word not in words_count:
                unsorted_count = text_list_copy.count(word)
                words_count[word] = unsorted_count

        sorted_count = sorted(words_count.values(), reverse=True)
        sorted_dictionary = {}
        for index in sorted_count:
            for k in words_count.keys():
                if words_count[k] == index:
                    sorted_dictionary[k] = words_count[k]
        print(sorted_dictionary)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

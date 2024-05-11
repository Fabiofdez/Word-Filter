import argparse
import re
import random


def read_default():

    with open("data/default.txt") as f:
        content = f.read()
        words = content.split()
        sentences = content.split(".")
        words.sort()
        f.close()

    return words, sentences



def read_from_files(files: str):

    def freq_word(line): 
        sep = line.split("\t")
        return (sep[1], int(sep[2]))
  
    with open(f"data/{files}/{files}-words.txt") as wf:
        lines = wf.readlines()
        words = [freq_word(line) for line in lines]

    with open(f"data/{files}/{files}-sentences.txt") as sf:
        sentences = [line.split("\t")[1] for line in sf.readlines()]

    return words, sentences



def filter_by_substr(words: list, substr: str):

    filtered: dict[str, int] = {}
    
    if isinstance(words[0], tuple):
        filtered: list[str] = []

        for word, _ in words:

            if substr in word:
                filtered.append(word)

    else:
        for word in words:

            if substr not in word:
                continue

            if (word not in filtered):
                filtered[word.lower()] = 1
            else:
                filtered[word.lower()] += 1

        filtered = {k: v for k, v in sorted(filtered.items(), key=lambda item: item[1])}
        filtered: list[str] = list(reversed(filtered.keys()))

    return filtered



def get_small_corpus_with(word_list: list[str], sent_list: list[str]):

    small_corpus: list[str] = []

    for word in word_list:
        for sentence in sent_list:

            if f" {word.lower()} " in f" {sentence.lower()} ":
                small_corpus.append(sentence)
                break

        if len(small_corpus) == len(word_list):
            break

    return small_corpus



def clean_up_corpus(corpus: list[str]):

    joined_corpus = ". ".join(corpus) + "."
    clean_corpus = re.sub(r"[^a-zA-ZáéíóúüÁÉÍÓÚÜñÑ.\s-]", '', joined_corpus)
    clean_corpus = re.sub(r'(\s*\.\s*)+', '. ', clean_corpus)
    clean_corpus = re.sub(r'^[^A-Za-z"\'¿¡«\(\[{\u2018\u201C]+', '', clean_corpus)

    return re.sub(r'\s+', ' ', clean_corpus)



def clean_up(word: str):
    clean_word = re.sub(r"[^a-záéíóúüñ-]", '', word.lower())
    return re.sub(r'\s+', ' ', clean_word)



def run_filter():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--files", default=None)
    parser.add_argument("-s", "--substring", required=True)
    parser.add_argument("-c", "--count", default=5)
    parser.add_argument("-p", "--print-sample", action="store_true")

    args = parser.parse_args()

    # Define the substring to filter, number of words
    substr = args.substring
    num_words = int(args.count)
    file_dir = args.files
    print_sample = args.print_sample

    words, sentences = read_from_files(file_dir) if (file_dir is not None) else read_default()

    filtered = filter_by_substr(words, substr)

    if len(filtered) == 0:
        print(f"\n(!!!) Found no words with \"{substr}\"\n")
        return

    if len(filtered) < num_words:
        word_noun = "word" if len(filtered) == 1 else "words"
        print(f"\n(!) Found only {len(filtered)} {word_noun} with \"{substr}\"")
        num_words = min(num_words, len(filtered))

    # get lists of words
    most_freq_words = filtered[:num_words]
    rand_selection = random.sample(filtered, k=num_words)

    print(f"\nTop {num_words} most frequent words with \"{substr}\":")
    for word in filtered[:num_words]:
        print(" >", clean_up(word))

    print(f"\nRandom selection of {num_words} words with \"{substr}\":")
    for word in rand_selection:
        print(" >", clean_up(word))
    
    print()
    
    # generate corpora
    if print_sample:

        small_corpus1 = get_small_corpus_with(most_freq_words, sentences)
        small_corpus2 = get_small_corpus_with(rand_selection, sentences)

        small_corpus1 = clean_up_corpus(small_corpus1).strip()
        small_corpus2 = clean_up_corpus(small_corpus2).strip()

        print("\nCorpus 1 (most-frequent):\n")
        print(small_corpus1, "\n")
        print("\nCorpus 2 (random):\n")
        print(small_corpus2, "\n")

run_filter()

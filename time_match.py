import wordobjectforfiletranscript import Word,
def time_match(sentences, words):
    response = {}
    while len(ordered_word) != 0:
        ordered_pair = words.popleft()
        word = ordered_pair.getWord()
        sentence = sentences.popleft()
        sentence_array = sentence.split()
        response[sentence] = ordered_pair.getTime()
        for i in range(len(sentence_array)):
            words.popleft()

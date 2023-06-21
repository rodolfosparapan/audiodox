from files import reader as file_reader

start_rec_words = file_reader.get_string_array_from_file("files/start_words.txt")
stop_rec_words = file_reader.get_string_array_from_file("files/stop_words.txt")

def search_for_starter_keyword(word):
    for start_rec_word in start_rec_words:
        if start_rec_word.lower() in word.lower():
            return start_rec_word
    return ""

def search_for_stop_keyword(word):
    for stop_rec_word in stop_rec_words:
        if stop_rec_word.lower() in word.lower():
            return stop_rec_word
    return ""

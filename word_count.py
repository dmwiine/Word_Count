def words(word):
    word_list = word.split()  # Spliting the word
    word_dict = {}             # Initialise empty dictionary to hold the word count
    for wrd in word_list:
        counter = 0
        if wrd not in word_dict:
            repeat = 0
            while counter < len(word_list):

                if str(wrd) == str(word_list[counter]):
                    repeat += 1

                counter += 1
            if wrd.isdigit():
                word_dict.update({int(wrd): int(repeat)})
            else:
                word_dict.update({wrd: int(repeat)})
    return word_dict

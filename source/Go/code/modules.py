import re


def delete_punctuations(text):
    text = re.sub('[-=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`…》]', '', text)
    return text


def to_lower_case(text):
    return text.lower()


def make_stop_words_ls(df, group_ls):
    stop_word_ls = []
    for i in group_ls:
        group_name = 'group_'+str(i)
        stop_word_ls.extend(df[group_name].dropna().unique().tolist())
    return stop_word_ls


def remove_stop_words(df, stop_words):
    for i in stop_words:
        try:
            del df[i]
        except:
            pass
    return df

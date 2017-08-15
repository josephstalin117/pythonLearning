import requests
import re
from bs4 import BeautifulSoup
import string


def parser_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find('div', 'post-content').getText().encode('utf-8')
    return content


def remove_punctuation(content):
    for c in string.punctuation:
        content = content.replace(c, "")
    return content


def frequency(list):
    dict = {}
    for idx, val in enumerate(list):
        if val in dict:
            dict[val] += 1
        else:
            dict[val] = 1
    return dict


def stats(list):
    dict = {}
    for idx, val in enumerate(list):
        if idx + 1 != len(list):
            next_word = list[idx + 1]
        else:
            next_word = ""
        if val in dict:
            dict[val].append(next_word)
        else:
            dict[val] = [next_word]
    for i in dict:
        dict[i] = max(set(dict[i]), key=dict[i].count)
    return dict


if __name__ == '__main__':
    html = requests.get('http://josephstalin117.github.io/essay/2017/08/14/gettysburg-address.html')
    content = parser_html(html.content)
    content = remove_punctuation(content)
    list = content.split()
    print list
    print len(list)
    word_count = frequency(list)
    print word_count
    next_word = stats(list)
    print next_word
    print len(next_word)

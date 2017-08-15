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


def stats(list):
    dict = {}
    for i in list:
        if (list.index(i)) + 1 != len(list):
            dict[i] = list[list.index(i) + 1]
        else:
            dict[i] = ""
    return dict


if __name__ == '__main__':
    html = requests.get('http://josephstalin117.github.io/essay/2017/08/14/gettysburg-address.html')
    content = parser_html(html.content)
    content = remove_punctuation(content)
    list=content.split()
    print list

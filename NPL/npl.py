import requests
import re
from zhon.hanzi import punctuation
import string
import jieba
from collections import Counter


def parser_html(html):
    items = re.findall(ur'<p>.*</p>', html.content)
    content = ""
    for i in items:
        i = re.sub(ur"[%s%s]+" % (punctuation, string.punctuation), "", i.decode('utf-8'))
        i = re.sub(ur"[a-z]", "", i)
        content += i[3:-4]
    return content


def cut(text):
    list = jieba._lcut(text)
    return [x.encode('utf-8') for x in list]


def stats(list):
    dict = {}
    for i in list:
        if (list.index(i)) + 1 != len(list):
            dict[i] = list[list.index(i) + 1]
        else:
            dict[i] = ""
    return dict


if __name__ == '__main__':
    text = requests.get('http://china.huanqiu.com/article/2017-08/11108469.html?from=bdwz')
    content = parser_html(text)
    print content
    list = cut(content)
    # for i in list:
    #     print i
    # dict = Counter(list)
    # for i in dict:
    #     print i
    #     print dict[i]
    worddict = stats(list)
    print "***************************"

    for k, v in worddict.iteritems():
        print k+" "+v

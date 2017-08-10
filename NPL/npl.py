import requests
import re
from zhon.hanzi import punctuation
import string


def parser_html(html):
    items = re.findall(ur'<p>.*</p>', html.content)
    content = ""
    for i in items:
        i=re.sub(ur"[%s%s]+" %(punctuation,string.punctuation), "", i.decode('utf-8'))
        # i=re.sub(ur"[%s]+" %string.punctuation, "", i)
        content += i[3:-4]
    return content

if __name__ == '__main__':
    text = requests.get('http://china.huanqiu.com/article/2017-08/11108469.html?from=bdwz')
    content = parser_html(text)
    print content

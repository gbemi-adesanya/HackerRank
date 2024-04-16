"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem
"""

from html.parser import HTMLParser

class MyHTMLParser (HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for element in attrs:
            print("-> {} > {}".format(element[0], element[1]))

if __name__ == "__main__":
    n = int(input())
    html = '\n'.join([input() for x in range(0, n)])  
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()

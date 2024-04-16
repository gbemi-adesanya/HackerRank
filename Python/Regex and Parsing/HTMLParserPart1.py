"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/html-parser-part-1/problem
"""

from html.parser import HTMLParser

if __name__ == "__main__":
    n = int(input())
    
    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            print("Start :", tag)
            for element in attrs:
                print("->", element[0], ">", element[1])
        
        def handle_endtag(self, tag):
            print("End   :", tag)
            
        def handle_startendtag(self, tag, attrs):
            print("Empty :", tag)
            for element in attrs:
                print("->", element[0], ">", element[1])
            
    parser = MyHTMLParser()
    for _ in range(n):
        line = input().strip()
        parser.feed(line)

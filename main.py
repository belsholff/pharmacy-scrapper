import sys
from scrap.websites.pacheco import Pacheco

def main():
    pachecoObj = Pacheco("https://www.drogariaspacheco.com.br/")
    pachecoObj.scrap("ramipril 5mg")

if __name__ == '__main__':
    main()

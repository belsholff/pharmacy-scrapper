from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import sys

from scrap.prototype import WebSite

class Pacheco(WebSite):
    """
    Definition: Scrapping Pacheco pharmacy website looking for a medicine price
    """

    def __init__(self, url):
        super(Pacheco, self).__init__(url)
        self.testing = False

    def scrap(self, product, **kwargs):
        try:
            if self.testing is True:
                browser = webdriver.Firefox()
            else:
                opt = Options()
                opt.add_argument('--headless')
                browser = webdriver.Firefox(options=opt)

            browser.get(self.url)

            searchBox = browser.find_element_by_css_selector(".busca > input")
            searchBox.send_keys(product.upper() + Keys.RETURN)

            WebDriverWait(browser, 10).until(
                EC.title_contains(product.upper()),
                message="Não foi possível obter os resultados de {} na {}".format(product.upper(), self.__class__.__name__)
            )

            searchResults = WebDriverWait(browser, 10).until(
                lambda tree: tree.find_elements_by_css_selector(".prateleira.vitrine.default .prateleira.vitrine.default ul li"),
                message="Não foi possível retirar os dados de {} na ".format(product.upper(), self.__class__.__name__)
            )

            for item in searchResults:
                medName = item.find_element_by_css_selector(".collection-link").text
                itemUrl = item.find_element_by_css_selector(".collection-link").get_attribute("href")
                fee = item.find_element_by_css_selector(".valor-por span").text
                print("====================")
                print(medName)
                print(itemUrl)
                print(fee)

        except Exception as e:
            print(e, file=sys.stderr)
        finally:
            browser.quit()

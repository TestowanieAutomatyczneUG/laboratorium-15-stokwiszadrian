import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='../../drivers/chromedriver')
        self.driver.implicitly_wait(10)
        self.driver.get("https://mfi.ug.edu.pl/")

    def test_links_count(self):
        links = self.driver.find_elements(by="xpath", value="//a")
        # print(len(links))
        self.assertTrue(len(links) >= 0)

    def test_images_count(self):
        images = self.driver.find_elements(by="xpath", value="//img")
        # print(len(images))
        self.assertTrue(len(images) >= 0)

    def test_in_and_out(self):
        links = self.driver.find_elements(by="xpath", value="//a[contains(@href, '')]")
        time.sleep(1)
        for a in range(0, len(links)):
            newlinks = self.driver.find_elements(by="xpath", value="//a[contains(@href, '')]")
            if newlinks[a].get_dom_attribute("href") is None:
                break
            for i in range(0, 2):
                try:
                    self.driver.execute_script("arguments[0].click()", self.driver.find_element(by="xpath", value=f"//a[@href=\'{newlinks[a].get_dom_attribute('href')}\']"))
                    self.driver.get("https://mfi.ug.edu.pl/")
                    break
                except StaleElementReferenceException as ex:
                    print(ex)
        self.assertTrue(len(links) >= 0)

    def test_inputs_count(self):
        form = self.driver.find_element(by="xpath", value="//form")
        inputs = form.find_elements(by="xpath", value=".//input")
        # print(len(inputs))
        self.assertTrue(len(inputs) >= 0)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
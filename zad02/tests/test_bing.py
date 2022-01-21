import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MyTestCase(unittest.TestCase):
    def test_first_result(self):
        driver = webdriver.Chrome(executable_path='../../drivers/chromedriver')
        driver.implicitly_wait(10)
        driver.get("https://bing.com/")
        driver.find_element(by="id", value="sb_form_q").send_keys("BDD")
        driver.find_element(by="id", value="sb_form_go").submit()

        # przechowujemy listę resultatów w zmiennej results, wybieramy 1szy, znajdujemy w nim link i klikamy go

        results = driver.find_elements(by="class name", value="b_algo")
        first = results[0].find_element(by="tag name", value="a")
        first.click()

        self.assertEqual(driver.title, "Behavior-driven development – Wikipedia, wolna encyklopedia")
        driver.quit()

    def test_third_result(self):
        driver = webdriver.Chrome(executable_path='../../drivers/chromedriver')
        driver.implicitly_wait(10)
        driver.get("https://bing.com/")
        driver.find_element(by="id", value="sb_form_q").send_keys("BDD")
        driver.find_element(by="id", value="sb_form_go").submit()
        results = driver.find_elements(by="class name", value="b_algo")
        third = results[2].find_element(by="tag name", value="a")
        third.click()
        h1 = driver.find_element(by="class name", value="section-jpro").find_element(by="tag name", value="h1").text
        self.assertEqual(h1, "Testy BDD – czy naprawdę są potrzebne?")
        driver.quit()

    def test_different_click(self):
        driver = webdriver.Chrome(executable_path='../../drivers/chromedriver')
        driver.implicitly_wait(10)
        driver.get("https://bing.com/")
        driver.find_element(by="id", value="sb_form_q").send_keys("BDD")
        driver.find_element(by="id", value="sb_form_go").submit()
        results = driver.find_elements(by="class name", value="b_algo")
        second = results[1].find_element(by="partial link text", value="What is BDD")

        # wysłanie przycisku RETURN = click()
        second.send_keys(Keys.RETURN)

        self.assertEqual(driver.title, "What is BDD (Behavior Driven Development)? | Agile Alliance")
        driver.quit()

    def test_element_not_found_try_except(self):
        driver = webdriver.Chrome(executable_path='../../drivers/chromedriver')
        driver.implicitly_wait(10)
        driver.get("https://bing.com/")

        # 1. blok try - except

        try:
            driver.find_element(by="id", value="sb_form_q").send_keys("BDD")
            driver.find_element(by="id", value="sb_form_go").submit()
            results = driver.find_elements(by="class name", value="b_algo")
            second = results[1].find_element(by="partial link text", value="What is BDD")

            # second = results[1].find_element(by="partial link text", value="jajecznica")

            second.send_keys(Keys.RETURN)
        except Exception as ex:
            print(ex)
        self.assertEqual(driver.title, "What is BDD (Behavior Driven Development)? | Agile Alliance")
        driver.quit()

    def test_element_not_found_list(self):
        driver = webdriver.Chrome(executable_path='../../drivers/chromedriver')
        driver.implicitly_wait(10)
        driver.get("https://bing.com/")
        driver.find_element(by="id", value="sb_form_q").send_keys("BDD")
        driver.find_element(by="id", value="sb_form_go").submit()
        results = driver.find_elements(by="class name", value="b_algo")

        # find_elements zwróci pustą listę w przypadku, gdy element nie zostanie znaleziony - nie wyrzuci wyjątku
        # second = results[1].find_elements(by="partial link text", value="jajecznica")

        second = results[1].find_elements(by="partial link text", value="What is BDD")
        second[0].send_keys(Keys.RETURN)
        self.assertEqual(driver.title, "What is BDD (Behavior Driven Development)? | Agile Alliance")
        driver.quit()


if __name__ == '__main__':
    unittest.main()
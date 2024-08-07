from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class MySeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)
        cls.browser = cls.selenium

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_title(self):
        self.browser.get(f"{self.live_server_url}/")
        page_title = self.selenium.title
        self.assertEqual(page_title, "Yassine | Portfolio")
    
    def test_check_projects_btn(self):
        self.browser.get(f"{self.live_server_url}/#projects")
        original_window = self.browser.current_window_handle

        btns = self.browser.find_elements(By.CLASS_NAME, "project-link")
        btns[0].click()
        btns[1].click()
        
        tabs = self.browser.window_handles[1:]

        self.browser.switch_to.window(tabs[0])
        self.assertEqual("https://github.com/fulanii/flask-auth-project", self.browser.current_url) 

        self.browser.switch_to.window(tabs[1])
        self.assertEqual("https://github.com/fulanii/rest-api-project", self.browser.current_url) 
    
    def test_my_links_page(self):
        self.browser.get(f"{self.live_server_url}/")
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        all_links = self.browser.find_element(By.CLASS_NAME, "footer__link")
        all_links.click()
        self.assertEqual("Yassine | Links", self.browser.title) 
  
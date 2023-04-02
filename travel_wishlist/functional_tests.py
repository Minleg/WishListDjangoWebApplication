from selenium.webdriver.chrome.webdriver import WebDriver

from selenium.webdriver.common.by import By

from django.test import LiveServerTestCase

class TitleTest(LiveServerTestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)
        
    @classmethod
    def tearDownClass(cls) -> None:
        cls.selenium.quit()
        super().tearDownClass()
        
    def test_title_on_home_page(self):
        self.selenium.get(self.live_server_url)
        self.assertIn('Travel Wishlist', self.selenium.title)
        
class AddPlacesTest(LiveServerTestCase):
    
    fixtures = [ 'test_places' ]
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)
        
    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
        
    def test_add_new_place(self):
        
        self.selenium.get(self.live_server_url)
        input_name = self.selenium.find_element(By.ID,'id_name') # id of the form input
        input_name.send_keys('Denver') # types Denver

        add_button = self.selenium.find_element(By.ID, 'add-new-place') # id of the Add place button
        add_button.click() # clicks the button
        
        denver = self.selenium.find_element(By.ID, 'place-name-5') # test has place until id 4 and expects Denver with next id which is 5
        self.assertEqual('Denver', denver.text)
        
        self.assertIn('Denver', self.selenium.page_source)
        self.assertIn('New York', self.selenium.page_source)
        self.assertIn('Tokyo', self.selenium.page_source)
        
        
        
        
     
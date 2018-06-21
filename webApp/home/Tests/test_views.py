from django.test import TestCase
from home.models import MissingPerson,FoundPerson

from django.core.urlresolvers import reverse

from home.models import User,MissingPerson,FoundPerson
from django.utils import timezone
from django.core.urlresolvers import reverse
from home.views import missingDetails,foundDetails
from home.forms import FoundPerson,MissingPerson,User,UserForm,FoundForm,MissingForm,forms


def test_home_list_view(self):
    w = self.create_home()
    url = reverse("home.views.home")
    resp = self.client.get(url)

    self.assertEqual(resp.status_code, 200)
    self.assertIn(w.title, resp.content)







# views (uses selenium)
import unittest
from selenium import webdriver

from home.views import MissingForm

class fprofilecreatetest (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_Report_Missing_Form_fire(self):
        self.driver.get("http://localhost:8000/logedin/addfound/")
        self.driver.find_element_by_id('title').send_keys("test title")
        self.driver.find_element_by_id('body').send_keys("test body")
        self.driver.find_element_by_id('foundIn').send_keys("test found")
        self.driver.find_element_by_id('loc').send_keys("cairo")
        self.driver.find_element_by_id('FoundDate').send_keys("2/5/2015")
        self.driver.find_element_by_css_selector("input[id='Male']").click()
        self.driver.find_element_by_id('file - upload').click()
        self.driver.find_element_by_id('Details').send_keys("ca,fnwlnw;glngpweg wew iro")
        self.driver.find_element_by_id('login').send_keys("D:\myfile.jpg")

        self.assertIn("http://localhost:8000/", self.driver.current_url)

    def tearDown(self):
        self.driver.quit

    if __name__ == '__main__':
        unittest.main()


class mprofilecreatetest (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_Report_Missing_Form_fire(self):
        self.driver.get("http://localhost:8000/logedin/addmissing/")
        self.driver.find_element_by_id('title').send_keys("test title")
        self.driver.find_element_by_id('body').send_keys("test body")
        self.driver.find_element_by_id('id_Sex').send_keys("cairo")
        self.driver.find_element_by_id('id_SecondName').send_keys("menna ")
        self.driver.find_element_by_id('id_DateOfBirth').send_keys("2/5/2015")
        self.driver.find_element_by_id('id_Weight').send_keys("80")
        self.driver.find_element_by_id('id_FirstName').send_keys("cairo")
        self.driver.find_element_by_id('id_RelativeRelation').send_keys("ommoh ")
        self.driver.find_element_by_id('id_AgeBeforeMissing').send_keys("20")
        self.driver.find_element_by_id('id_EyesColour').send_keys("fushia")
        self.driver.find_element_by_id('id_MissingFrom').send_keys("el 3ezbaah ")

        self.driver.find_element_by_id('id_Height').send_keys("150")
        self.driver.find_element_by_id('id_RelativeID').send_keys("150")
        self.driver.find_element_by_id('id_MissingDate').send_keys("20/5/2015")
        self.driver.find_element_by_id('id_HairColour').send_keys("fushia")
        self.driver.find_element_by_id('id_MissingPersonImage').send_keys("D:\myfile.jpg")
        self.driver.find_element_by_id('login').click()

        self.assertIn("http://localhost:8000/", self.driver.current_url)

    def tearDown(self):
        self.driver.quit

    if __name__ == '__main__':
        unittest.main()
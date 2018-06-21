from django.test import TestCase
from django.contrib.auth import get_user_model

from home.models import User, FoundPerson, MissingPerson
from home.forms import UserForm, MissingForm, FoundForm


class UserFormTest(TestCase):

    def setUp(self):
        # form = UserForm()
        self.user = User.objects.create(username="Turanga Leela", email="leela@example.com",
                                        password="Hi there")

    def test_Password_field_label(self):
        self.user = User.objects.create(Password='235ccfg6hkiism')
        self.assertEquals(UserForm.Password, '235ccfg6hkiism')

    def test_valid_form(self):
        mp = User.objects.create(title='Login Form', body='Bar')
        data = {'title': mp.title, 'body': mp.body, }
        form = UserForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        w = User.objects.create(title='Login Form', body='')
        data = {'title': w.title, 'body': w.body, }
        form = UserForm(data=data)
        self.assertFalse(form.is_valid())

    def test_valid_data(self):
        form = UserForm({
            'username': "Turanga Leela",
            'email': "leela@example.com",
            'password': "Hi there",
        })

        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEqual(user.name, "Turanga Leela")
        self.assertEqual(user.email, "leela@example.com")
        self.assertEqual(user.password, "Hi 2513698514258there")
        # self.assertEqual(user.entry, self.entry)

    def test_blank_data(self):
        form = UserForm({})
        # form = UserForm({}, entry=self.entry)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'username': ['required'],
            'email': ['required'],
            'password': ['required'],
        })


class MissingFormTest(TestCase):
    def setUp(self):
        form = MissingForm()
        self.user = form.objects.create(FirstName='aya', SecondName='shaaban',
                                        Sex='female', AgeBeforeMissing='15',
                                        DateOfBirth='20/5/2012', HairColour='fuchia',
                                        EyesColour='red',
                                        Weight='50', Height='150',
                                        MissingFrom='cairo',
                                        MissingDate='20/5/2018', RelativeID='53689',
                                        RelativeRelation='mother',
                                        Details='l2etha',
                                        MissingPersonImage='',)
        # image needs mock up

    def test_valid_form(self):
        mp = MissingPerson.objects.create(title='Find Your Missing.....', body='Bar')
        data = {'title': mp.title, 'body': mp.body, }
        form = MissingForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        w = MissingPerson.objects.create(title='Find Your Missing.....', body='')
        data = {'title': w.title, 'body': w.body, }
        form = MissingForm(data=data)
        self.assertFalse(form.is_valid())

    def test_valid_data(self):
        form = MissingForm({
            'FirstName': 'aya', 'SecondName': 'shaaban', 'Sex': 'female', 'AgeBeforeMissing': '15',
            'DateOfBirth': '20/5/2012', 'HairColour': 'fuchia', 'EyesColour': 'red',
            'Weight': '50', 'Height': '150', 'MissingFrom': 'cairo',
            'MissingDate': '20/5/2018', 'RelativeID': '53689', 'RelativeRelation': 'mother',
            'Details': 'l2etha',
            'MissingPersonImage': '',
        })

        self.assertTrue(form.is_valid())
        missp = form.save()
        self.assertEqual(missp.FirstName, "aya")
        self.assertEqual(missp.SecondName, "shaaban")
        self.assertEqual(missp.Sex, "female")
        self.assertEqual(missp.AgeBeforeMissing, "15")
        self.assertEqual(missp.DateOfBirth, "20/5/2012")
        self.assertEqual(missp.HairColour, "fuchia")
        self.assertEqual(missp.EyesColour, "red")
        self.assertEqual(missp.Weight, "50")
        self.assertEqual(missp.Height, "150")
        self.assertEqual(missp.MissingFrom, "cairo")
        self.assertEqual(missp.MissingDate, "20/5/2018")
        self.assertEqual(missp.RelativeID, "53689")
        self.assertEqual(missp.RelativeRelation, "mother")
        self.assertEqual(missp.Details, "l2etha")
        self.assertEqual(missp.MissingPersonImage, "")

    def test_blank_data(self):
        form = UserForm({})
        # form = UserForm({}, entry=self.entry)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'FirstName': ['required'],
            'SecondNam': ['required'],
            'AgeBeforeMissing': ['required'],
            'DateOfBirth': ['required'],
            'HairColour': ['required'],
            'EyesColour': ['required'],
            'Weigh': ['required'],
            'Height': ['required'],
            'MissingFrom': ['required'],
            'MissingDate': ['required'],
            'RelativeID': ['required'],
            'RelativeRelation': ['required'],
            'Details': ['required'],
            'MissingPersonImage': ['required'],

        })


class FoundFormTest(TestCase):
    # def setUp(self):
    #     form = FoundForm()
    #     self.user = form.objects.create(Sex="femal",FoundIn='cairo',
    #                                     FoundDate='20/4/2015',Location='5233665',Details='l2etha',
    #                                     FoundPersonImage='',)
    def test_valid_form(self):
        fp = FoundPerson.objects.create(title='Found Form', body='Bar')
        data = {'title': fp.title, 'body': fp.body, }
        form = FoundForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        w = FoundPerson.objects.create(title='Found Form', body='')
        data = {'title': w.title, 'body': w.body, }
        form = FoundForm(data=data)
        self.assertFalse(form.is_valid())

    def test_valid_data(self):
        form = FoundForm({'Sex': "femal",
                          'FoundIn': "cairo",
                          'FoundDate': "20/4/2015",
                          'Location': "5233665",
                          'Details': "l2etha",
                          'FoundPersonImage': "",
                          # m=image mockup dont forget
                          })

        self.assertTrue(form.is_valid())
        missp = form.save()
        self.assertEqual(missp.sex, "female")
        self.assertEqual(missp.FoundIn, "cairo")
        self.assertEqual(missp.FoundDate, "20/4/2015")
        self.assertEqual(missp.Location, "5233665")
        self.assertEqual(missp.Details, "l2etha")
        self.assertEqual(missp.FoundPersonImage, "")

    def test_blank_data(self):
        form = FoundForm({})

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'Sex': ['required'],
            'FoundIn': ['required'],
            'FoundDate': ['required'],
            'Location': ['required'],
            'Details': ['required'],
            'FoundPersonImage': ['required'],
        })

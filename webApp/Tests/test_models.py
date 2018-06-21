from django.test import TestCase
from home.models import MissingPerson,FoundPerson

from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
import unittest.mock as mock
from django.core.files import File
from django.core.files.storage import Storage
from PIL import Image
import tempfile
from django.test import TestCase

from django.test import override_settings

import os.path
# another way
# file_mock = mock.MagicMock(spec=File, name='FileMock')

#Note For me : FAILED (errors=1)
# Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
# (this failure is expected, because False is not True!).
# nkamel ba2a rabena m3ana


# models test
#Missing Person

# class MissingPerson(TestCase):
#     def create_missinpperson(self, title="only a test", body="yes, this is only a test"):
#         return MissingPerson.objects.create(title=title, body=body, created_at=timezone.now())
#
#     def test_missinpperson_creation(self):
#         w = self.create_missinpperson()
#         self.assertTrue(isinstance(w, MissingPerson))
#         self.assertEqual(w.__unicode__(), w.title)



class MissingPersonTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods


        MissingPerson.objects.create(FirstName ='Ayah', SecondName='Shaaban',Sex='female', AgeBeforeMissing='15',DateOfBirth='20/5/1988'
                                     ,HairColour='fushiah',EyesColour='abyad',Weight='50',Height='150'
                                     ,MissingFrom='cairo',MissingDate='15/5/2000'
                                     ,RelativeID='215863398475',RelativeRelation='mother',
                                     Details='msh 3awzaaha lama tla2oha mowtoha w hadekom floos XD ',
                                    )
     # Names
    def test_FirstName_label(self):
        missing=MissingPerson.objects.get(id=1)
        field_label = missing._meta.get_field('FirstName').verbose_name
        self.assertEquals(field_label,'FirstName')

    def test_SecondName_label(self):
            missing = MissingPerson.objects.get(id=1)
            field_label = missing._meta.get_field('SecondName').verbose_name
            self.assertEquals(field_label, 'SecondName')
    def test_FirstName_length(self):
        missing=MissingPerson.objects.get(id=1)
        max_length = missing._meta.get_field('FirstName').max_length
        self.assertEquals(max_length,40)
    def test_SecondName_length(self):
        missing=MissingPerson.objects.get(id=1)
        max_length = missing._meta.get_field('SecondName').max_length
        self.assertEquals(max_length,40)
    def test_Sex(self):
            missing = MissingPerson.objects.get(id=1)
            field_label = missing._meta.get_field('Sex').verbose_name
            self.assertEquals(field_label, 'Sex')
    def test_Sex_length(self):
        missing=MissingPerson.objects.get(id=1)
        max_length = missing._meta.get_field('Sex').max_length
        self.assertEquals(max_length,15)

    def test_AgeBeforeMissing(self):
            missing = MissingPerson.objects.get(id=1)
            field_label = missing._meta.get_field('AgeBeforeMissing').verbose_name
            self.assertEquals(field_label, 'AgeBeforeMissing')
    def test_AgeBeforeMissing_length(self):
        missing=MissingPerson.objects.get(id=1)
        max_length = missing._meta.get_field('AgeBeforeMissing').max_length
        self.assertEquals(max_length,3)

    def test_DateOfBirth(self):
            missing = MissingPerson.objects.get(id=1)
            field_label = missing._meta.get_field('DateOfBirth').verbose_name
            self.assertEquals(field_label, 'DateOfBirth')

    def test_DateOfBirth_length(self):
            missing = MissingPerson.objects.get(id=1)
            max_length = missing._meta.get_field('DateOfBirth').max_length
            self.assertEquals(max_length, 10)

    def test_HairColour(self):
        missing = MissingPerson.objects.get(id=1)
        field_label = missing._meta.get_field('HairColour').verbose_name
        self.assertEquals(field_label, 'HairColour')

    def test_HairColour_length(self):
        missing = MissingPerson.objects.get(id=1)
        max_length = missing._meta.get_field('HairColour').max_length
        self.assertEquals(max_length, 50)

    def test_EyesColour(self):
        missing = MissingPerson.objects.get(id=1)
        field_label = missing._meta.get_field('EyesColour').verbose_name
        self.assertEquals(field_label, 'EyesColour')

    def test_EyesColour_length(self):
        missing = MissingPerson.objects.get(id=1)
        max_length = missing._meta.get_field('EyesColour').max_length
        self.assertEquals(max_length, 50)

    def test_Weight(self):
        missing = MissingPerson.objects.get(id=1)
        field_label = missing._meta.get_field('Weight').verbose_name
        self.assertEquals(field_label, 'Weight')

    def test_Weight_length(self):
        missing = MissingPerson.objects.get(id=1)
        max_length = missing._meta.get_field('Weight').max_length
        self.assertEquals(max_length,4)

    def test_Height(self):
        missing = MissingPerson.objects.get(id=1)
        field_label = missing._meta.get_field('Height').verbose_name
        self.assertEquals(field_label, 'Height')

    def test_Height_length(self):
        missing = MissingPerson.objects.get(id=1)
        max_length = missing._meta.get_field('Height').max_length
        self.assertEquals(max_length,4)


    def test_MissingFrom(self):
        missing = MissingPerson.objects.get(id=1)
        field_label = missing._meta.get_field('MissingFrom').verbose_name
        self.assertEquals(field_label, 'MissingFrom')

    def test_MissingFrom_length(self):
        missing = MissingPerson.objects.get(id=1)
        max_length = missing._meta.get_field('MissingFrom').max_length
        self.assertEquals(max_length,150)

    def test_MissingDate(self):
        missing = MissingPerson.objects.get(id=1)
        field_label = missing._meta.get_field('MissingDate').verbose_name
        self.assertEquals(field_label, 'MissingDate')

    def test_MissingDate_length(self):
        missing = MissingPerson.objects.get(id=1)
        max_length = missing._meta.get_field('MissingDate').max_length
        self.assertEquals(max_length,10)

    def test_RelativeID(self):
        missing = MissingPerson.objects.get(id=1)
        field_label = missing._meta.get_field('RelativeID').verbose_name
        self.assertEquals(field_label, 'RelativeID')

    def test_RelativeID_length(self):
        missing = MissingPerson.objects.get(id=1)
        max_length = missing._meta.get_field('RelativeID').max_length
        self.assertEquals(max_length,15)

    def test_RelativeRelation(self):
        missing = MissingPerson.objects.get(id=1)
        field_label = missing._meta.get_field('RelativeRelation').verbose_name
        self.assertEquals(field_label, 'RelativeRelation')

    def test_RelativeRelation_length(self):
        missing = MissingPerson.objects.get(id=1)
        max_length = missing._meta.get_field('RelativeRelation').max_length
        self.assertEquals(max_length,80)

    def test_RDetails(self):
        missing = MissingPerson.objects.get(id=1)
        field_label = missing._meta.get_field('Details').verbose_name
        self.assertEquals(field_label, 'Details')

    def test_Details_length(self):
        missing = MissingPerson.objects.get(id=1)
        max_length = missing._meta.get_field('Details').max_length
        self.assertEquals(max_length,4000)

    def test_MissingPersonImage(self):
        os.chdir("D:\Computer department\Missing people\FindYourMissing-master")
        MissingPerson.MissingPersonImage = SimpleUploadedFile(name='test_image.jpg',
                                                              content=open('FindYourMissing-master/home/Tests', 'rb').read(),
                                                              content_type='image/jpg')






#___________♥______________________#

    #data field

    # def test_date_label(self):
    #     missing=MissingPerson.objects.get(id=1)
    #     field_label = missing._meta.get_field('date').verbose_name
    # self.assertEquals(field_label,'5/5/2012')

    # text field

    # def test_Text_label(self):
    #     missing=MissingPerson.objects.get(id=1)
    #     field_label = missing._meta.get_field('Text').verbose_name
    # self.assertEquals(field_label,'aaaalsssssls')





    def test_get_absolute_url(self):
        missing = MissingPerson.objects.get(id=1)
        #This will also fail if the urlconf is not defined.

        # self.assertEqual("/home/missingDetailsView/pk", self.missing.objects.get(pk=1))
        self.assertEqual("/home/missingDetailsView/1",missing.get_absolute_url())


class FoundPersonTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods

        user =FoundPerson.objects.create(Sex='female', AgeBeforeMissing='15',DateOfBirth='20/5/1988'
                                     , FoundIn='cairo',FoundDate='15/5/2000'
                                     ,Location='+69215863398475',
                                     Details='3ayel tayeh ya wlad el 7alaaaal T_T ',
                                    )

        FoundPerson.objects.create(userID=user)



    def test_Sex(self):
        found = MissingPerson.objects.get(id=1)
        field_label = found._meta.get_field('Sex').verbose_name
        self.assertEquals(field_label, 'Sex')
    def test_Sex_length(self):
        found=MissingPerson.objects.get(id=1)
        max_length = found._meta.get_field('Sex').max_length
        self.assertEquals(max_length,15)

    def test_FoundIn(self):
        found = MissingPerson.objects.get(id=1)
        field_label = found._meta.get_field('FoundIn').verbose_name
        self.assertEquals(field_label, 'FoundIn')


    def test_FoundIn_length(self):
        found=MissingPerson.objects.get(id=1)
        max_length = found._meta.get_field('FoundDate').max_length
        self.assertEquals(max_length,150)


    def test_FoundDate(self):
        found = MissingPerson.objects.get(id=1)
        field_label = found._meta.get_field('FoundDate').verbose_name
        self.assertEquals(field_label, 'FoundDate')


    def test_FoundDate_length(self):
        found = MissingPerson.objects.get(id=1)
        max_length = found._meta.get_field('FoundDate').max_length
        self.assertEquals(max_length, 10)


    def test_Location(self):
        found = MissingPerson.objects.get(id=1)
        field_label = found._meta.get_field('Location').verbose_name
        self.assertEquals(field_label, 'Location')


    def test_Location_length(self):
        found = MissingPerson.objects.get(id=1)
        max_length = found._meta.get_field('Location').max_length
        self.assertEquals(max_length, 150)


    def test_RDetails(self):
        found = MissingPerson.objects.get(id=1)
        field_label = found._meta.get_field('Details').verbose_name
        self.assertEquals(field_label, 'Details')

    def test_Details_length(self):
        found = MissingPerson.objects.get(id=1)
        max_length = found._meta.get_field('Details').max_length
        self.assertEquals(max_length,4000)

    def test_FoundPersonImage(self):
             path = "D:\Computer department\Missing people\FindYourMissing-master"
             FoundPerson.FoundPersonImage = SimpleUploadedFile(name='test_image.jpg',content=open( path, 'rb').read(),content_type='image/jpg')


# ERROR !
    def test_get_absolute_url(self):
            found = FoundPerson.objects.get(id=1)


            # This will also fail if the urlconf is not defined.

            # self.assertEqual("/home/missingDetailsView/pk", self.missing.objects.get(pk=1))
            self.assertEqual( found.get_absolute_url(),"/home/foundDetailsView/1")
from datetime import datetime

from django.test import TestCase

# Create your tests here.

from .models import *


class SaaSAppModelTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        car = Car.objects.create(id=1, name='科迈罗')
        dealer = CarDealer.objects.create(id=1, name='肇庆市金城', address='肇庆市过境公路鼎湖苏村段',
                                          phone_num='18475164455', call_phone_num=1,
                                          visitor_num=1, buy_num=1)
        CustomerLogger.objects.create(date_time=datetime.now(), user_ip='127.0.0.1', car_dealer=dealer)
        AskingLowPrice.objects.create(date_time=datetime.now(), user_ip='127.0.0.1', car_dealer=dealer, user_name='张三',
                                      user_phone='18475133344')
        TestDrive.objects.create(date_time=datetime.now(), user_ip='127.0.0.1', car_dealer=dealer, user_name='张三',
                                 user_phone='18475133344')
        CarSalesDetails.objects.create(name='2018 2.0E精英版', naked_car_price=17.98, guidance_price=16.98, dealer=dealer,
                                       car=car)

    def test_CustomerLogger_model(self):
        result = CustomerLogger.objects.get(id=1)
        self.assertFalse(result.is_call_phone)
        self.assertEqual(result.user_ip, '127.0.0.1')

    def test_AskingLowPrice_model(self):
        result = AskingLowPrice.objects.get(id=1)
        self.assertEqual(result.car_dealer.name, '肇庆市金城')
        self.assertEqual(result.user_name, '张三')

    def test_TestDrive_model(self):
        result = TestDrive.objects.get(id=1)
        self.assertEqual(result.car_dealer.name, '肇庆市金城')
        self.assertEqual(result.user_phone, '18475133344')

    def test_CarSalesDetails_model(self):
        result = CarSalesDetails.objects.get(id=1)
        self.assertEqual(result.name, '2018 2.0E精英版')
        self.assertEqual(result.naked_car_price, 17.98)
        self.assertEqual(result.car.name, '科迈罗')

    @classmethod
    def tearDownClass(cls):
        CustomerLogger.objects.get(id=1).delete()
        AskingLowPrice.objects.get(id=1).delete()
        TestDrive.objects.get(id=1).delete()
        CarSalesDetails.objects.get(id=1).delete()
        Car.objects.get(id=1).delete()
        CarDealer.objects.get(id=1).delete()

from datetime import datetime

from django.test import TestCase

from .models import *


# Create your tests here.


class SaaSPCModelTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        region = Region.objects.create(id=1, name='华北')
        province = Province.objects.create(id=1, name='广东', region=region)
        city = City.objects.create(id=1, name='广州', province=province)
        district = District.objects.create(id=1, name='天河', city=city)
        power_type = PowerType.objects.create(id=1, name='汽油车')
        market_level = MarketLevel.objects.create(id=1, name='跑车')
        grade_level = GradeLevel.objects.create(id=1, name='进口')
        blood_relationship = BloodRelationship.objects.create(id=1, name='美系')
        car_type = CarType.objects.create(id=1, name='跑车')
        car_brand = CarBrand.objects.create(id=1, name='雪佛兰')
        manufacturer_name = ManufacturerName.objects.create(id=1, name='雪佛兰')
        car = Car.objects.create(id=1, name='科迈罗', power_type=power_type, market_level=market_level,
                                 grade_level=grade_level,
                                 blood_relationship=blood_relationship,
                                 car_type=car_type, car_brand=car_brand, manufacturer_name=manufacturer_name)
        dealer = CarDealer.objects.create(id=1, name='肇庆市金城', address='肇庆市过境公路鼎湖苏村段',
                                          province=province,
                                          city=city, phone_num='18475164455', call_phone_num=1,
                                          visitor_num=1, buy_num=1)
        DealerUser.objects.create(id=1, username='liuwang', last_login=datetime.now(), is_superuser=1,
                                  frist_create_ip='192.168.0.0', dealer=dealer, last_login_ip='192.168.0.1',
                                  permission_levels=1)
        UrlApi.objects.create(id=1, api_name='获取所有省份的名称接口')
        DealerAndCars.objects.create(car=car, car_dealer=dealer)
        CityPeopleNum.objects.create(date=datetime.now().date(), province=province, city=city, watch_num=1,
                                     intent_num=1, like_num=1)
        CarInterestLoophole.objects.create(date=datetime.now().date(), city=city, car=car, watch_num=1,
                                           intent_num=1, like_num=1)
        CarSalesSummary.objects.create(date=datetime.now().date(), dealer=dealer, car_id=car.id, visitor_num=1,
                                       call_phone_num=2)
        ActivityPlan.objects.create(dealer=dealer, create_plan_time=datetime.now(), activity_name='180621 凯美瑞日常拉新',
                                    city=city, district=district, plan_status=0, push_mode=0,
                                    watch_start_time=datetime.strptime('2018-03-05', '%Y-%m-%d'),
                                    watch_end_time=datetime.strptime('2018-03-05', '%Y-%m-%d'), intention_attributes=0,
                                    sexs=3, ages=31, car=car, push_freq=10, time_interval=1,
                                    start_push_with_workingday=datetime.strptime('2018-03-05', '%Y-%m-%d'),
                                    end_push_with_workingday=datetime.strptime('2018-03-05', '%Y-%m-%d'),
                                    push_cover_num=1000, push_cover_percent=0.98)

    def test_region_model(self):
        result = Region.objects.get(id=1)
        self.assertEqual(result.name, '华北')

    def test_province_model(self):
        result = Province.objects.get(id=1)
        self.assertEqual(result.name, '广东')

    def test_city_model(self):
        result = City.objects.get(id=1)
        self.assertEqual(result.name, '广州')

    def test_district_model(self):
        result = District.objects.get(id=1)
        self.assertEqual(result.name, '天河')

    def test_PowerType_model(self):
        result = PowerType.objects.get(id=1)
        self.assertEqual(result.name, '汽油车')

    def test_MarketLevel_model(self):
        result = MarketLevel.objects.get(id=1)
        self.assertEqual(result.name, '跑车')

    def test_GradeLevel_model(self):
        result = GradeLevel.objects.get(id=1)
        self.assertEqual(result.name, '进口')

    def test_CarType_model(self):
        result = CarType.objects.get(id=1)
        self.assertEqual(result.name, '跑车')

    def test_CarBrand_model(self):
        result = CarBrand.objects.get(id=1)
        self.assertEqual(result.name, '雪佛兰')

    def test_ManufacturerName_model(self):
        result = ManufacturerName.objects.get(id=1)
        self.assertEqual(result.name, '雪佛兰')

    def test_Car_model(self):
        result = Car.objects.get(id=1)
        self.assertEqual(result.name, '科迈罗')
        self.assertEqual(result.car_type.name, '跑车')

    def test_CarDealer_model(self):
        result = CarDealer.objects.get(id=1)
        self.assertEqual(result.name, '肇庆市金城')
        self.assertEqual(result.address, '肇庆市过境公路鼎湖苏村段')
        self.assertEqual(result.province.name, '广东')
        self.assertEqual(result.phone_num, '18475164455')

    def test_DealerUser_model(self):
        result = DealerUser.objects.get(id=1)
        self.assertEqual(result.username, 'liuwang')
        self.assertEqual(result.frist_create_ip, '192.168.0.0')
        self.assertEqual(result.get_permission_levels_display(), '城市级别')

    def test_UrlApi_model(self):
        result = UrlApi.objects.get(id=1)
        self.assertEqual(result.api_name, '获取所有省份的名称接口')

    def test_DealerAndCars_model(self):
        result = DealerAndCars.objects.get(id=1)
        self.assertEqual(result.car.name, '科迈罗')

    def test_CityPeopleNum_model(self):
        result = CityPeopleNum.objects.get(id=1)
        self.assertEqual(result.date, datetime.now().date())
        self.assertEqual(result.buy_num, 0)

    def test_CarInterestLoophole_model(self):
        result = CarInterestLoophole.objects.get(id=1)
        self.assertEqual(result.date, datetime.now().date())
        self.assertEqual(result.city.name, '广州')

    def test_CarSalesSummary_model(self):
        result = CarSalesSummary.objects.get(id=1)
        self.assertEqual(result.car.name, '科迈罗')

    def test_ActivityPlan_model(self):
        result = ActivityPlan.objects.get(id=1)
        self.assertEqual(result.activity_name, '180621 凯美瑞日常拉新')
        self.assertEqual(result.watch_start_time.strftime('%Y-%m-%d'), '2018-03-05')
        self.assertEqual(result.get_sexs_display(), '男女都选')
        self.assertEqual(result.push_cover_percent, 0.98)

    @classmethod
    def tearDownClass(cls):
        DealerAndCars.objects.get(id=1).delete()
        CityPeopleNum.objects.get(id=1).delete()
        CarInterestLoophole.objects.get(id=1).delete()
        CarSalesSummary.objects.get(id=1).delete()
        Region.objects.get(id=1).delete()
        Province.objects.get(id=1).delete()
        City.objects.get(id=1).delete()
        District.objects.get(id=1).delete()
        PowerType.objects.get(id=1).delete()
        MarketLevel.objects.get(id=1).delete()
        GradeLevel.objects.get(id=1).delete()
        BloodRelationship.objects.get(id=1).delete()
        CarType.objects.get(id=1).delete()
        CarBrand.objects.get(id=1).delete()
        ManufacturerName.objects.get(id=1).delete()
        Car.objects.get(id=1).delete()
        CarDealer.objects.get(id=1).delete()
        UrlApi.objects.get(id=1).delete()

from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class PowerType(models.Model):
    """
    动力类型表
    """
    name = models.CharField(max_length=20, verbose_name='动力类型名称')

    class Meta:
        verbose_name = '动力类型'
        verbose_name_plural = verbose_name
        db_table = 'power_type'


class MarketLevel(models.Model):
    """
    市场级别及细分级别表
    """
    name = models.CharField(max_length=20, verbose_name='市场级别及细分级别名称')

    class Meta:
        verbose_name = '市场级别及细分级别'
        verbose_name_plural = verbose_name
        db_table = 'market_level'


class GradeLevel(models.Model):
    """
    档次等级表
    """
    name = models.CharField(max_length=20, verbose_name='档次等级名称')

    class Meta:
        verbose_name = '档次等级'
        verbose_name_plural = verbose_name
        db_table = 'grade_level'


class BloodRelationship(models.Model):
    """
    车系血缘表
    """
    name = models.CharField(max_length=20, verbose_name='车系血缘名称')

    class Meta:
        verbose_name = '车系血缘'
        verbose_name_plural = verbose_name
        db_table = 'blood_relationship'


class CarType(models.Model):
    """
    车身类型表
    """
    name = models.CharField(max_length=20, verbose_name='车身类型名称')

    class Meta:
        verbose_name = '车身类型'
        verbose_name_plural = verbose_name
        db_table = 'car_type'


class CarBrand(models.Model):
    """
    车企品牌表
    """
    name = models.CharField(max_length=20, verbose_name='车企品牌名称')

    class Meta:
        verbose_name = '车企品牌'
        verbose_name_plural = verbose_name
        db_table = 'car_brand'


class ManufacturerName(models.Model):
    """
    厂家表
    """
    name = models.CharField(max_length=20, verbose_name='厂家名称')

    class Meta:
        verbose_name = '厂家'
        verbose_name_plural = verbose_name
        db_table = 'manufacturer_name'


class Car(models.Model):
    """
    汽车属性表
    """
    name = models.CharField(max_length=20, verbose_name='汽车名称')
    power_type = models.ForeignKey(PowerType, verbose_name='动力类型', on_delete=models.CASCADE)
    market_level = models.ForeignKey(MarketLevel, verbose_name='市场级别及细分级别', on_delete=models.CASCADE)
    grade_level = models.ForeignKey(GradeLevel, verbose_name='档次等级', on_delete=models.CASCADE)
    blood_relationship = models.ForeignKey(BloodRelationship, verbose_name='车系血缘', on_delete=models.CASCADE)
    car_type = models.ForeignKey(CarType, verbose_name='车身类型', on_delete=models.CASCADE)
    car_brand = models.ForeignKey(CarBrand, verbose_name='车企品牌', on_delete=models.CASCADE)
    manufacturer_name = models.ForeignKey(ManufacturerName, verbose_name='厂家名称', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '汽车'
        verbose_name_plural = verbose_name
        db_table = 'car'


class Region(models.Model):
    """
    区域表
    """
    name = models.CharField(max_length=20, verbose_name='区域名称')

    class Meta:
        verbose_name = '区域'
        verbose_name_plural = verbose_name
        db_table = 'region'


class Province(models.Model):
    """
    省份表
    """
    name = models.CharField(max_length=20, verbose_name='省份名称')
    region = models.ForeignKey(Region, verbose_name='区域', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = '省份'
        verbose_name_plural = verbose_name
        db_table = 'province'


class City(models.Model):
    """
    城市表
    """
    name = models.CharField(max_length=20, verbose_name='城市名称')
    province = models.ForeignKey(Province, verbose_name='省份', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name
        db_table = 'city'


class District(models.Model):
    """
    行政区表
    """
    name = models.CharField(max_length=20, verbose_name='行政区名称')
    city = models.ForeignKey(City, verbose_name='城市', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '行政区'
        verbose_name_plural = verbose_name
        db_table = 'district'


class CarDealer(models.Model):
    """
    汽车经销商信息
    """
    name = models.CharField(max_length=50, verbose_name='汽车厂商名称')
    address = models.TextField(verbose_name='经销商地址')
    province = models.ForeignKey(Province, verbose_name='省份', on_delete=models.CASCADE)
    city = models.ForeignKey(City, verbose_name='城市', on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=20, verbose_name='汽车经销商页面号码')
    visitor_num = models.IntegerField(default=0, verbose_name='经销商总页面浏览人数')
    call_phone_num = models.IntegerField(default=0, verbose_name='经销商总拨打电话人数')
    buy_num = models.IntegerField(default=0, verbose_name='经销商总提供线索买车人数')

    class Meta:
        verbose_name = '汽车经销商'
        verbose_name_plural = verbose_name
        db_table = 'car_dealer'


class DealerUser(AbstractUser):
    """
    员工信息，使用saas的人
    """
    frist_create_ip = models.CharField(max_length=20, verbose_name='用户首次创建ip地址')
    last_login_ip = models.CharField(max_length=20, verbose_name='用户最近登陆ip')
    api_permissions = models.TextField(verbose_name='API的权限,为各API权限表的ID')
    permission_levels = models.IntegerField(default=0, choices=((1, '城市级别'), (2, '省级'), (3, '全国级')),
                                            verbose_name='权限等级')
    dealer = models.ForeignKey(CarDealer, verbose_name='汽车经销商', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '经销商员工'
        verbose_name_plural = verbose_name
        db_table = 'dealer_user'


class UrlApi(models.Model):
    api_name = models.TextField(verbose_name='api名称')

    class Meta:
        verbose_name = 'API权限id表'
        verbose_name_plural = verbose_name
        db_table = 'url_api'


class DealerAndCars(models.Model):
    """
    经销商与车型关系表
    """
    car_dealer = models.ForeignKey(CarDealer, verbose_name='经销商', on_delete=models.CASCADE, null=False, blank=False)
    car = models.ForeignKey(Car, verbose_name='汽车', on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        verbose_name = '经销商与车型关系表'
        verbose_name_plural = verbose_name
        db_table = 'dealer_and_cars'


class CityPeopleNum(models.Model):
    """
    基于城市的关注汽车人数数量表
    """
    date = models.DateField(verbose_name='日期', null=False, blank=False)
    province = models.ForeignKey(Province, verbose_name='省份', on_delete=models.CASCADE, null=False, blank=False)
    city = models.ForeignKey(City, verbose_name='城市', on_delete=models.CASCADE, null=False, blank=False)
    watch_num = models.IntegerField(default=0, verbose_name='关注人数')
    intent_num = models.IntegerField(default=0, verbose_name='兴趣人数')
    like_num = models.IntegerField(default=0, verbose_name='意向人数')
    buy_num = models.IntegerField(default=0, verbose_name='到店人数')

    class Meta:
        verbose_name = '基于城市的关注汽车的人数'
        verbose_name_plural = verbose_name
        unique_together = ('date', 'province', 'city')
        db_table = 'city_people_num'


class CarInterestLoophole(models.Model):
    """
    关注汽车的人数数量表
    """
    date = models.DateField(verbose_name='日期', null=False, blank=False)
    city = models.ForeignKey(City, verbose_name='城市', on_delete=models.CASCADE, null=False, blank=False)
    car = models.ForeignKey(Car, verbose_name='汽车', on_delete=models.CASCADE, null=False, blank=False)
    watch_num = models.IntegerField(default=0, verbose_name='关注人数')
    intent_num = models.IntegerField(default=0, verbose_name='兴趣人数')
    like_num = models.IntegerField(default=0, verbose_name='意向人数')
    buy_num = models.IntegerField(default=0, verbose_name='到店人数')

    class Meta:
        verbose_name = '基于城市的关注汽车的人数'
        verbose_name_plural = verbose_name
        unique_together = ('date', 'car', 'city')
        db_table = 'car_interest_loophole'


class CarSalesSummary(models.Model):
    date = models.DateField(default=datetime.now, verbose_name='时间', null=False, blank=False)
    dealer = models.ForeignKey(CarDealer, verbose_name='汽车经销商', null=False, blank=False, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, verbose_name='汽车', null=False, blank=False, on_delete=models.CASCADE)
    visitor_num = models.IntegerField(default=0, verbose_name='经销商总页面浏览人数')
    call_phone_num = models.IntegerField(default=0, verbose_name='经销商总拨打电话人数')
    buy_num = models.IntegerField(default=0, verbose_name='经销商总提供线索买车人数')

    class Meta:
        verbose_name = '经销商车型营销页面访问表'
        verbose_name_plural = verbose_name
        unique_together = ('date', 'dealer', 'car')
        db_table = 'car_sales_summary'


class ActivityPlan(models.Model):
    """
    活动计划投放表
    """
    dealer = models.ForeignKey(CarDealer, verbose_name='汽车经销商', on_delete=models.CASCADE)
    create_plan_time = models.DateTimeField(default=datetime.now, verbose_name='计划创建时间')
    activity_name = models.CharField(max_length=50, verbose_name='活动名称')
    city = models.ForeignKey(City, verbose_name='城市', on_delete=models.CASCADE)
    district = models.ForeignKey(District, verbose_name='行政区', on_delete=models.CASCADE)
    plan_status = models.IntegerField(choices=((0, '未发送'), (1, '已开始'), (2, '结束')), verbose_name='计划状态')
    push_mode = models.IntegerField(choices=((0, '短信'), (1, '精准营销'), (2, '云呼')), verbose_name='推送模式')
    watch_start_time = models.DateField(verbose_name='看车周期开始时间')
    watch_end_time = models.DateField(verbose_name='看车周期结束时间')
    intention_attributes = models.IntegerField(choices=((0, '关注'), (1, '兴趣'), (2, '意向'), (3, '到店')),
                                               verbose_name='意向属性')
    sexs = models.IntegerField(choices=((0, '男女都不选'), (1, '只选女'), (2, '只选男'), (3, '男女都选')), verbose_name='性别属性')
    ages = models.IntegerField(verbose_name='年龄属性(多选)，采用二进制表示，第一位表示小于25岁，第二位表示25~32岁，第三位表示32~40岁，第四位表示40~50岁，第五位表示大于50')
    car = models.ForeignKey(Car, verbose_name='汽车', on_delete=models.CASCADE)
    push_freq = models.IntegerField(verbose_name='推送频次')
    time_interval = models.IntegerField(verbose_name='时间间隔(天)')
    start_push_with_workingday = models.DateTimeField(verbose_name='工作日推送开始时间')
    end_push_with_workingday = models.DateTimeField(verbose_name='工作日推送结束时间')
    start_push_with_holiday = models.DateTimeField(verbose_name='节假日推送开始时间')
    end_push_with_holiday = models.DateTimeField(verbose_name='节假日推送结束时间')
    push_cover_num = models.IntegerField(verbose_name='发送覆盖人数')
    push_cover_percent = models.FloatField(verbose_name='覆盖百分比')

    class Meta:
        verbose_name = '活动计划'
        verbose_name_plural = verbose_name
        db_table = 'activity_plan'

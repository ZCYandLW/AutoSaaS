from datetime import datetime

from django.db import models
from SaasPC.models import Car, CarDealer


# Create your models here.


class CustomerLogger(models.Model):
    """
    用户访问经销商页面日志表
    """
    date_time = models.DateTimeField(default=datetime.now, verbose_name='登录时间')
    user_ip = models.CharField(max_length=20, verbose_name='用户IP')
    car_dealer = models.ForeignKey(CarDealer, verbose_name='汽车经销商', null=True, blank=True, on_delete=models.SET_NULL)
    is_call_phone = models.BooleanField(default=False, verbose_name='是否拨打电话')
    is_leave_clue = models.BooleanField(default=False, verbose_name='是否留下线索')

    class Meta:
        verbose_name = '用户访问经销商页面日志表'
        verbose_name_plural = verbose_name
        unique_together = ('date_time', 'user_ip', 'car_dealer')
        db_table = 'customer_logger'


class AskingLowPrice(models.Model):
    """
    用户寻价记录表
    """
    date_time = models.DateTimeField(default=datetime.now, verbose_name='登录时间')
    user_ip = models.CharField(max_length=20, verbose_name='用户IP')
    car_dealer = models.ForeignKey(CarDealer, verbose_name='汽车经销商', null=True, blank=True, on_delete=models.SET_NULL)
    user_name = models.CharField(max_length=11, verbose_name='用户姓名')
    user_phone = models.CharField(max_length=11, verbose_name='用户电话号码')

    class Meta:
        verbose_name = '用户寻价记录表'
        verbose_name_plural = verbose_name
        unique_together = ('date_time', 'user_ip', 'car_dealer')
        db_table = 'asking_low_price'


class TestDrive(models.Model):
    """
    用户预约试驾表
    """
    date_time = models.DateTimeField(default=datetime.now, verbose_name='登录时间', null=False, blank=False)
    user_ip = models.CharField(max_length=20, verbose_name='用户IP', null=False, blank=False)
    car_dealer = models.ForeignKey(CarDealer, verbose_name='汽车经销商', null=True, blank=True, on_delete=models.SET_NULL)
    user_name = models.CharField(max_length=11, verbose_name='用户姓名')
    user_phone = models.CharField(max_length=11, verbose_name='用户电话号码')

    class Meta:
        verbose_name = '用户预约试驾表'
        verbose_name_plural = verbose_name
        unique_together = ('date_time', 'user_ip', 'car_dealer')
        db_table = 'test_drive'


class CarSalesDetails(models.Model):
    """
    经销商具体车型销售明细列表
    """
    name = models.CharField(max_length=20, verbose_name='具体车型款式名称')
    naked_car_price = models.FloatField(verbose_name='具体车型裸车价(万)')
    guidance_price = models.FloatField(verbose_name='具体车型指导价(万)')
    dealer = models.ForeignKey(CarDealer, verbose_name='汽车经销商', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, verbose_name='汽车', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '经销商具体车型销售明细列表'
        verbose_name_plural = verbose_name
        db_table = 'car_sales_details'

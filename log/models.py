from django.db import models

# Create your models here.
class AptCost(models.Model):
    seq = models.AutoField(primary_key=True)  # 자동 증가 기본 키
    apt_name = models.CharField(max_length=30, null=False, blank=False)
    build_year = models.CharField(max_length=5, null=False, blank=False)
    deal_amount = models.CharField(max_length=20, null=False, blank=False)
    deal_day = models.CharField(max_length=5, null=False, blank=False)
    deal_month = models.CharField(max_length=5, null=False, blank=False)
    deal_year = models.CharField(max_length=5, null=False, blank=False)
    exclu_usearea = models.CharField(max_length=20, null=False, blank=False)  # 전용면적
    floor = models.CharField(max_length=5, null=False, blank=False)
    land_leaseholdgbn = models.CharField(
        max_length=5, null=False, blank=False
    )  # 토지임대부 아파트 여부
    sgg_cd = models.CharField(max_length=10, null=False, blank=False)  # 법정동 코드
    umd_nm = models.CharField(max_length=30, null=False, blank=False)  # 법정동 이름.
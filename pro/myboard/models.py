from django.db import models

# Create your models here.
class Shopboard(models.Model):
    num = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    pass_field = models.CharField(db_column='pass', max_length=20)
    mail = models.CharField(max_length=30, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    cont = models.TextField(blank=True, null=True)
    bip = models.CharField(max_length=20, blank=True, null=True)
    bdate = models.CharField(max_length=50, blank=True, null=True)
    readcnt = models.IntegerField(blank=True, null=True)
    gnum = models.IntegerField(blank=True, null=True)
    onum = models.IntegerField(blank=True, null=True)
    nested = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shopboard'
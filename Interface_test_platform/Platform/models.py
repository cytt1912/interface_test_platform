from django.db import models

# Create your models here.

class DBComments(models.Model):
    user = models.CharField(max_length=32,null=True)  #吐槽人名称
    text = models.CharField(max_length=1000,null=True) #吐槽内容
    createtime = models.DateTimeField(auto_now=True)
    #定义数据库显示
    def __str__(self):
        return self.text + str(self.createtime)

#定义传送门数据
class DB_home_href(models.Model):
    name = models.CharField(max_length=32,null=True) #超链接名称
    href = models.CharField(max_length=2000,null=True) #超链接内容

    def __str__(self):
        return self.name



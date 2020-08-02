from django.db import models

# Create your models here.

class DBComments(models.Model):
    user = models.CharField(max_length=32,null=True)  #吐槽人名称
    text = models.CharField(max_length=1000,null=True) #吐槽内容
    createtime = models.DateTimeField(auto_now=True)
    #定义数据库显示
    def __str__(self):
        return self.text + str(self.createtime)

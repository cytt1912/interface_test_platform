# Generated by Django 2.2.1 on 2020-08-02 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Platform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbcomments',
            name='createtime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

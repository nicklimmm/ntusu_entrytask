# Generated by Django 3.1.2 on 2020-10-29 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20201028_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='coding', max_length=255),
        ),
    ]

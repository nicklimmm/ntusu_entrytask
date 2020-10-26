# Generated by Django 3.1.2 on 2020-10-26 07:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201025_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_posted',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(max_length=255),
        ),
    ]
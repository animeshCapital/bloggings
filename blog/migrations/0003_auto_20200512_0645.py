# Generated by Django 2.2.9 on 2020-05-12 06:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200511_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=1, on_delete=True, to=settings.AUTH_USER_MODEL),
        ),
    ]

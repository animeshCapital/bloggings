# Generated by Django 2.2.9 on 2020-05-16 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone_no',
            field=models.CharField(max_length=15, null=True),
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-24 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='host',
            field=models.CharField(default='unknown', max_length=10),
        ),
        migrations.AddField(
            model_name='resume',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
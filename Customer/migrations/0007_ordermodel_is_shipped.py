# Generated by Django 3.1.7 on 2021-05-29 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0006_auto_20210529_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='is_shipped',
            field=models.BooleanField(default=False),
        ),
    ]

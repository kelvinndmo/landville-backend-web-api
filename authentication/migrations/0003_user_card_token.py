# Generated by Django 2.2.1 on 2019-07-16 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='card_token',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
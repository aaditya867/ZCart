# Generated by Django 2.2.7 on 2020-02-07 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200130_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('con_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.IntegerField(default=0)),
                ('desc', models.CharField(default='No description found', max_length=3000)),
            ],
        ),
    ]

# Generated by Django 2.1.1 on 2018-09-18 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20180918_0153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessrecord',
            name='name',
        ),
        migrations.RemoveField(
            model_name='webpage',
            name='topic',
        ),
        migrations.DeleteModel(
            name='AccessRecord',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.DeleteModel(
            name='Webpage',
        ),
    ]

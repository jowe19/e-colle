# Generated by Django 2.0.5 on 2018-05-06 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accueil', '0003_auto_20180504_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='matiere',
            name='nomcomplet',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='ramassage',
            name='moisDebut',
            field=models.DateField(choices=[(datetime.date(2017, 9, 1), 'septembre 2017'), (datetime.date(2017, 10, 1), 'octobre 2017'), (datetime.date(2017, 11, 1), 'novembre 2017'), (datetime.date(2017, 12, 1), 'décembre 2017'), (datetime.date(2018, 1, 1), 'janvier 2018'), (datetime.date(2018, 2, 1), 'février 2018'), (datetime.date(2018, 3, 1), 'mars 2018'), (datetime.date(2018, 4, 1), 'avril 2018'), (datetime.date(2018, 5, 1), 'mai 2018'), (datetime.date(2018, 6, 1), 'juin 2018')], verbose_name='Début'),
        ),
        migrations.AlterField(
            model_name='ramassage',
            name='moisFin',
            field=models.DateField(choices=[(datetime.date(2017, 9, 1), 'septembre 2017'), (datetime.date(2017, 10, 1), 'octobre 2017'), (datetime.date(2017, 11, 1), 'novembre 2017'), (datetime.date(2017, 12, 1), 'décembre 2017'), (datetime.date(2018, 1, 1), 'janvier 2018'), (datetime.date(2018, 2, 1), 'février 2018'), (datetime.date(2018, 3, 1), 'mars 2018'), (datetime.date(2018, 4, 1), 'avril 2018'), (datetime.date(2018, 5, 1), 'mai 2018'), (datetime.date(2018, 6, 1), 'juin 2018')], verbose_name='Fin'),
        ),
    ]
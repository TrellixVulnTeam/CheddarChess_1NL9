# Generated by Django 2.1.2 on 2020-11-26 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajedrez_app', '0013_auto_20201013_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugador',
            name='esperaoponente',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]

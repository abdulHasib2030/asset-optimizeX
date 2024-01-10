# Generated by Django 4.2.6 on 2023-10-28 04:53

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        ('share_assets', '0015_alter_sharedasset_short_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharedasset',
            name='short_url',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=22),
        ),
    ]

# Generated by Django 4.2.5 on 2023-11-02 17:29

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        ('share_assets', '0004_alter_sharedasset_short_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharedasset',
            name='short_url',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=22),
        ),
    ]

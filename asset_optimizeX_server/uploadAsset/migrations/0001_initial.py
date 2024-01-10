# Generated by Django 4.2.6 on 2023-10-20 10:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('asset', models.FileField(upload_to='images/company/asset_versions/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='uploadAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('asset', models.FileField(null=True, upload_to='images/company/asset/')),
                ('description', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(max_length=200)),
                ('comment', models.CharField(blank=True, max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.library')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.organization')),
                ('tags', models.ManyToManyField(blank=True, to='uploadAsset.tag')),
                ('versions', models.ManyToManyField(blank=True, to='uploadAsset.assetversion')),
            ],
        ),
    ]

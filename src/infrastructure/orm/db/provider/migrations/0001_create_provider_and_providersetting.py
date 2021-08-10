# Generated by Django 3.2.5 on 2021-08-10 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('slug', models.SlugField(max_length=25, unique=True)),
                ('priority', models.PositiveSmallIntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'provider',
                'verbose_name_plural': 'providers',
                'ordering': ('priority',),
            },
        ),
        migrations.CreateModel(
            name='ProviderSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setting_type', models.CharField(choices=[('boolean', 'boolean'), ('float', 'float'), ('integer', 'integer'), ('secret', 'secret'), ('text', 'text'), ('url', 'url')], max_length=10)),
                ('key', models.SlugField(max_length=64)),
                ('value', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='provider.provider')),
            ],
            options={
                'verbose_name': 'provider setting',
                'verbose_name_plural': 'provider settings',
                'unique_together': {('provider', 'key')},
            },
        ),
    ]

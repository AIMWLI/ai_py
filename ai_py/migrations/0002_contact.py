# Generated by Django 3.2.10 on 2022-01-19 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai_py', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, null=True, verbose_name='code')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='name')),
            ],
        ),
    ]
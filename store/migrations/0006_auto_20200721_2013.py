# Generated by Django 3.0.4 on 2020-07-21 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0005_auto_20200721_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='country',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='state',
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('country', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(max_length=200, null=True)),
                ('pincode', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

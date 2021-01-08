# Generated by Django 3.1.2 on 2020-12-09 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice', models.CharField(blank=True, max_length=16, null=True)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=150)),
                ('f_name', models.CharField(max_length=100)),
                ('total', models.IntegerField()),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.city')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
            ],
        ),
    ]
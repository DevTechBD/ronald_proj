# Generated by Django 3.1.4 on 2021-01-05 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20201226_0334'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_title', models.CharField(max_length=155)),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='sub_name',
        ),
        migrations.AddField(
            model_name='product',
            name='percent',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
        migrations.AddField(
            model_name='order',
            name='method',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.deliverymethod'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.orderstatus'),
        ),
    ]
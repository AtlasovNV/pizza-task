# Generated by Django 3.0.2 on 2020-01-08 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Order', max_length=128, verbose_name='Order')),
                ('nameUser', models.CharField(default=0, max_length=128, verbose_name='Name user')),
                ('email', models.CharField(default=0, max_length=128, verbose_name='Email')),
                ('address', models.CharField(default=0, max_length=300, verbose_name='Address')),
                ('OrderUser', models.CharField(default=0, max_length=300, verbose_name='Order User')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Total')),
            ],
        ),
        migrations.CreateModel(
            name='ProductClassics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Price')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDrinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Brief')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Price')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('image', models.ImageField(blank=True, upload_to='Images')),
                ('short_desc', models.CharField(blank=True, max_length=60, verbose_name='Brief')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Price')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSpecials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Price')),
            ],
        ),
    ]

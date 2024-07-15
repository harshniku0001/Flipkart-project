# Generated by Django 5.0.4 on 2024-05-21 04:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='category')),
                ('main_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.main')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('review', models.CharField(max_length=20)),
                ('rating', models.CharField(max_length=20)),
                ('detailss', models.TextField()),
                ('image', models.ImageField(upload_to='product')),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.CharField(max_length=20)),
                ('avilable', models.BooleanField()),
                ('description', models.TextField()),
                ('color', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='details')),
                ('pro_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
        migrations.CreateModel(
            name='sub_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='sub_category')),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='sub_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sub_category'),
        ),
    ]

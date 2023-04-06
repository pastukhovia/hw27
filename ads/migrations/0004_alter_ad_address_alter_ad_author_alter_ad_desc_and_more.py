# Generated by Django 4.2 on 2023-04-06 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_alter_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='address',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='author',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='desc',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ad',
            name='name',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]

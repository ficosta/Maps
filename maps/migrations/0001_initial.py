# Generated by Django 2.2 on 2019-04-25 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Status',
                'ordering': ['status'],
            },
        ),
        migrations.CreateModel(
            name='Occurrence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maps.Status', verbose_name='Status')),
            ],
        ),
    ]
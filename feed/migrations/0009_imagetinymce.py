# Generated by Django 2.2.13 on 2020-11-03 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0008_auto_20201102_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageTinymce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
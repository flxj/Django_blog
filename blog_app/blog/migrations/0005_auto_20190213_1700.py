# Generated by Django 2.1.5 on 2019-02-13 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190213_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='picture',
            field=models.ImageField(upload_to='C:\\Pythonweb\\blog_app\\static/blog/img/'),
        ),
    ]

# Generated by Django 3.2.16 on 2023-12-10 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-pub_date',)},
        ),
    ]

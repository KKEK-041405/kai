# Generated by Django 4.1.4 on 2022-12-20 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbts', '0004_sem1_remove_post_text_post_pinno_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.CharField(max_length=12, null=True),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-29 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='article_body',
            field=models.TextField(),
        ),
    ]
# Generated by Django 4.0.2 on 2022-03-01 09:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0005_alter_articles_dislike_alter_articles_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='dislike',
            field=models.ManyToManyField(related_name='dislike', to=settings.AUTH_USER_MODEL),
        ),
    ]

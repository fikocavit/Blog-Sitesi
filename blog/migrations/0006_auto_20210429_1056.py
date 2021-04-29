# Generated by Django 3.1.5 on 2021-04-29 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_delete_begenilermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yorumlarmodel',
            name='yazar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yorum', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='yorumlarmodel',
            name='yazi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yorumlar', to='blog.yazilarmodel'),
        ),
    ]

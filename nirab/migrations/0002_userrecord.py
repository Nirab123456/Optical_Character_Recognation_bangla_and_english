# Generated by Django 4.2.2 on 2023-07-02 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nirab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nirab.record')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='record', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

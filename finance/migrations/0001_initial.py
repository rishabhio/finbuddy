# Generated by Django 3.2.13 on 2022-05-08 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, default=0.0, max_digits=19, verbose_name='Amount')),
                ('reason', models.TextField(blank=True, null=True, verbose_name='Long Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_on')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_on')),
                ('paid_back', models.BooleanField(default=False, verbose_name='Status')),
                ('borrower', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='borrower', to=settings.AUTH_USER_MODEL)),
                ('lender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

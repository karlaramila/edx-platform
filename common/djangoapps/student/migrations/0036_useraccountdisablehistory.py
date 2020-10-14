# Generated by Django 2.2.16 on 2020-10-14 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0035_bulkchangeenrollmentconfiguration'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccountDisableHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('comment', models.CharField(blank=True, help_text='Add a reason', max_length=255, null=True)),
                ('disabled', models.BooleanField(default=True)),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_disabled', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disable_comment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

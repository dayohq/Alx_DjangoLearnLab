# Generated by Django 5.1.6 on 2025-03-04 13:28

import django.contrib.auth.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('bookshelf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.group')),
            ],
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_view', 'Can view book'), ('can_create', 'Can create book'), ('can_edit', 'Can edit book'), ('can_delete_book', 'Can delete book')]},
        ),
    ]

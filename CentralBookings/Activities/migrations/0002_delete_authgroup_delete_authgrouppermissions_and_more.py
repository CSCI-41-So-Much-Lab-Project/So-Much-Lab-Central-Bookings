# Generated by Django 5.1.3 on 2024-12-01 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Activities', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.AlterModelOptions(
            name='activity',
            options={},
        ),
        migrations.AlterModelOptions(
            name='booking',
            options={},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={},
        ),
        migrations.AlterModelOptions(
            name='organizer',
            options={},
        ),
        migrations.AlterModelOptions(
            name='participant',
            options={},
        ),
    ]

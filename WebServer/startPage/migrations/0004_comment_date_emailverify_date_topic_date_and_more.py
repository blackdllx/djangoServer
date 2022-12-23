# Generated by Django 4.1.4 on 2022-12-23 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startPage', '0003_emailverify_master'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation data'),
        ),
        migrations.AddField(
            model_name='emailverify',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='request data'),
        ),
        migrations.AddField(
            model_name='topic',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation data'),
        ),
        migrations.AlterField(
            model_name='emailverify',
            name='link',
            field=models.CharField(max_length=500, verbose_name='token'),
        ),
        migrations.AlterField(
            model_name='forum',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation data'),
        ),
    ]

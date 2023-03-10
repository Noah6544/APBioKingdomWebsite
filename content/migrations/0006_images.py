# Generated by Django 4.1.4 on 2023-02-02 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_alter_domain_keytraits'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=150, null=True)),
                ('caption', models.TextField(blank=True, default='pictures caption', max_length=1000)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('Domain', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='content.domain')),
            ],
        ),
    ]

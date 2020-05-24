# Generated by Django 3.0.6 on 2020-05-24 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grid', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_name', models.CharField(max_length=30)),
                ('img_description', models.TextField()),
                ('photo', models.ImageField(default='', upload_to='images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grid.Category')),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grid.Editor')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grid.Location')),
            ],
        ),
    ]

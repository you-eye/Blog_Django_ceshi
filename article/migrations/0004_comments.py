# Generated by Django 2.0 on 2019-06-25 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0003_auto_20190622_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='评论日期')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article', verbose_name='文章')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='评论用户')),
            ],
            options={
                'verbose_name': '评论表',
                'verbose_name_plural': '评论表',
                'db_table': 'comments',
            },
        ),
    ]
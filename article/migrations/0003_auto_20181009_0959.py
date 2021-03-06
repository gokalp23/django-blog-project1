# Generated by Django 2.1.1 on 2018-10-09 06:59

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20181007_0139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=50, verbose_name='İsim')),
                ('comment_content', models.TextField(max_length=5000, verbose_name='Yorum')),
                ('comment_date', models.DateTimeField(auto_now_add=True, verbose_name='Yorum Tarihi')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Makaleye Resim Ekleyebilirsiniz'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='İçerik'),
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.Article', verbose_name='Yazı'),
        ),
    ]

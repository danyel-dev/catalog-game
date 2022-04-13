# Generated by Django 4.0.3 on 2022-04-13 13:34

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('core', '0005_game_created_at_game_tags_game_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date_lauch',
            field=models.DateField(verbose_name='Data de lançamento'),
        ),
        migrations.AlterField(
            model_name='game',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Gêneros'),
        ),
    ]

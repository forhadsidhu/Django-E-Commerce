# Generated by Django 3.0.4 on 2020-05-06 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_wizard_type', models.CharField(choices=[('SURVEY_WIZARD_ONE', 'survey_wizard_one'), ('SURVEY_WIZARD_TWO', 'survey_wizard_two'), ('SURVEY_WIZARD_THREE', 'survey_wizard_three')], max_length=1000)),
                ('pos_count', models.SmallIntegerField(default=0)),
                ('neg_count', models.SmallIntegerField(default=0)),
                ('total_count', models.SmallIntegerField(default=0)),
            ],
        ),
    ]
# Generated by Django 2.0.13 on 2019-05-31 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20190530_2237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, unique=True, verbose_name='Auteur')),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='author',
        ),
        migrations.AlterField(
            model_name='game',
            name='age',
            field=models.IntegerField(verbose_name='Vanaf welke leeftijd'),
        ),
        migrations.AlterField(
            model_name='game',
            name='duration',
            field=models.DurationField(help_text='Noteer het zo: [mm:ss]', verbose_name='Duur'),
        ),
        migrations.AlterField(
            model_name='game',
            name='numberofplayersmaximum',
            field=models.IntegerField(verbose_name='Maximum aantal spelers'),
        ),
        migrations.AlterField(
            model_name='game',
            name='numberofplayersminimum',
            field=models.IntegerField(verbose_name='Minimum aantal spelers'),
        ),
        migrations.AlterField(
            model_name='game',
            name='publisher',
            field=models.CharField(max_length=70, verbose_name='Uitgever'),
        ),
        migrations.AlterField(
            model_name='game',
            name='skill',
            field=models.CharField(choices=[('CR', 'Concentratie'), ('GD', 'Geduld'), ('GH', 'Geheugen'), ('HR', 'Hoofdrekenen'), ('DR', 'Durf'), ('HK', 'Herkenning'), ('RV', 'Reactievermogen')], max_length=2, verbose_name='Vaardigheid'),
        ),
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Titel'),
        ),
        migrations.AddField(
            model_name='game',
            name='authors',
            field=models.ManyToManyField(related_name='games', to='games.Author'),
        ),
    ]

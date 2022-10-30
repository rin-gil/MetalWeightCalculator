from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metal_type', models.CharField(db_index=True, max_length=10, unique=True, verbose_name='Металл')),
                ('density', models.SmallIntegerField(verbose_name='Плотность материала, кг/м3')),
            ],
            options={
                'verbose_name': 'Металл',
                'verbose_name_plural': 'Металлы',
                'ordering': ('metal_type',),
            },
        ),
        migrations.CreateModel(
            name='MetalShape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape_name', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Профиль металла',
                'verbose_name_plural': 'Профили металла',
                'ordering': ('shape_name',),
            },
        ),
        migrations.CreateModel(
            name='PageInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, unique=True, verbose_name='Название страницы')),
                ('description', models.CharField(max_length=150, verbose_name='Описание страницы')),
                ('keywords', models.CharField(max_length=250, verbose_name='Ключевые слова')),
            ],
            options={
                'verbose_name': 'Информация о страницы',
                'verbose_name_plural': 'Информация о страницах',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='MetalGrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metal_grade', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='Марка металла')),
                ('density', models.SmallIntegerField(verbose_name='Плотность сплава, кг/м3')),
                ('metal_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metalCalc.metals', verbose_name='Металл')),
            ],
            options={
                'verbose_name': 'Марка металла',
                'verbose_name_plural': 'Марки металлов',
                'ordering': ('metal_type_id', 'metal_grade'),
            },
        ),
    ]

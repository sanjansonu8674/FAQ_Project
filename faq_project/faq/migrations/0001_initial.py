from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('question_hi', models.TextField(blank=True, null=True)),
                ('question_bn', models.TextField(blank=True, null=True)),
                ('answer_hi', models.TextField(blank=True, null=True)),
                ('answer_bn', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
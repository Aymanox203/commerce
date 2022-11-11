# Generated by Django 4.1 on 2022-11-04 13:38

import auctions.util
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bider', models.CharField(max_length=50, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, default=1, max_digits=7, validators=[auctions.util.validateBid])),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bider', models.CharField(max_length=50, unique=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bider', models.CharField(max_length=50, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('image', models.URLField(blank=True, null=True)),
                ('category', models.CharField(blank=True, choices=[('0', 'All Categories'), ('1', 'Antiques'), ('2', 'Art'), ('3', 'Baby'), ('4', 'Books'), ('5', 'Business & Industrial'), ('6', 'Cameras & Photo'), ('7', 'Cell Phones & Accessories'), ('8', 'Clothing, Shoes & Accessories'), ('9', 'Coins  & Paper Money'), ('10', 'Collectibles'), ('11', 'Computers/Tablets & Networking'), ('12', 'Consumer Electronics'), ('13', 'crafts'), ('14', 'Dolls '), ('15', 'Movies'), ('16', 'Entertainment Memorabilia'), ('17', 'Gift Cards & Coupons'), ('19', 'Health & Beauty'), ('20', 'Home'), ('21', 'Jewelry'), ('22', 'Music'), ('23', 'Musical Instruments'), ('24', 'Gear'), ('25', 'Pet Supplies'), ('26', 'Pottery & Glass'), ('27', 'Real Estate'), ('28', 'Specialty Services'), ('29', 'Sporting Goods'), ('30', 'Sports Mem, Cards'), ('31', 'Tickets & Experiences'), ('32', 'Toys & Hobbies'), ('33', 'Travel'), ('34', 'Video Games & Consoles'), ('35', 'Everything Else')], default='0', max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
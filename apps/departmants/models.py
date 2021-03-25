from django.db import models
from apps.foods.models import FoodCategory
from django.core.validators import RegexValidator

phone_number_regex = RegexValidator(
    regex=r'^(\+996)\d{9}$',
    message=(
        "Телефон должен быть в формате +996[код][номер]"
    )
)

PARKING_CHOICE = (
    ('F', 'Парковка неохраняемая, бесплатная'),
    ('Pay', 'Парковка охраняемая, небесплатная'),
    ('Not', 'Парковки нет'),
)


class Department(models.Model):
    title = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name='Название место'
    )
    image = models.ImageField(
        upload_to='department',
        null=True, blank=True,
        verbose_name='Изображение заведения'
    )
    location = models.CharField(
        max_length=255,
        verbose_name='Место расположения'
    )
    food = models.ManyToManyField(
        FoodCategory,
        related_name='department_food',
        blank=True,
        verbose_name='Кухня'
    )
    check = models.CharField(
        max_length=255,
        verbose_name='Средний счет'
    )
    seats = models.PositiveIntegerField(
        verbose_name='Количество мест',
        default=0,
        blank=True,
        null=True
    )
    parking = models.CharField(
        max_length=255,
        choices=PARKING_CHOICE,
        verbose_name='Парковка'
    )
    music = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name="Музыка"
    )
    facebook_profile = models.URLField(
        max_length=255,
        blank=True, null=True,
        verbose_name='Ссылка на Facebook'
    )
    insta_profile = models.URLField(
        max_length=255,
        blank=True, null=True,
        verbose_name='Ссылка на Instagram'
    )
    web_profile = models.URLField(
        max_length=255,
        blank=True, null=True,
        verbose_name='Ссылка на Website'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True, null=True,
    )

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.title


class PhoneNumber(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='phone_number',
        verbose_name='Заведения'
    )
    number = models.CharField(
        max_length=255,
        verbose_name='Телефон',
        validators=[phone_number_regex],
        null=True, blank=True
    )

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f"{self.department} -- {self.number}"


class Booking(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        verbose_name='Место расположения',
        related_name='booking'
    )
    day = models.DateField(verbose_name='Дата')
    people = models.PositiveIntegerField(
        verbose_name='Число людей',
    )
    number = models.CharField(
        max_length=255,
        validators=[phone_number_regex],
        verbose_name='Телефон',
        blank=True, null=True
    )

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f"{self.department.title} book's {self.day}"

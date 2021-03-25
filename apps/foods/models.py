from django.db import models


class FoodCategory(models.Model):
    main_title = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name='Название меню'
    )
    title = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name='Категорий кухни'
    )

    def __str__(self):
        return self.title


class Food(models.Model):
    title = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name='Название еды'
    )
    category = models.ForeignKey(
        FoodCategory,
        related_name='food_category',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Категорий'
    )
    price = models.PositiveSmallIntegerField(verbose_name='Цена', default=0)
    description = models.TextField(verbose_name='Описание еды')

    def __str__(self):
        return f"{self.title} -- {self.category.title} -- {self.price}c"

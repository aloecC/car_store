from django.db import models


class Car(models.Model):
    """Модель машины"""
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'машина'
        verbose_name_plural = 'машины'


class Moto(models.Model):
    """Модель мотоцикла"""
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'мотоцикл'
        verbose_name_plural = 'мотоциклы'


class Mileage(models.Model):
    """Модель пробега"""
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True, related_name='mileage')
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, null=True, blank=True, related_name='mileage')

    mileage = models.PositiveIntegerField(verbose_name='пробег')
    year = models.PositiveSmallIntegerField(verbose_name='год регистрации')

    def __str__(self):
        return f'{self.moto if self.moto else self.car} - {self.mileage} {self.year}'

    class Meta:
        verbose_name = 'пробег'
        verbose_name_plural = 'пробег'
        ordering = ('-year',)

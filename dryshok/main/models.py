from django.db import models

class Animals(models.Model):
    """Модель для карточек животных"""

    class kategori_pol(models.TextChoices):
        men = 'Men', 'Мальчик'
        women = 'Women', 'Девочка'

    class kategori_tip(models.TextChoices):
        dog = 'Dog', 'Собака'
        cat = 'Cat', 'Кошка'

    name = models.CharField('Имя', max_length=30)
    age = models.CharField('Возраст', max_length=20)
    pol = models.CharField('Пол', choices=kategori_pol.choices)
    tip = models.CharField('Тип животного', choices=kategori_tip.choices)
    text = models.TextField('Описание')
    photo = models.CharField('Фото')

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'

    def __str__(self):
        return self.name


class VolunteerApplication(models.Model):
    """Модель для заявок волонтеров"""

    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('processing', 'В обработке'),
        ('approved', 'Одобрена'),
        ('rejected', 'Отклонена'),
    ]

    full_name = models.CharField('ФИО', max_length=200)
    email = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=20)
    age = models.PositiveIntegerField('Возраст', null=True, blank=True)
    experience = models.TextField('Опыт работы с животными', blank=True)
    motivation = models.TextField('Мотивация', blank=True)
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Заявка волонтера'
        verbose_name_plural = 'Заявки волонтеров'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.created_at.strftime('%d.%m.%Y')}"


class News(models.Model):
    """Модель для новостей"""

    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Текст новости')
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
    image = models.CharField('Фото', max_length=500, blank=True, null=True)
    is_published = models.BooleanField('Опубликовано', default=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date']  # Сначала новые

    def __str__(self):
        return self.title


class Report(models.Model):
    """Модель для отчетности о расходах/сборах"""

    title = models.CharField('Заголовок', max_length=200)
    description = models.TextField('Описание', help_text='На что были потрачены средства или что было собрано')
    amount = models.DecimalField('Сумма', max_digits=10, decimal_places=2, help_text='Сумма в рублях')
    report_type = models.CharField('Тип отчета', max_length=20, choices=[
        ('expense', 'Расход'),
        ('income', 'Сбор'),
    ], default='expense')
    date = models.DateTimeField('Дата', auto_now_add=True)
    receipt_image = models.CharField('Фото чека/документа', max_length=500, blank=True, null=True)
    is_published = models.BooleanField('Опубликовано', default=True)

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчетность'
        ordering = ['-date']

    def __str__(self):
        return f"{self.get_report_type_display()}: {self.title} - {self.amount} руб."
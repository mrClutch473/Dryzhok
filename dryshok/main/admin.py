from django.contrib import admin
from .models import VolunteerApplication, Animals
from .models import News

#Заявка волонтера
@admin.register(VolunteerApplication)
class VolunteerApplicationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['full_name', 'email', 'phone']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Контактная информация', {
            'fields': ('full_name', 'email', 'phone', 'age')
        }),
        ('Дополнительная информация', {
            'fields': ('experience', 'motivation')
        }),
        ('Статус', {
            'fields': ('status',)
        }),
        ('Системная информация', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


#База собак
@admin.register(Animals)
class AnimalsAdmin(admin.ModelAdmin):
    """Настройка отображения модели Animals в админ-панели"""

    # Поля, отображаемые в списке записей (убрано created_at)
    list_display = [
        'id',
        'name',
        'age',
        'pol',
        'tip',
        'get_photo_preview',
    ]

    # Поля-ссылки (при клике открывается редактирование)
    list_display_links = ['name', 'id']

    # Поля для фильтрации (убрано created_at)
    list_filter = ['tip', 'pol']

    # Поля для поиска
    search_fields = ['name', 'text', 'age']

    # Количество записей на странице
    list_per_page = 20

    # Поля, которые будут отображаться в форме редактирования
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'age', 'pol', 'tip')
        }),
        ('Подробное описание', {
            'fields': ('text',),
            'classes': ('wide',)
        }),
        ('Фотография', {
            'fields': ('photo',),
            'description': 'Добавьте ссылку на фото животного'
        }),
    )

    # Поля, которые доступны только для чтения (убрано created_at, updated_at)
    readonly_fields = ['get_photo_preview']

    # Сортировка по умолчанию (по имени, т.к. created_at нет)
    ordering = ['name']

    # Действия с выбранными записями
    actions = ['mark_as_dog', 'mark_as_cat', 'mark_as_male', 'mark_as_female']

    def get_photo_preview(self, obj):
        """Отображение превью фото в списке"""
        if obj.photo:
            return f'<img src="{obj.photo}" width="50" height="50" style="border-radius: 8px; object-fit: cover;" />'
        return 'Нет фото'

    get_photo_preview.short_description = 'Фото'
    get_photo_preview.allow_tags = True

    def mark_as_dog(self, request, queryset):
        """Массовое изменение типа на 'Собака'"""
        queryset.update(tip='Dog')

    mark_as_dog.short_description = 'Отметить выбранные как "Собака"'

    def mark_as_cat(self, request, queryset):
        """Массовое изменение типа на 'Кошка'"""
        queryset.update(tip='Cat')

    mark_as_cat.short_description = 'Отметить выбранные как "Кошка"'

    def mark_as_male(self, request, queryset):
        """Массовое изменение пола на 'Мальчик'"""
        queryset.update(pol='Men')

    mark_as_male.short_description = 'Отметить выбранные как "Мальчик"'

    def mark_as_female(self, request, queryset):
        """Массовое изменение пола на 'Девочка'"""
        queryset.update(pol='Women')

    mark_as_female.short_description = 'Отметить выбранные как "Девочка"'

#НОВОСТИ
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'is_published']
    list_filter = ['is_published', 'date']
    search_fields = ['title', 'text']
    list_editable = ['is_published']
    readonly_fields = ['date']
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'text', 'image')
        }),
        ('Публикация', {
            'fields': ('is_published', 'date')
        }),
    )

from .models import Report

#Отчетность
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['title', 'report_type', 'amount', 'date', 'is_published']
    list_filter = ['report_type', 'is_published', 'date']
    search_fields = ['title', 'description']
    list_editable = ['is_published']
    readonly_fields = ['date']
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'amount', 'report_type')
        }),
        ('Документы', {
            'fields': ('receipt_image',)
        }),
        ('Публикация', {
            'fields': ('is_published', 'date')
        }),
    )
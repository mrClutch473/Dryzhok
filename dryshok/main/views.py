from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
import json
from .forms import VolunteerApplicationForm
from .models import VolunteerApplication
from .models import Animals
from .models import News
from .models import Report

# Create your views here.
def vivod_glav_str(request):
    return render(request, "main/glav_str.html")

def animals_page(request):
    """Страница с животными"""
    animals = Animals.objects.all()
    return render(request, "main/animals.html", {'animals': animals})


def submit_volunteer_application(request):
    """Обработка заявки волонтера"""
    if request.method == 'POST':
        try:
            # Получаем данные из POST запроса
            data = json.loads(request.body)
            form = VolunteerApplicationForm(data)

            if form.is_valid():
                # Сохраняем заявку
                application = form.save()

                # Отправляем уведомление на email
                send_mail(
                    f'Новая заявка волонтера от {application.full_name}',
                    f"""
                    Поступила новая заявка на волонтерство:

                    ФИО: {application.full_name}
                    Email: {application.email}
                    Телефон: {application.phone}
                    Возраст: {application.age}

                    Опыт: {application.experience}
                    Мотивация: {application.motivation}

                    Дата заявки: {application.created_at.strftime('%d.%m.%Y %H:%M')}
                    """,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                    fail_silently=False,
                )

                return JsonResponse({
                    'success': True,
                    'message': 'Спасибо! Ваша заявка успешно отправлена. Мы свяжемся с вами в ближайшее время.'
                })
            else:
                return JsonResponse({
                    'success': False,
                    'errors': form.errors
                }, status=400)

        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            }, status=500)

    return JsonResponse({'success': False, 'message': 'Метод не поддерживается'}, status=405)

def news_page(request):
    """Страница новостей"""
    news_list = News.objects.filter(is_published=True).order_by('-date')
    return render(request, "main/news.html", {'news_list': news_list})


def reports_page(request):
    """Страница отчетности"""
    reports = Report.objects.filter(is_published=True).order_by('-date')

    # Подсчет сумм
    total_income = sum(r.amount for r in reports if r.report_type == 'income')
    total_expense = sum(r.amount for r in reports if r.report_type == 'expense')
    balance = total_income - total_expense

    context = {
        'reports': reports,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
    }
    return render(request, "main/reports.html", context)
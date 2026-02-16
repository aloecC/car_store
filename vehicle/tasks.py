from celery import shared_task
from django.core.mail import send_mail

from vehicle.models import Car, Moto


@shared_task
def check_mileage(pk, model):
    if model == 'Car':
        instance = Car.objects.filter(pk=pk).first()
    else:
        instance = Moto.objects.filter(pk=pk).first()

    if instance:
        prev_mileage = -1
        for m in instance.mileage.all():
            if prev_mileage == -1:
                prev_mileage = m.mileage

            else:
                if prev_mileage < m.mileage:
                    print('Неверный пробег')
                    break

@shared_task
def check_filter():

    filter_price = {'amount__lte': 1500}

    if Car.objects.filter(**filter_price).exists():
        print('отчет по фильтру')
        #send_mail(
        #    subject= 'Машины по вашему запросу',
        #    message= 'У нас появились новинки по вашему фильтру',
        #    from_email='admin@mail.ru',
        #    recipient_list=[user.email]

        #)
    # for filter_item in UserFilter.objects.all
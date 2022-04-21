from .models import Client
from django.conf import settings
from django.core.mail import send_mail


class ClientHandler:
    def __init__(self, request):
        self.name = request.POST.get('name')
        self.mail = request.POST.get('mail')
        self.phone = request.POST.get('phone')
        self.add_to_db()
        self.send_mail()

    def add_to_db(self):
        new_client = Client.objects.create(name=self.name, mail=self.mail, phone=self.phone)
        new_client.save()

    def send_mail(self):
        client = f'Имя: ' + self.name + 'Почта: ' + self.mail + 'Телефон: ' + self.phone
        send_mail('Новая заявка', client, settings.EMAIL_HOST_USER, ['iqworks@bk.ru'])


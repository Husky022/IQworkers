from .models import Client


class ClientHandler:
    def __init__(self, request):
        self.name = request.POST.get('name')
        self.mail = request.POST.get('mail')
        self.phone = request.POST.get('phone')
        self.add_to_db()

    def add_to_db(self):
        new_client = Client.objects.create(name=self.name, mail=self.mail, phone=self.phone)
        new_client.save()

    def send_mail(self):
        pass


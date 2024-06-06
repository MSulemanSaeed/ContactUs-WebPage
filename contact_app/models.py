from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    class StatusChoices(models.TextChoices):
        BUYER = 'B', 'Buyer'
        SUPPLIER = 'S', 'Supplier'
    status = models.CharField(max_length=1, choices=StatusChoices.choices, default=StatusChoices.BUYER)
    message_field = models.TextField()

    def __str__(self) -> str:
        return self.name
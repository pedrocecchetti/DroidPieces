import uuid
from django.db import models

class Address(models.Model):

    STATES = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]
    

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    country = models.CharField(max_length=25, default='Brasil', verbose_name='País')
    city = models.CharField(max_length=30, verbose_name='Cidade')
    state = models.CharField(max_length=2, choices=STATES, verbose_name="Estados")
    street = models.CharField(max_length=50, verbose_name='Logradouro')
    number = models.PositiveIntegerField(verbose_name='Número')
    zip_code = models.CharField(max_length=9, help_text='XXXXX-XXX', verbose_name='CEP') 

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

    def __str__(self):
        return "{},{} / {} , {} - {} ".format(self.street, self.number, self.city, self.state, self.country)

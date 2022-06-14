from django.db import models

# Create your models here.

voto_rei = [
    ('2021305180', 'guilherme'),
    ('2020302405', 'ian'),
    ('2020307045', 'daniel'),
    ('2021303766', 'kaua'),
    ('2021303701', 'gilmar'),
]

voto_rainha = [
    ('2020301800', 'alana'),
    ('2022306898', 'khetelen'),
    ('2021303828', 'milena'),
    ('2021303864', 'monik'),
]

class Alunos(models.Model):
    matricula = models.IntegerField(db_column='matricula', primary_key=True)
    nome = models.CharField(db_column='nome', max_length=255, blank=True, null=True)
    voto_rei = models.CharField(db_column='voto_rei', choices=voto_rei, max_length=10, blank=True, null=True)
    voto_rainha = models.CharField(db_column='voto_rainha', choices=voto_rainha, max_length=10, blank=True, null=True)
    statusvoto = models.CharField(db_column='statusVoto', max_length=1, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'alunos'
    def __str__(self):
        return self.nome
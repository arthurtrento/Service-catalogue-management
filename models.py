from django.db import models

    
class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

class Atendentes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    login = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'atendentes'
    def __str__(self) -> str:
        return self.login
        
class Resolvedores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resolvedores'
    def __str__(self) -> str:
        return self.nome

class Servicos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    categoria_n0 = models.CharField(db_column='categoria_N0', max_length=100)  # Field name made lowercase.
    categoria_n1 = models.CharField(db_column='categoria_N1', max_length=100)  # Field name made lowercase.
    categoria_n2 = models.CharField(db_column='categoria_N2', max_length=100)  # Field name made lowercase.
    categoria_n3 = models.CharField(db_column='categoria_N3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    grupo_responsavel = models.CharField(max_length=100)
    tempo_unico = models.CharField(max_length=100, blank=True, null=True)
    tempo_centro = models.CharField(db_column='tempo_CENTRO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tempo_metropolitana = models.CharField(db_column='tempo_METROPOLITANA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tempo_interior = models.CharField(db_column='tempo_INTERIOR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tempo_via_telefone = models.CharField(db_column='tempo_VIA_TELEFONE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tempo_via_web = models.CharField(db_column='tempo_VIA_WEB', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tempo_particular = models.CharField(db_column='tempo_PARTICULAR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tempo = models.CharField(max_length=100, blank=True, null=True)
    servico_completo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicos'
    def __str__(self) -> str:
        return self.nome

        
class Inserir(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    data_criação = models.DateTimeField()
    nome = models.CharField(db_column='Nome', max_length=60)  # Field name made lowercase.
    telefone = models.CharField(db_column='Telefone', max_length=15)  # Field name made lowercase.
    setor = models.CharField(db_column='Setor', max_length=150)  # Field name made lowercase.
    tipo = models.CharField(max_length=20, blank=True, null=True)
    area = models.CharField(max_length=20, blank=True, null=True)
    categoria_n0 = models.CharField(db_column='categoria_N0', max_length=100, blank=True, null=True)  # Field name made lowercase.
    categoria_n1 = models.CharField(db_column='categoria_N1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    categoria_n2 = models.CharField(db_column='categoria_N2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    categoria_n3 = models.CharField(db_column='categoria_N3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sla = models.CharField(max_length=100, blank=True, null=True)
    resolvedores = models.CharField(max_length=100, blank=True, null=True)
    gestores = models.CharField(max_length=100, blank=True, null=True)
    comentarios = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inserir'
    def __str__(self) -> str:
        return self.nome


class Modificar(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    data_criação = models.DateTimeField()
    nome = models.CharField(db_column='Nome', max_length=60)  # Field name made lowercase.
    telefone = models.CharField(db_column='Telefone', max_length=15)  # Field name made lowercase.
    serviço_atual = models.CharField(db_column='Serviço_atual', max_length=255)  # Field name made lowercase.
    setor = models.CharField(db_column='Setor', max_length=150)  # Field name made lowercase.
    tipo = models.CharField(max_length=20, blank=True, null=True)
    area = models.CharField(max_length=20, blank=True, null=True)
    categoria_n0 = models.CharField(db_column='categoria_N0', max_length=100, blank=True, null=True)  # Field name made lowercase.
    categoria_n1 = models.CharField(db_column='categoria_N1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    categoria_n2 = models.CharField(db_column='categoria_N2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    categoria_n3 = models.CharField(db_column='categoria_N3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sla = models.CharField(max_length=100, blank=True, null=True)
    resolvedores = models.CharField(max_length=100, blank=True, null=True)
    gestores = models.CharField(max_length=100, blank=True, null=True)
    comentarios = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modificar'
    def __str__(self) -> str:
        return self.nome

        
class Excluir(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    data_criação = models.DateTimeField()
    nome = models.CharField(db_column='Nome', max_length=60)  # Field name made lowercase.
    telefone = models.CharField(db_column='Telefone', max_length=15)  # Field name made lowercase.
    setor = models.CharField(db_column='Setor', max_length=150)  # Field name made lowercase.
    serviço = models.CharField(db_column='Serviço', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'excluir'
    def __str__(self) -> str:
        return self.nome

        
    # def __str__(self): 
    #     """String for representing the Model object."""
    #     return self.name
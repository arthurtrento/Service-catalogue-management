# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Atendentes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    login = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'atendentes'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Excluir(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    data_criação = models.DateTimeField()
    nome = models.CharField(db_column='Nome', max_length=60)  # Field name made lowercase.
    telefone = models.CharField(db_column='Telefone', max_length=13)  # Field name made lowercase.
    setor = models.CharField(db_column='Setor', max_length=45)  # Field name made lowercase.
    serviço = models.CharField(db_column='Serviço', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'excluir'


class Inserir(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    data_criação = models.DateTimeField()
    nome = models.CharField(db_column='Nome', max_length=60)  # Field name made lowercase.
    telefone = models.CharField(db_column='Telefone', max_length=13)  # Field name made lowercase.
    setor = models.CharField(db_column='Setor', max_length=45)  # Field name made lowercase.
    tipo = models.CharField(max_length=10, blank=True, null=True)
    area = models.CharField(max_length=10, blank=True, null=True)
    categoria_n0 = models.CharField(db_column='categoria_N0', max_length=100, blank=True, null=True)  # Field name made lowercase.
    categoria_n1 = models.CharField(db_column='categoria_N1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    categoria_n2 = models.CharField(db_column='categoria_N2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    categoria_n3 = models.CharField(db_column='categoria_N3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sla = models.CharField(max_length=100, blank=True, null=True)
    resolvedores = models.CharField(max_length=100, blank=True, null=True)
    gestores = models.CharField(max_length=100, blank=True, null=True)
    comentarios = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inserir'


class Modificar(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    data_criação = models.DateTimeField()
    nome = models.CharField(db_column='Nome', max_length=60)  # Field name made lowercase.
    telefone = models.CharField(db_column='Telefone', max_length=13)  # Field name made lowercase.
    serviço_atual = models.CharField(db_column='Serviço_atual', max_length=255)  # Field name made lowercase.
    setor = models.CharField(db_column='Setor', max_length=45)  # Field name made lowercase.
    tipo = models.CharField(max_length=10, blank=True, null=True)
    area = models.CharField(max_length=10, blank=True, null=True)
    categoria_n0 = models.CharField(db_column='categoria_N0', max_length=100, blank=True, null=True)  # Field name made lowercase.
    categoria_n1 = models.CharField(db_column='categoria_N1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    categoria_n2 = models.CharField(db_column='categoria_N2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    categoria_n3 = models.CharField(db_column='categoria_N3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sla = models.CharField(max_length=100, blank=True, null=True)
    resolvedores = models.CharField(max_length=100, blank=True, null=True)
    gestores = models.CharField(max_length=100, blank=True, null=True)
    comentarios = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modificar'


class Resolvedores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resolvedores'


class Servicos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=10)
    area = models.CharField(max_length=10)
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

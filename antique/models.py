from django.db import models
from django.utils.translation import gettext_lazy as _


class Antique(models.Model):
    antique_id = models.BigAutoField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    last_posting_date = models.DateTimeField()
    creaction_date = models.CharField(max_length=255, blank=True, null=True)
    room = models.ForeignKey('Room', models.DO_NOTHING, blank=True, null=True)
    antique_condition = models.ForeignKey('AntiqueCondition', models.DO_NOTHING)
    antique_production = models.ForeignKey('AntiqueProduction', models.DO_NOTHING)
    status = models.ForeignKey('AntiqueStatus', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'antique'
        verbose_name = _('Антиквариат')
        verbose_name_plural = _('Антиквариат')

    def __str__(self):
        return f'{self.antique_id}: {self.antique_production.name}'


class AntiqueCondition(models.Model):
    antique_condition_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=45)
    recommended_actions = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'antique_condition'
        verbose_name = _('Состояние антиквариата')
        verbose_name_plural = _('Состояния антиквариата')

    def __str__(self):
        return f'{self.antique_condition_id}: {self.name}'


class AntiqueExhibition(models.Model):
    antique = models.OneToOneField(Antique, models.DO_NOTHING,
                                   primary_key=True)  # The composite primary key (antique_id, exhibition_id) found, that is not supported. The first column is selected.
    exhibition = models.ForeignKey('Exhibition', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'antique_exhibition'
        unique_together = (('antique', 'exhibition'),)
        verbose_name = _('Выставка - Антиквариант')
        verbose_name_plural = _('Выставки - Антиквариат')

    def __str__(self):
        return f'{self.antique} - {self.exhibition}'


class AntiqueProduction(models.Model):
    antique_production_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    manufacturer = models.ForeignKey('Manufacturer', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'antique_production'
        verbose_name = _('Продукт антиквариата')
        verbose_name_plural = _('Продукты антиквариата')

    def __str__(self):
        return f'{self.antique_production_id}: {self.name}'


class AntiqueProductionAntiqueType(models.Model):
    antique = models.OneToOneField(AntiqueProduction, models.DO_NOTHING,
                                   primary_key=True)  # The composite primary key (antique_id, antique_type_id) found, that is not supported. The first column is selected.
    antique_type = models.ForeignKey('AntiqueType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'antique_production_antique_type'
        unique_together = (('antique', 'antique_type'),)
        verbose_name = _('Продукт антиквариата - Тип антиквариат')
        verbose_name_plural = _('Продукты антиквариата - Типы антиквариата')

    def __str__(self):
        return f'{self.antique} - {self.antique_type}'


class AntiqueProductionAuthor(models.Model):
    antique_production = models.OneToOneField(AntiqueProduction, models.DO_NOTHING,
                                              primary_key=True)  # The composite primary key (antique_production_id, author_id) found, that is not supported. The first column is selected.
    author = models.ForeignKey('Author', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'antique_production_author'
        unique_together = (('antique_production', 'author'),)
        verbose_name = _('Продукт антиквариата - Автор антиквариата')
        verbose_name_plural = _('Продукты антиквариата - Авторы антиквариата')

    def __str__(self):
        return f'{self.antique_production} - {self.author}'


class AntiqueStatus(models.Model):
    antique_status_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'antique_status'
        verbose_name = _('Статус антиквариата')
        verbose_name_plural = _('Статусы антиквариата')

    def __str__(self):
        return f'{self.antique_status_id}: {self.name}'


class AntiqueType(models.Model):
    antique_type_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=45)
    min_temperature = models.FloatField()
    max_temperature = models.FloatField()
    min_humidity = models.FloatField()
    max_humidity = models.FloatField()

    class Meta:
        managed = False
        db_table = 'antique_type'
        verbose_name = _('Тип антиквариата')
        verbose_name_plural = _('Типы антиквариата')

    def __str__(self):
        return f'{self.antique_type_id}: {self.name}'


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


class Author(models.Model):
    author_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    patronymic = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    biography = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'author'
        verbose_name = _('Автор')
        verbose_name_plural = _('Авторы')

    def __str__(self):
        return f'{self.author_id}: {self.surname} {self.name} {self.patronymic}'


class AuthorAuthorSpecialization(models.Model):
    author = models.OneToOneField(Author, models.DO_NOTHING,
                                  primary_key=True)  # The composite primary key (author_id, author_specialization_id) found, that is not supported. The first column is selected.
    author_specialization = models.ForeignKey('AuthorSpecialization', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'author_author_specialization'
        unique_together = (('author', 'author_specialization'),)
        verbose_name = _('Автор - Специализация автора')
        verbose_name_plural = _('Авторы - Специализации автора')

    def __str__(self):
        return f'{self.author} - {self.author_specialization}'


class AuthorSpecialization(models.Model):
    author_specialization_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'author_specialization'
        verbose_name = _('Специализация автора')
        verbose_name_plural = _('Специализации автора')

    def __str__(self):
        return f'{self.author_specialization_id}: {self.name}'


class Client(models.Model):
    client_id = models.BigAutoField(primary_key=True)
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=25)
    email = models.CharField(max_length=255)
    client_discount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'client'
        verbose_name = _('Клиент')
        verbose_name_plural = _('Клиенты')

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'


class ClimateEquipment(models.Model):
    name = models.CharField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    climate_equipment_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'climate_equipment'
        verbose_name = _('Климатическое оборудование')
        verbose_name_plural = _('Климатические оборудования')

    def __str__(self):
        return f'{self.climate_equipment_id}: {self.name}'


class ClimateEquipmentRoom(models.Model):
    climate_equipment = models.OneToOneField(ClimateEquipment, models.DO_NOTHING,
                                             primary_key=True)  # The composite primary key (climate_equipment_id, room_id) found, that is not supported. The first column is selected.
    room = models.ForeignKey('Room', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'climate_equipment_room'
        unique_together = (('climate_equipment', 'room'),)
        verbose_name = _('Климатическое оборудование - Помещение')
        verbose_name_plural = _('Климатические оборудования - Помещения')

    def __str__(self):
        return f'{self.climate_equipment} - {self.room}'


class Contract(models.Model):
    contract_id = models.BigAutoField(primary_key=True)
    details = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'contract'
        verbose_name = _('Договор')
        verbose_name_plural = _('Договоры')

    def __str__(self):
        return f'{self.contract_id}: {self.start_date}-{self.end_date} {self.client}'


class ContractAntique(models.Model):
    contracrt = models.OneToOneField(Contract, models.DO_NOTHING,
                                     primary_key=True)  # The composite primary key (contracrt_id, antique_id) found, that is not supported. The first column is selected.
    antique = models.ForeignKey(Antique, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'contract_antique'
        unique_together = (('contracrt', 'antique'),)
        verbose_name = _('Договор - Антиквариат')
        verbose_name_plural = _('Договоры - Антиквариат')

    def __str__(self):
        return f'{self.contracrt} - {self.antique}'


class ContractEmployee(models.Model):
    contract = models.OneToOneField(Contract, models.DO_NOTHING,
                                    primary_key=True)  # The composite primary key (contract_id, employee_id) found, that is not supported. The first column is selected.
    employee = models.ForeignKey('Employee', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'contract_employee'
        unique_together = (('contract', 'employee'),)
        verbose_name = _('Договор - Сотрудник')
        verbose_name_plural = _('Договоры - Сотрудники')

    def __str__(self):
        return f'{self.contract} - {self.employee}'


class ContractServiceType(models.Model):
    contract = models.OneToOneField(Contract, models.DO_NOTHING,
                                    primary_key=True)  # The composite primary key (contract_id, service_type_id) found, that is not supported. The first column is selected.
    service_type = models.ForeignKey('ServiceType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'contract_service_type'
        unique_together = (('contract', 'service_type'),)
        verbose_name = _('Договор - Тип услуги')
        verbose_name_plural = _('Договоры - Типы услуг')

    def __str__(self):
        return f'{self.contract} - {self.service_type}'


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


class Employee(models.Model):
    employee_id = models.BigAutoField(primary_key=True)
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255, blank=True, null=True)
    passport_series = models.CharField(max_length=4)
    passport_number = models.CharField(max_length=6)
    gender = models.CharField(max_length=1)
    phone_number = models.CharField(max_length=25)
    position = models.ForeignKey('Position', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employee'
        verbose_name = _('Сотрудник')
        verbose_name_plural = _('Сотрудники')

    def __str__(self):
        return f'{self.employee_id}: {self.surname} {self.name} {self.patronymic}'


class Exhibition(models.Model):
    exhibition_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=45)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField()
    room = models.ForeignKey('Room', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'exhibition'
        verbose_name = _('Выставка')
        verbose_name_plural = _('Выставки')

    def __str__(self):
        return f'{self.exhibition_id}: {self.name}'


class ExhibitionEmployee(models.Model):
    exhibition = models.OneToOneField(Exhibition, models.DO_NOTHING,
                                      primary_key=True)  # The composite primary key (exhibition_id, employee_id) found, that is not supported. The first column is selected.
    employee = models.ForeignKey(Employee, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'exhibition_employee'
        unique_together = (('exhibition', 'employee'),)
        verbose_name = _('Выставка - Сотрудник')
        verbose_name_plural = _('Выставки - Сотрудники')

    def __str__(self):
        return f'{self.exhibition} - {self.employee}'


class Manufacturer(models.Model):
    manufacturer_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=45, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacturer'
        verbose_name = _('Состояние антиквариата')
        verbose_name_plural = _('Состояния антиквариата')

    def __str__(self):
        return f'{self.manufacturer_id}: {self.name}'


class Position(models.Model):
    position_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=45)
    salary = models.DecimalField(max_digits=9, decimal_places=2)
    responsibilities = models.TextField()
    requirements = models.TextField()

    class Meta:
        managed = False
        db_table = 'position'
        verbose_name = _('Должность')
        verbose_name_plural = _('Должности')

    def __str__(self):
        return f'{self.position_id}: {self.name}'


class Room(models.Model):
    room_id = models.BigAutoField(primary_key=True)
    address = models.CharField(max_length=255)
    area = models.FloatField()
    phone_number = models.CharField(max_length=25)
    chief = models.ForeignKey(Employee, models.DO_NOTHING, db_column='chief')

    class Meta:
        managed = False
        db_table = 'room'
        verbose_name = _('Помещение')
        verbose_name_plural = _('Помещения')

    def __str__(self):
        return f'{self.room_id}: {self.address}'


class RoomInspectionSchedule(models.Model):
    room_inspection_schedule_id = models.IntegerField(primary_key=True)
    temperature = models.FloatField(blank=True, null=True)
    humidity = models.FloatField(blank=True, null=True)
    room = models.ForeignKey(Room, models.DO_NOTHING, blank=True, null=True)
    schedule_date_inspections = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room_inspection_schedule'
        verbose_name = _('Проверка помещения')
        verbose_name_plural = _('Проверки помещения')

    def __str__(self):
        return f'{self.room_inspection_schedule_id}: {self.room} {self.schedule_date_inspections}'


class RoomRoomType(models.Model):
    room = models.OneToOneField(Room, models.DO_NOTHING,
                                primary_key=True)  # The composite primary key (room_id, room_type_id) found, that is not supported. The first column is selected.
    room_type = models.ForeignKey('RoomType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'room_room_type'
        unique_together = (('room', 'room_type'),)
        verbose_name = _('Помещение - Тип помещения')
        verbose_name_plural = _('Помещения - Типы помещения')

    def __str__(self):
        return f'{self.room} - {self.room_type}'


class RoomType(models.Model):
    room_type_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'room_type'
        verbose_name = _('Тип помещения')
        verbose_name_plural = _('Типы помещения')

    def __str__(self):
        return f'{self.room_type_id}: {self.name}'


class ServiceType(models.Model):
    service_type_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=55)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'service_type'
        verbose_name = _('Тип услуги')
        verbose_name_plural = _('Типы услуги')

    def __str__(self):
        return f'{self.service_type_id}: {self.name}'


class UsersUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    patronymic = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'users_user'


class UsersUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_groups'
        unique_together = (('user', 'group'),)


class UsersUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_user_permissions'
        unique_together = (('user', 'permission'),)

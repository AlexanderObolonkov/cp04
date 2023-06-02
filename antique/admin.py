from django.contrib import admin

from antique.models import (Antique, AntiqueProduction, AntiqueCondition, AntiqueExhibition,
                            AntiqueProductionAntiqueType, AntiqueProductionAuthor, AntiqueStatus,
                            AntiqueType, Author, AuthorAuthorSpecialization, AuthorSpecialization,
                            Client, ClimateEquipment, ClimateEquipmentRoom, Contract, ContractAntique,
                            ContractEmployee, ContractServiceType, Exhibition, ExhibitionEmployee,
                            Manufacturer, Position, Room, RoomInspectionSchedule, RoomRoomType,
                            RoomType, ServiceType)


admin.site.register(Antique)
admin.site.register(AntiqueProduction)
admin.site.register(AntiqueCondition)
admin.site.register(AntiqueExhibition)
admin.site.register(AntiqueProductionAntiqueType)
admin.site.register(AntiqueProductionAuthor)
admin.site.register(AntiqueStatus)
admin.site.register(AntiqueType)
admin.site.register(Author)
admin.site.register(AuthorAuthorSpecialization)
admin.site.register(AuthorSpecialization)
admin.site.register(Client)
admin.site.register(ClimateEquipment)
admin.site.register(ClimateEquipmentRoom)
admin.site.register(Contract)
admin.site.register(ContractAntique)
admin.site.register(ContractEmployee)
admin.site.register(ContractServiceType)
admin.site.register(Exhibition)
admin.site.register(ExhibitionEmployee)
admin.site.register(Manufacturer)
admin.site.register(Position)
admin.site.register(Room)
admin.site.register(RoomInspectionSchedule)
admin.site.register(RoomRoomType)
admin.site.register(RoomType)
admin.site.register(ServiceType)

from django.contrib import admin

# Register your models here.


from .models import SystemName

admin.site.register(SystemName)
# admin.site.register(SystemInformation)
# admin.site.register(DiskInformation)
# admin.site.register(MemoryInformation)
# admin.site.register(CpuInformation)
# admin.site.register(BootTime)
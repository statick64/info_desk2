from django.db import models
import uuid
# Create your models here.




# class SystemInformation(models.Model):

#     pc_name = models.CharField(max_length=250)
#     release = models.CharField(max_length=250)
#     version = models.CharField(max_length=250)
#     machine = models.CharField(max_length=250)
#     processor = models.CharField(max_length=250)


# class CpuInformation(models.Model):
#     # cpu_info = models.ForeignKey(SystemName, on_delete=models.CASCADE, related_name='cpu_name_information')
#     id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
#     total_cores = models.CharField(max_length=250)
#     max_frequency = models.CharField(max_length=250)
#     current_frequency = models.CharField(max_length=250)
#     total_cpu_usage = models.IntegerField()


# class MemoryInformation(models.Model):
#     # memory_info = models.OneToOneField(SystemName, on_delete=models.CASCADE,related_name='memory_name_information' )
#     id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
#     total_memory = models.CharField(max_length=250)
#     free_memory  = models.CharField(max_length=250)
#     used_memory  = models.CharField(max_length=250)
#     memory_percentage = models.IntegerField()

# class DiskInformation(models.Model):
#     # disk_info = models.ForeignKey(SystemName, on_delete=models.CASCADE, related_name= 'disk_name_information')
#     id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
#     total_size = models.CharField(max_length=250)
#     used = models.CharField(max_length=250)
#     free = models.CharField(max_length=250)
#     disk_percentage = models.IntegerField()

# class BootTime(models.Model):
#     # boot_info = models.ForeignKey(SystemName, on_delete=models.CASCADE, related_name= 'boot_name_information')
#     id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
#     pc_boot_time = models.CharField(max_length=250)


class SystemName(models.Model):
    sys_name = models.CharField(primary_key=True, max_length=250)
    pc_boot_time = models.CharField(max_length=250)
    total_size = models.CharField(max_length=250)
    total_memory = models.CharField(max_length=250)
    total_cores = models.CharField(max_length=250)
    processor = models.CharField(max_length=250)
    usage_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.sys_name



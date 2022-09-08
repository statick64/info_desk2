# from dataclasses import fields
from rest_framework import serializers

from .models import SystemName



# class MemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MemoryInformation
#         fields = "__all__"


# class CpuSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MemoryInformation
#         fields = "__all__"


# class SystemInformationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MemoryInformation
#         fields = "__all__"

# class Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = MemoryInformation
#         fields = "__all__"

# class MemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MemoryInformation
#         fields = "__all__"

class SystemNameSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = SystemName
        fields = "__all__"
    
    # def create(self, validated_data):
    #     memory_info = validated_data.pop("memory_info")
    #     # MemSerializer(validated_data=memory_info).save()
    #     MemoryInformation.objects.create(**memory_info)

    #     return validated_data
 





# class SysinfoSerializer(serializers.ModelSerializer):
#     Sys_name = SysnameSerializer()
#     class Meta:
#         model = SystemInformation
#         fields = "__all__"

# class BootSerializer(serializers.ModelSerializer):
#     Sys_name = SysnameSerializer()
#     class Meta:
#         model = BootTime
#         fields = "__all__"

# class DiskSerializer(serializers.ModelSerializer):
#     Sys_name = SysnameSerializer()
#     class Meta:
#         model = DiskInformation
#         fields = "__all__"

# class CpuSerializer(serializers.ModelSerializer):
#     Sys_name = SysnameSerializer()
#     class Meta:
#         model = CpuInformation
#         fields = "__all__"
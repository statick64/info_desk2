from logging import raiseExceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SystemNameSerializer
from .models import SystemName
from api import serializers

class SystemInformations(APIView):

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        sys_name_serializer = SystemNameSerializer
        queryset = SystemName.objects.all()
        serializer = sys_name_serializer(queryset, many=True)
        serializer.data
        return Response(serializer.data)

    def post(self, request, **kwargs):
        serializer = SystemNameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            data = serializer.data
            return Response(data)

        # memory_info =  serializer.validated_data.get("memory_info")
        # print(memory_info)
        # system_info = serializer.validated_data.get("system_info")
        # print(system_info)
        # cpu_info  = serializer.validated_data.get("cpu_info")
        # print(cpu_info)
        # disk_info = serializer.validated_data.get("disk_info")
        # print(disk_info)
        # boot_info = serializer.validated_data.get("boot_info")
        # print(boot_info)


        # memory = MemoryInformation.objects.filter(id=memory_info).last()
        # print(memory)
        # cpu = CpuInformation.objects.filter(id=cpu_info).last()
        # print(cpu)
        # disk = DiskInformation.objects.filter(id=disk_info).last()
        # print(disk)
        # boot = BootTime.objects.filter(id=boot_info).last()
        # print(boot)
        # system_details = SystemInformation.objects.filter(id=system_info).last()
        # print(system_details)

        # data = {
        # "sys_name":  serializer.validated_data.get("sys_name"),
        # "memory_info" : memory,
        # "cpu_info" : cpu,
        # "disk_info" : disk,
        # "boot_info" : boot,
        # "system_info" : system_details
        
        # }
        
        # resp = SystemName.objects.create(**data)
        # return Response(resp)
        
        

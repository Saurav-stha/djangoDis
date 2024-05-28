#used to serialize(convert) different formats of data like python dict, list to json format

from rest_framework.serializers import ModelSerializer
from base.models import Server


class ServerSerializer(ModelSerializer):
    class Meta:
        model = Server
        fields = "__all__"
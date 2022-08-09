from rest_framework import serializers

from .models import Computer

class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = '__all__'


    def to_representation(self, instance:Computer):
        rep = super().to_representation(instance)
        rep['rating'] = instance.average_rating

        request = self.context.get('request')
        return rep
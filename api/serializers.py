from rest_framework import serializers

from core.models.user import User
from core.models.address import Address
from core.models.demmand import Demmand

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'telephone')


class AddressSerializer(serializers.ModelSerializer):

    country = serializers.ReadOnlyField()

    class Meta: 
        model = Address
        fields = ('id','country', 'state', 'city', 'street', 'number')


class DemmandSerializer(serializers.ModelSerializer):
    
    announcer = UserSerializer(read_only=True)
    deliver_address = AddressSerializer()
    

    class Meta:
        model = Demmand
        fields = ('id','description', 'deliver_address', 'announcer','is_finalized')

    def create(self, validated_data):
        address_data = validated_data.pop('deliver_address')
        demmand = Demmand.objects.create(**validated_data)
        address = Address.objects.create(
            state=address_data['state'],
            city=address_data['city'],
            street=address_data['street'],
            number=address_data['number']
        )

        demmand.deliver_address = address

        demmand.save()
        
        return demmand

    def update(self, instance, validated_data):
        address_data = validated_data.pop('deliver_address')
        instance.description = validated_data.get('description', instance.description)
        address = Address.objects.create(
            state=address_data['state'],
            city=address_data['city'],
            street=address_data['street'],
            number=address_data['number']
        )
        instance.is_finalized = validated_data.get('is_finalized', instance.is_finalized)
        instance.deliver_address = address
        instance.save()
        return instance
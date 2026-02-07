from rest_framework import serializers

from vehicle.models import Car, Moto, Mileage
from vehicle.validators import TitleValidator


class MileageSerializer(serializers.ModelSerializer):
    '''Сериализатор пробега'''

    class Meta:
        model = Mileage
        fields ='__all__'


class CarSerializer(serializers.ModelSerializer):
    '''Сериализатор моделей автомобилей'''
    last_mileage = serializers.SerializerMethodField(read_only=True)
    mileage = MileageSerializer(many=True, read_only=True)
    usd_price = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields ='__all__'

    def get_usd_price(self, instance):
        return convert_currencies(instance)


    def get_last_mileage(self, obj):
        last_mileage = obj.mileage.order_by('-id').first()
        return last_mileage.mileage if last_mileage else None


class MotoSerializer(serializers.ModelSerializer):
    '''Сериализатор мото-моделей '''
    last_mileage = serializers.SerializerMethodField()

    class Meta:
        model = Moto
        fields ='__all__'


    @staticmethod
    def get_last_mileage(instance):
        if instance.mileage.all().first():
            return instance.mileage.all().first().mileage
        return 0


class MotoMileageSerializer(serializers.ModelSerializer):
    '''Сериализатор пробега мотоциклов'''
    moto = MotoSerializer()

    class Meta:
        model = Mileage
        fields =('mileage', 'year', 'moto',)


class MotoCreateSerializer(serializers.ModelSerializer):
    mileage = MileageSerializer(many=True)

    class Meta:
        model = Moto
        fields = '__all__'
        validators = [
            TitleValidator(field='title'),
            serializers.UniqueTogetherValidator(fields=['title', 'description'], queryset=Moto.objects.all())
        ]

    def create(self, validated_data):
        mileage = validated_data.pop('mileage')

        moto_item = Moto.objects.create(**validated_data)

        for m in mileage:
            Mileage.objects.create(**m, moto=moto_item)

        return moto_item
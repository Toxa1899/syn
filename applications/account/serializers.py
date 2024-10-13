from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()

class RegisterSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=6, required=True, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2')

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password2')

        if p1 != p2:
            return serializers.ValidationError('Пароли не совпадают')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

from rest_framework import serializers
from AdvisorCall.models import *


class UserSerializer(serializers.ModelSerializer):
    # advisorbooked = serializers.BookCallSerializer()

    class Meta:
        model = User
        # fields = ('id', 'name', 'password', 'email', 'advisorbooked')
        fields = ('id', 'name', 'password', 'email')


        name = serializers.CharField(max_length=200)
        email = serializers.CharField(max_length=200)
        password = serializers.CharField(max_length=100)

    def create_user(self, name, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        name = self.name
        email = self.normalize_email(email)
        if email:
            from AdvisorCall.models import User
            user = User.objects.filter(email=email)
            if user.exists():
                raise ValueError(_('The Email already registered'))

        user = self.model(name=name, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name', instance.name)
        print(instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance


    def create_superuser(self, name, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(name, email, password, **extra_fields)


class AdvisorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advisor
        fields = ('id', 'name', 'image_url')
    
    # def create(self, validated_data):
    #     return Advisor.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     print(instance.name)
    #     instance.name = validated_data.get('name', instance.name)
    #     print(instance.name)
    #     instance.image_url = validated_data.get('image_url', instance.image_url)
    #     instance.save()
    #     return instance
    

class BookCallSerializer(serializers.ModelSerializer):

    class Meta:
        models = BookCall
        fields = ('id', 'user', 'advisor', 'created')

    def create(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        print(instance.user)
        instance.advisor = validated_data.get('advisor', instance.advisor)
        print(instance.advisor)
        instance.save()
        return instance
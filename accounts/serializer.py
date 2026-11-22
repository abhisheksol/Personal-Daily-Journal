from rest_framework import serializers
from accounts.models import UserModel



class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'dob', 'profile_picture']
        extra_kwargs = {'password': {'write_only': True}}


    def validate(self, data):

        password = data.get('password')
        if password and len(password) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")

        if username := data.get('username'):
            if UserModel.objects.filter(username=username).exists():
                raise serializers.ValidationError("Username already exists.")

        if email := data.get('email'):
            if UserModel.objects.filter(email=email).exists():
                raise serializers.ValidationError("Email already exists.")

        # bank field not allowed to be empty
        if not data.get('username'):
            raise serializers.ValidationError("Username is required.")

        if not data.get('email'):
            raise serializers.ValidationError("Email is required.")

        if not data.get('password'):
            raise serializers.ValidationError("Password is required.")
        
        return data
    

       

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            dob=validated_data.get('dob', None),
            profile_picture=validated_data.get('profile_picture', None),    
        )
        return user
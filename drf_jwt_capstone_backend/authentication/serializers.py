from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[
                                   UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        # If added new columns through the User model, add them in the fields
        # list as seen below
        fields = ('rest_score','ent_score','street','city,','state', 'password', 'email',
                  'first_name', 'last_name','saved_ent','saved_rest', 'total_usage', 'total_refresh' )

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            rest_score=validated_data['rest_score'],
            ent_score=validated_data['ent_score'],
            street=validated_data['street'],
            city=validated_data['city'],
            state=['state'],
            saved_ent=validated_data['saved_ent'],
            total_usage=validated_data['total_usage'],
            total_refresh=validated_data['total_refresh']

            # If added new columns through the User model, add them in this
            # create method call in the format as seen above
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

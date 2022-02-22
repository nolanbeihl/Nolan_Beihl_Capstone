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
        fields = ('street','city','state', 'password', 'email',
                  'firstName', 'lastName' )
                #   'savedEnt','savedRest','restScore','entScore',, 'total_usage', 'total_refresh','userName'

    def create(self, validated_data):

        user = User.objects.create(
            # userName=validated_data['userName'],
            email=validated_data['email'],
            firstName=validated_data['firstName'],
            lastName=validated_data['lastName'],
            # restScore=validated_data['rest_score'],
            # entScore=validated_data['ent_score'],
            street=validated_data['street'],
            city=validated_data['city'],
            state=['state'],
            # savedEnt=validated_data['saved_ent'],
            # savedRest=validated_data['saved_rest'],
            # total_usage=validated_data['total_usage'],
            # total_refresh=validated_data['total_refresh'],

            # If added new columns through the User model, add them in this
            # create method call in the format as seen above
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

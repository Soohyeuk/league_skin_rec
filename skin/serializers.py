from rest_framework import serializers
from .models import Skins

class SkinSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = Skins
        fields =  '__all__'
    
    def get_average_rating(self, obj):
        return obj.average_rating()
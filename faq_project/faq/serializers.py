from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
    def get_translated_question(self, obj):
        request = self.context.get('request')
        lang = request.query_params.get('lang', 'en')
        return obj.get_translation(lang)
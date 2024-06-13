from rest_framework import serializers
from .models import Odam, Ikon, Sponsr, Sumpermision, Maqola


class OdamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Odam
        fields = ['id', 'ism_famiya', 'mamlakati', 'rasm', 'uversitet']


class IkonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ikon
        fields = ['id', 'text', 'ikon_rasm']


class SumpermisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sumpermision
        fields = ['id', 'text', 'name', 'narx']


class SponsrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsr
        fields = ['id', 'name', 'sponsr_rasm']


class MaqolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maqola
        fields = [
            'id', 'first_name', 'last_name', 'country', 'email',
            'tel_raqam', 'affiliation', 'title', 'key_words',
            'section', 'files'
        ]

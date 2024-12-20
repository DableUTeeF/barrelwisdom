from rest_framework import serializers
from collections import OrderedDict
from games.A15.categories_a15.models import Category
from games.A15.items_a15.models import Item, Ingredient

class A15ItemSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = ['slug', 'name', 'level', 'evalue', 'fire', 'water', 'wind', 'earth']

    def get_name(self,obj):
        if 'language' not in self.context:
            return obj.item_en.name
        elif self.context['language'] == 'ja':
            return obj.item_ja.name
        else:
            return obj.item_en.name

class A15IngredientSerializer(serializers.ModelSerializer):
    synthitem = A15ItemSerializer()
    class Meta:
        model = Ingredient
        fields = ['synthitem']

class A15CategorySerializerName(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['name', 'icon_name']
    def get_name(self,obj):
        if 'language' not in self.context:
            return obj.cat_en.name
        elif self.context['language'] == 'ja':
            return obj.cat_ja.name
        else:
            return obj.cat_en.name

class A15CategorySerializerLink(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['slug', 'name']
    def get_name(self,obj):
        if 'language' not in self.context:
            return obj.cat_en.name
        elif self.context['language'] == 'ja':
            return obj.cat_ja.name
        else:
            return obj.cat_en.name

class A15CategorySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['slug', 'name', 'icon_name']

    def get_name(self,obj):
        if 'language' not in self.context:
            return obj.cat_en.name
        elif self.context['language'] == 'ja':
            return obj.cat_ja.name
        else:
            return obj.cat_en.name

class A15CategoryDataSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    item_set = A15ItemSerializer(many=True)
    ingredientcat = A15IngredientSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['slug', 'name', 'icon_name', 'item_set', 'ingredientcat']

    def get_name(self,obj):
        if 'language' not in self.context:
            return obj.cat_en.name
        elif self.context['language'] == 'ja':
            return obj.cat_ja.name
        else:
            return obj.cat_en.name
    def to_representation(self, instance):
        result = super(A15CategoryDataSerializer, self).to_representation(instance)
        return OrderedDict((k, v) for k, v in result.items() 
                           if v not in [None, [], '', False, {}])
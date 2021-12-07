from games.BRSL.facilities_brsl.models import Facility, FacilityEffect, FacilityEffectLine, FacilityIngredient, FacilitySet
from games.BRSL.items_brsl.serializers import BRSLEffectSerializer, BRSLCategorySerializer, BRSLItemNameSerializer
from rest_framework import serializers
from collections import OrderedDict

class BRSLFacilityEffectSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    desc = serializers.SerializerMethodField()
    class Meta:
        model = FacilityEffect
        fields = ['name', 'desc']#, 'act0', 'val0','act1', 'val1','act2', 'val2']
    def get_name(self,obj):
        if 'language' not in self.context:
            return obj.eff_en.name
        if self.context['language'] == 'ja':
            return obj.eff_ja.name
        if self.context['language'] == 'sc':
            return obj.eff_sc.name
        if self.context['language'] == 'tc':
            return obj.eff_tc.name
        else:
            return obj.eff_en.name
    def get_desc(self,obj):
        if 'language' not in self.context:
            return obj.eff_en.desc
        if self.context['language'] == 'ja':
            return obj.eff_ja.desc
        if self.context['language'] == 'sc':
            return obj.eff_sc.desc
        if self.context['language'] == 'tc':
            return obj.eff_tc.desc
        else:
            return obj.eff_en.desc
    def to_representation(self, instance):
        result = super(BRSLFacilityEffectSerializer, self).to_representation(instance)
        return OrderedDict((k, v) for k, v in result.items() 
                           if v not in [None, [], '', False, {}])

class BRSLFacilityEffectLineSerializer(serializers.ModelSerializer):
    effect = BRSLFacilityEffectSerializer()
    class Meta:
        model = FacilityEffectLine
        fields = ['effect', 'line', 'num']
        
class BRSLFacilityIngredienteSerializer(serializers.ModelSerializer):
    effect = BRSLEffectSerializer()
    item = BRSLItemNameSerializer()
    category = BRSLCategorySerializer()
    class Meta:
        model = FacilityIngredient
        fields = ['level', 'num', 'item', 'category', 'effect']
    def to_representation(self, instance):
        result = super(BRSLFacilityIngredienteSerializer, self).to_representation(instance)
        return OrderedDict((k, v) for k, v in result.items() 
                           if v not in [None, [], '', False, {}])
        

class BRSLFacilityNameSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = Facility
        fields = ['slug', 'name']
    def get_name(self,obj):
        if 'language' not in self.context:
            return obj.facility_en.name
        if self.context['language'] == 'ja':
            return obj.facility_ja.name
        if self.context['language'] == 'sc':
            return obj.facility_sc.name
        if self.context['language'] == 'tc':
            return obj.facility_tc.name
        else:
            return obj.facility_en.name
        
class BRSLFacilitySimpleSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = Facility
        fields = ['slug', 'name', 'size', 'isDLC']
    def get_name(self,obj):
        if 'language' not in self.context:
            return obj.facility_en.name
        if self.context['language'] == 'ja':
            return obj.facility_ja.name
        if self.context['language'] == 'sc':
            return obj.facility_sc.name
        if self.context['language'] == 'tc':
            return obj.facility_tc.name
        else:
            return obj.facility_en.name
    def to_representation(self, instance):
        result = super(BRSLFacilitySimpleSerializer, self).to_representation(instance)
        return OrderedDict((k, v) for k, v in result.items() 
                           if v not in [None, [], '', False, {}])

class BRSLFacilitySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    desc = serializers.SerializerMethodField()
    facilityeffectline_set = BRSLFacilityEffectLineSerializer(many=True)
    facilityingredient_set = BRSLFacilityIngredienteSerializer(many=True)
    class Meta:
        model = Facility
        fields = ['slug', 'name', 'desc', 'char', 'size', 'isDLC', 'facilityeffectline_set', 'facilityingredient_set']
    def get_name(self,obj):
        if 'language' not in self.context:
            return obj.facility_en.name
        if self.context['language'] == 'ja':
            return obj.facility_ja.name
        if self.context['language'] == 'sc':
            return obj.facility_sc.name
        if self.context['language'] == 'tc':
            return obj.facility_tc.name
        else:
            return obj.facility_en.name
    def get_desc(self,obj):
        if 'language' not in self.context:
            return obj.facility_en.desc
        if self.context['language'] == 'ja':
            return obj.facility_ja.desc
        if self.context['language'] == 'sc':
            return obj.facility_sc.desc
        if self.context['language'] == 'tc':
            return obj.facility_tc.desc
        else:
            return obj.facility_en.desc
    def to_representation(self, instance):
        result = super(BRSLFacilitySerializer, self).to_representation(instance)
        return OrderedDict((k, v) for k, v in result.items() 
                           if v not in [None, [], '', False, {}])

class BRSLFacilitySetSerializer(serializers.ModelSerializer):
    effect = BRSLFacilityEffectSerializer()
    facilities = BRSLFacilityNameSerializer(many=True)
    class Meta:
        model = FacilitySet
        fields = ['effect', 'facilities']
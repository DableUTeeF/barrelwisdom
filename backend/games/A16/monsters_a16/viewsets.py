from rest_framework import viewsets, filters
from games.A16.monsters_a16.models import Monster
from games.A16.monsters_a16.serializers import A16MonsterSerializer, A16MonsterLevelSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

class A16MonsterViewSet(viewsets.ModelViewSet):
    queryset = Monster.objects.all()
    serializer_class = A16MonsterSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    lookup_field = 'slug'

    @action(detail=False)
    def en(self, request):
        queryset = (
            Monster.objects
            .select_related(
                'mon_en'
            )
        )
        serializer = A16MonsterLevelSerializer(queryset, many=True, context={'language': 'en'})
        return Response(serializer.data)

    @action(detail=False)
    def ja(self, request):
        queryset = (
            Monster.objects
            .select_related(
                'mon_ja'
            )
        )
        serializer = A16MonsterLevelSerializer(queryset, many=True, context={'language': 'ja'})
        return Response(serializer.data)

    # allows easy access via catect/slug/en
    @action(detail=True, methods=['get'], url_path="en")
    def en_full(self, request, slug):
        try:
            queryset = (
                Monster.objects
                .select_related(
                    'mon_en'
                )
                .prefetch_related(
                    'item_set__item_en',
                    'locations__reg_en'
                )
                .get(slug=slug)
            )
        except ObjectDoesNotExist:
            raise Http404
        serializer = A16MonsterSerializer(queryset, context={'language': 'en'})
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path="ja")
    def ja_full(self, request, slug):
        try:
            queryset = (
                Monster.objects
                .select_related(
                    'mon_ja'
                )
                .prefetch_related(
                    'item_set__item_ja',
                    'locations__reg_ja'
                )
                .get(slug=slug)
            )
        except ObjectDoesNotExist:
            raise Http404
        serializer = A16MonsterSerializer(queryset, context={'language': 'ja'})
        return Response(serializer.data)
from rest_framework import viewsets, filters
from games.A23.traits_a23.models import Trait
from games.A23.traits_a23.serializers import A23TraitSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

class A23TraitViewSet(viewsets.ModelViewSet):
    queryset = Trait.objects.all()
    serializer_class = A23TraitSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    lookup_field = 'slug'

    @action(detail=False)
    def en(self, request):
        queryset = (
            Trait.objects
            .select_related(
                'trait_en'
            )
            .prefetch_related(
                'item_set',
                'item_set__item_en',
                "combo1",
                "combo2",
            )
        )
        serializer = A23TraitSerializer(queryset, many=True, context={'language': 'en'})
        return Response(serializer.data)

    @action(detail=False)
    def ko(self, request):
        queryset = (
            Trait.objects
            .select_related(
                'trait_ko'
            )
            .prefetch_related(
                'item_set',
                'item_set__item_ko',
                "combo1",
                "combo2",
            )
        )
        serializer = A23TraitSerializer(queryset, many=True, context={'language': 'ko'})
        return Response(serializer.data)

    @action(detail=False)
    def ja(self, request):
        queryset = (
            Trait.objects
            .select_related(
                'trait_ja'
            )
            .prefetch_related(
                'item_set',
                'item_set__item_ja',
            )
        )
        serializer = A23TraitSerializer(queryset, many=True, context={'language': 'ja'})
        return Response(serializer.data)

    @action(detail=False)
    def sc(self, request):
        queryset = (
            Trait.objects
            .select_related(
                'trait_sc'
            )
            .prefetch_related(
                'item_set',
                'item_set__item_sc',
                "combo1",
                "combo2",
            )
        )
        serializer = A23TraitSerializer(queryset, many=True, context={'language': 'sc'})
        return Response(serializer.data)

    @action(detail=False)
    def tc(self, request):
        queryset = (
            Trait.objects
            .select_related(
                'trait_tc'
            )
            .prefetch_related(
                'item_set',
                'item_set__item_tc',
                "combo1",
                "combo2",
            )
        )
        serializer = A23TraitSerializer(queryset, many=True, context={'language': 'tc'})
        return Response(serializer.data)


    @action(detail=True, methods=['get'], url_path="en")
    def en_full(self, request, slug):
        try:
            queryset = (
                Trait.objects
                .select_related(
                    'trait_en'
                )
                .prefetch_related(
                    'item_set',
                    'item_set__item_en',
                    "combo1",
                    "combo2",
                )
                .get(slug=slug)
            )
        except ObjectDoesNotExist:
            raise Http404
        serializer = A23TraitSerializer(queryset, context={'language': 'en'})
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path="ko")
    def ko_full(self, request, slug):
        try:
            queryset = (
                Trait.objects
                .select_related(
                    'trait_ko'
                )
                .prefetch_related(
                    'item_set',
                    'item_set__item_ko',
                    "combo1",
                    "combo2",
                )
                .get(slug=slug)
            )
        except ObjectDoesNotExist:
            raise Http404
        serializer = A23TraitSerializer(queryset, context={'language': 'ko'})
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path="ja")
    def ja_full(self, request, slug):
        try:
            queryset = (
                Trait.objects
                .select_related(
                    'trait_ja'
                )
                .prefetch_related(
                    'item_set',
                    'item_set__item_ja',
                    "combo1",
                    "combo2",
                )
                .get(slug=slug)
            )
        except ObjectDoesNotExist:
            raise Http404
        serializer = A23TraitSerializer(queryset, context={'language': 'ja'})
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path="sc")
    def sc_full(self, request, slug):
        try:
            queryset = (
                Trait.objects
                .select_related(
                    'trait_sc'
                )
                .prefetch_related(
                    'item_set',
                    'item_set__item_sc',
                    "combo1",
                    "combo2",
                )
                .get(slug=slug)
            )
        except ObjectDoesNotExist:
            raise Http404
        serializer = A23TraitSerializer(queryset, context={'language': 'sc'})
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path="tc")
    def tc_full(self, request, slug):
        try:
            queryset = (
                Trait.objects
                .select_related(
                    'trait_tc'
                )
                .prefetch_related(
                    'item_set',
                    'item_set__item_tc',
                    "combo1",
                    "combo2",
                )
                .get(slug=slug)
            )
        except ObjectDoesNotExist:
            raise Http404
        serializer = A23TraitSerializer(queryset, context={'language': 'tc'})
        return Response(serializer.data)
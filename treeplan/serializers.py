from rest_framework import serializers
from treeplan.models import Plan, Tree


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('id', 'name', 'milestone')


class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = ('id', 'plan', 'x', 'y', 'name', 'sciName', 'diameter', 'height', 'heightToCrown', 'crownSpread', 'age',
                  'ontogenetic', 'health', 'note')


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.reverse import reverse

from treeplan.models import Plan, Tree
from treeplan.serializers import PlanSerializer, TreeSerializer


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class TreeViewSet(viewsets.ModelViewSet):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer

    def get_queryset(self):
        queryset = Tree.objects.all()
        plan_id = self.request.query_params.get('plan', None)
        if plan_id is not None:
            queryset = queryset.filter(plan=plan_id)
        return queryset


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'plans': reverse('plan-list', request=request, format=format),
        'trees': reverse('tree-list', request=request, format=format)
    })

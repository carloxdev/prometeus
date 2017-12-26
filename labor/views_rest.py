# -*- coding: utf-8 -*-

# Third-party Libraries
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response

# Own's Libraries
from .models import IncidentEvidence
from .forms import IncidentEvidenceAddForm


class IncidentEvidenceAPIView(views.APIView):

    def post(self, request):

        form = IncidentEvidenceAddForm(request.POST, request.FILES)
        if form.is_valid():
            record = form.save()
            data = {'name': record.image.name, 'url': record.image.url}
        else:
            data = form.errors
            return Response(
                data,
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            data,
            status=status.HTTP_200_OK
        )

# -*- coding: utf-8 -*-

# Third-party Libraries
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response

# Own's Libraries
from .models import VoucherType


class VoucherTypeAPIView(views.APIView):

    def get(self, request, pk):
        try:
            type = VoucherType.objects.get(id=pk)
            data = {
                'name': type.name,
                'valid_range': type.valid_range
            }

        except VoucherType.DoesNotExist:
            return Response(
                {'detail': "Tipo no existe"},
                status=status.HTTP_204_NO_CONTENT
            )
        except Exception as error:
            return Response(
                {'detail': str(error)},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            data,
            status=status.HTTP_200_OK
        )

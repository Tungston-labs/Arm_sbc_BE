from collections import defaultdict

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Processor    # <-- FIXED (removed Vendor)
from .serializers import ProcessorCatalogSerializer, VendorCatalogSerializer


class CatalogView(APIView):
    """
    Returns catalog grouped as:
    [
      {
        "vendor": "Rockchip",
        "processors": [ { processor+boards... }, ... ]
      },
      ...
    ]
    """

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        processors = Processor.objects.prefetch_related("boards").all()

        # Group by human-readable vendor label
        by_vendor = defaultdict(list)
        for p in processors:
            by_vendor[p.get_vendor_display()].append(p)

        payload = []
        for vendor_label, items in by_vendor.items():
            serializer = ProcessorCatalogSerializer(items, many=True)
            payload.append(
                {
                    "vendor": vendor_label,
                    "processors": serializer.data,
                }
            )

        return Response(payload)


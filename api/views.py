import csv
from django.http import JsonResponse
from rest_framework.response import Response
from django.shortcuts import HttpResponseRedirect, render
from rest_framework.views import APIView
from .models import Bank, Branch
from .serializers import BranchSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def bank_detail_view(request, ifsc, *args, **kwargs):
    qs = Branch.objects.filter(ifsc__iexact=ifsc).first()
    # if not qs.exists():
        # return Response({}, status=404)
    serializer = BranchSerializer(qs)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def banks_list_view(request, city, bank, *args, **kwargs):
    qs = Branch.objects.filter(city__iexact=city, bank__name__icontains=bank)
    # if not qs.exists():
        # return Response({}, status=404)
    serializer = BranchSerializer(qs, many=True)
    return Response(serializer.data, status=200)


class UploadView(APIView):
    def get(self, request):
        return render(request, 'upload.html')

    def post(self, request):
        csv_file = request.FILES.get('csv_file')
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        rows = csv.DictReader(decoded_file)

        for row in rows:
            bank_name = row.get('bank_name')
            ifsc = row.get('ifsc')
            branch = row.get('branch')
            address = row.get('address')
            city = row.get('city')
            district = row.get('district')
            state = row.get('state')

            bank_object, created = Bank.objects.get_or_create(
                name=bank_name
            )

            branch_defaults = {
                'name': branch,
                'bank': bank_object,
                'address': address,
                'city': city,
                'district': district,
                'state': state    
            }
        
            branch_object, created = Branch.objects.update_or_create(
                ifsc=ifsc, defaults=branch_defaults
            )
            
        return render(request, 'upload.html')
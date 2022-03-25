from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CloudTokenObtainPairSerializer


# Create your views here.
class CloudTokenObtainPairView(TokenObtainPairView):
    serializer_class = CloudTokenObtainPairSerializer

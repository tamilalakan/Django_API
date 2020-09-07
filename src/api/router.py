from account.views import AccountViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('',AccountViewset,basename='ap')


from django.contrib import admin
from django.urls import path,include
from api.Permission import view as permissionView
from api.Role import view as roleView
from api.User import view as userView
from api.TestAPI import view as TestView
from api.Address import view as AddressView
from api.ChangeMyPassword.view import ChangeMyPasswordView
from api.ForgetPassword.view import PasswordResetRequestView
from api.IsSuperUser.view import CheckUserType
from api.CreateUser import views as createUserViews
from api.Student.view import StudentViewSet
from api.classmg.view import ClassRoomViewSet
from api.teacher.view import TeacherViewSet
from api.Subject.view import SubjectViewSet
from api.Payment.view import PaymentViewSet



#Custom API imports
from api.CustomAPI.getTeacherbyid import GetTeacherByIdAPIView
from api.CustomAPI.getStudentById import GetStudentByIdAPIView

from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router=routers.DefaultRouter()
router.register(r'user',userView.UserViewset, basename='user'),
router.register(r'role',roleView.RoleViewset, basename='role'),
router.register(r'permission', permissionView.PermissionViewset, basename='permission'),
router.register(r'test', TestView.TestViewset, basename='test'),
router.register(r'address',AddressView.AddressViewset,basename='address'),
router.register(r'student', StudentViewSet, basename='student'),
router.register(r'class', ClassRoomViewSet, basename='classroom'),
router.register(r'teacher', TeacherViewSet, basename='teacher'),
router.register(r'subject', SubjectViewSet, basename='subject'),
router.register(r'payment', PaymentViewSet, basename='payment'),

# Create a schema view for drf-yasg
schema_view = get_schema_view(
    openapi.Info(
        title="Placeholder API",
        default_version='v1',
        description="Your API Description",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('',include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('changeMyPassword/', ChangeMyPasswordView.as_view(), name='changeMyPassword'),
    path('passwordReset/', PasswordResetRequestView.as_view(), name='passwordResetRequest'),
    # path('pass-reset/<str:temp_token>/', PasswordResetConfirmView.as_view(), name='pass-reset'),  # put it in security(auth) app's urls
    path('isSuperUser/', CheckUserType.as_view(), name='isSuperUser'),
    path('createUser/', createUserViews.CreateUserAPI.as_view(), name='create-user'),
    path('getTeacherById/<uuid:teacher_id>/', GetTeacherByIdAPIView.as_view(),name='getTeacherById'),
    path('getStudentById/<int:student_id>/', GetStudentByIdAPIView.as_view(),name='getStudentById'),
]
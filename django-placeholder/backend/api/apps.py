from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        import api.UserProfile
        import api.TestAPI.model
        import api.Address.model
        import api.Student.model
        import api.classmg.model
        import api.teacher.model
        import api.Subject.model
        import api.Payment.model
        
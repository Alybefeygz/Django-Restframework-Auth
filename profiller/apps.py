from django.apps import AppConfig


class ProfillerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "profiller"  # Eğer uygulamanın tam yolu 'core.profiller' ise bunu kullanmalısın.

    def ready(self):
        import profiller.signals  # Burada import işlemini düzgün yap




__all__ = ("DATABASES", "INSTALLED_APPS", "SECRET_KEY")

SECRET_KEY = "secret"

INSTALLED_APPS = (
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "django.contrib.auth",
    "django_filters",
    "tests",
)

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

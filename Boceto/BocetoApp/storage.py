from django.contrib.staticfiles.storage import ManifestStaticFilesStorage


class ForgivingManifestStaticFilesStorage(ManifestStaticFilesStorage):
    """Ignora referencias a archivos que no existen.

    El CSS minificado de terceros (jazzmin/bootstrap) referencia source maps
    que el paquete no incluye; la storage estricta aborta collectstatic al no
    poder hashearlos. Aquí la referencia rota se deja tal cual y el resto del
    manifest se genera con normalidad.
    """

    # En runtime, un archivo ausente del manifest devuelve su nombre sin hash
    # en vez de tumbar la página con ValueError.
    manifest_strict = False

    def hashed_name(self, name, content=None, filename=None):
        try:
            return super().hashed_name(name, content, filename)
        except ValueError:
            return name

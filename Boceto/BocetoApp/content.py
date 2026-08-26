"""Contenido editorial de la página de inicio.

Centralizado aquí para que las plantillas solo iteren datos: cambiar un texto,
una tarjeta o una certificación no requiere tocar HTML.
"""

HERO_BADGES = ['Fair Trade', '100% Orgánico', 'Global Gap', 'BPM']

ABOUT_CARDS = [
    {
        'icon': '🍌',
        'icon_class': '',
        'titulo': 'Producción de Calidad',
        'texto': (
            'El cultivo del banano es la principal fuente de ingresos de nuestros socios. '
            'Nuestra fruta es comercializada en varios países europeos como Alemania, Italia y Francia.'
        ),
    },
    {
        'icon': '🤝',
        'icon_class': 'card__icon--gold',
        'titulo': 'Comercio Justo',
        'texto': (
            'Contamos con Certificación Fair Trade, Orgánica, Global Gap, y Buenas Prácticas '
            'de Manufactura para los mercados de USA, Europa y Japón.'
        ),
    },
    {
        'icon': '🌱',
        'icon_class': 'card__icon--light',
        'titulo': 'Nuestra Historia',
        'texto': (
            'La Cooperativa Agrícola Oro Verde fue fundada el 11 de septiembre de 2017 por 12 socios. '
            'Hoy contamos con 25 socios dedicados a la producción de banano.'
        ),
    },
]

CERTIFICACIONES = [
    {
        'nombre': 'Fair Trade',
        'logo': 'boceto/images/fairtrade300.webp',
        'descripcion': 'Comercio justo que garantiza precios equitativos y condiciones laborales dignas.',
    },
    {
        'nombre': 'Global Gap',
        'logo': 'boceto/images/global300.webp',
        'descripcion': 'Estándares para producción segura y sostenible de alimentos a nivel mundial.',
    },
    {
        'nombre': 'Control Union',
        'logo': 'boceto/images/control300.webp',
        'descripcion': 'Certificación que evalúa prácticas sostenibles en producción y comercio.',
    },
    {
        'nombre': 'BPM',
        'logo': 'boceto/images/BPM300.webp',
        'descripcion': 'Buenas Prácticas de Manufactura para seguridad e integridad del producto.',
    },
    {
        'nombre': 'Orgánica',
        'logo': 'boceto/images/organica300.webp',
        'descripcion': 'Producción sin químicos sintéticos, respetuosa con el ambiente y la salud.',
    },
]

# Testimoniales de muestra que se usan mientras no existan registros en la BD.
# Mismos nombres de campos que el modelo Testimonial para poder iterarlos igual.
TESTIMONIALES_EJEMPLO = [
    {
        'nombre': 'Hans Müller',
        'cargo': 'Purchasing Director',
        'empresa': 'BioFrisch GmbH',
        'pais': '🇩🇪 Alemania',
        'rating': 5,
        'testimonio': (
            'Excellent quality bananas with consistent supply. Oro Verde has been our '
            'trusted partner for organic produce for over 3 years.'
        ),
    },
    {
        'nombre': 'Marco Rossi',
        'cargo': 'CEO',
        'empresa': 'Frutti Biologici S.r.l.',
        'pais': '🇮🇹 Italia',
        'rating': 5,
        'testimonio': (
            'La qualità delle banane è eccezionale. La certificazione Fair Trade è molto '
            'importante per i nostri clienti in Italia.'
        ),
    },
    {
        'nombre': 'Sophie Dubois',
        'cargo': 'Import Manager',
        'empresa': 'FruitsBio France',
        'pais': '🇫🇷 Francia',
        'rating': 5,
        'testimonio': (
            "Les bananes biologiques d'Oro Verde sont parmi les meilleures que nous avons "
            'importées. Service client impeccable.'
        ),
    },
]

"""Contenido editorial de la página de inicio.

Centralizado aquí para que las plantillas solo iteren datos: cambiar un texto,
una tarjeta o una certificación no requiere tocar HTML.
"""

HERO_BADGES = ['Fair Trade', '100% Orgánico', 'Global Gap', 'BPM']

# Cifras clave que prueban trayectoria arriba del fold
KPIS = [
    {'valor': '25', 'etiqueta': 'Socios productores'},
    {'valor': '2017', 'etiqueta': 'Año de fundación'},
    {'valor': '3', 'etiqueta': 'Mercados europeos'},
    {'valor': '5', 'etiqueta': 'Certificaciones internacionales'},
]

# Los iconos son paths SVG (Material Icons, viewBox 0 0 24 24): render
# consistente entre sistemas operativos, a diferencia de los emojis.
ICON_LEAF = (
    'M6.05 8.05c-2.73 2.73-2.73 7.15-.02 9.88 1.47-3.4 4.09-6.24 7.36-7.93-2.77 '
    '2.34-4.71 5.61-5.39 9.32 2.6 1.23 5.8.78 7.95-1.37C19.43 14.47 20 4 20 4S9.53 '
    '4.57 6.05 8.05z'
)
ICON_BALANCE = (
    'M13 7.83c.85-.3 1.53-.98 1.83-1.83H18l-3 7c0 1.66 1.57 3 3.5 3s3.5-1.34 '
    '3.5-3l-3-7h2V4h-6.17c-.41-1.17-1.52-2-2.83-2s-2.42.83-2.83 2H3v2h2l-3 7c0 '
    '1.66 1.57 3 3.5 3S9 16.66 9 15L6 8h3.17c.3.85.98 1.53 1.83 1.83V19H2v2h20v-2h-9V7.83z'
    'M20.37 13h-3.74l1.87-4.36L20.37 13zm-13 0H3.63L5.5 8.64 7.37 13z'
)
ICON_HISTORY = (
    'M13 3c-4.97 0-9 4.03-9 9H1l3.89 3.89.07.14L9 12H6c0-3.87 3.13-7 7-7s7 3.13 7 '
    '7-3.13 7-7 7c-1.93 0-3.68-.79-4.94-2.06l-1.42 1.42C8.27 19.99 10.51 21 13 21c4.97 '
    '0 9-4.03 9-9s-4.03-9-9-9zm-1 5v5l4.28 2.54.72-1.21-3.5-2.08V8H12z'
)

ABOUT_CARDS = [
    {
        'icon_path': ICON_LEAF,
        'icon_class': '',
        'titulo': 'Producción de Calidad',
        'texto': (
            'El cultivo del banano es la principal fuente de ingresos de nuestros socios. '
            'Nuestra fruta es comercializada en varios países europeos como Alemania, Italia y Francia.'
        ),
    },
    {
        'icon_path': ICON_BALANCE,
        'icon_class': 'card__icon--gold',
        'titulo': 'Comercio Justo',
        'texto': (
            'Contamos con Certificación Fair Trade, Orgánica, Global Gap y Buenas Prácticas '
            'de Manufactura. Hoy exportamos a Alemania, Italia y Francia, con habilitación '
            'para Estados Unidos y Japón.'
        ),
    },
    {
        'icon_path': ICON_HISTORY,
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

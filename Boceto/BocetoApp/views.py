from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.http import HttpResponse, Http404, JsonResponse
from django.views.decorators.http import require_POST, require_GET
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.conf import settings
from django.contrib import messages
import logging

from .models import Post, Cotizacion, Testimonial
from .forms import ContactForm
from .content import HERO_BADGES, ABOUT_CARDS, CERTIFICACIONES, TESTIMONIALES_EJEMPLO

# Configurar logger para errores de email
logger = logging.getLogger(__name__)


# ============================================
# 🏠 VISTAS PRINCIPALES
# ============================================

def _home_context():
    """Contexto compartido de la página de inicio (contenido editorial + testimoniales)."""
    testimoniales = list(Testimonial.objects.filter(activo=True)[:3])
    return {
        'hero_badges': HERO_BADGES,
        'about_cards': ABOUT_CARDS,
        'certificaciones': CERTIFICACIONES,
        'testimoniales': testimoniales or TESTIMONIALES_EJEMPLO,
        'contact_form': ContactForm(),
    }

def home(request):
    """Vista de la página principal."""
    return render(request, "boceto/home.html", _home_context())

def nosotros(request):
    """Vista de la página Nosotros con estilo premium."""
    return render(request, "boceto/nosotros.html")

def colaboradores(request):
    """Vista de la página de Colaboradores."""
    return render(request, "boceto/colaboradores.html")

def labor(request):
    """Vista de la página de Labor Social."""
    return render(request, "boceto/labor.html")

def banapan(request):
    """Vista de la página de Bana Pan."""
    return render(request, "boceto/banapan.html")

def cooporoverdesa(request):
    """Vista de la página de Cooporoverdesa."""
    return render(request, "boceto/cooporoverdesa.html")


# ============================================
# 📧 VISTA DE CONTACTO CON VALIDACIÓN
# ============================================

@require_POST
def enviar_correo(request):
    """
    Procesa el formulario de contacto con Django Forms y responde en la misma
    página (patrón POST/Redirect/GET con django.contrib.messages).
    """
    form = ContactForm(request.POST)

    if not form.is_valid():
        messages.error(request, form.errors['email'][0])
        return redirect(f"{reverse('index')}#contact")

    email = form.cleaned_data['email']

    subject = 'Gracias por ponerte en contacto con nosotros - Cooperativa Oro Verde'
    message = f"""
Hola,

Gracias por ponerte en contacto con nosotros. Hemos recibido tu mensaje
y pronto te responderemos.

Tu correo: {email}

Atentamente,
El equipo de Cooperativa Agrícola Oro Verde
🍌 Produciendo banano orgánico con comercio justo
    """.strip()

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )
        messages.success(request, '✅ Correo enviado correctamente. ¡Pronto te contactaremos!')
        logger.info(f"Correo enviado exitosamente a: {email}")
    except Exception as e:
        messages.error(request, 'Hubo un problema al enviar el correo. Por favor, intenta más tarde.')
        logger.error(f"Error al enviar correo a {email}: {str(e)}")

    return redirect(f"{reverse('index')}#contact")


# ============================================
# 📋 VISTA DE COTIZACIÓN
# ============================================

def cotizacion(request):
    """Muestra el formulario de cotización."""
    return render(request, "boceto/cotizacion.html", {
        'paises': Cotizacion.PAISES_CHOICES
    })

@require_POST
def enviar_cotizacion(request):
    """
    Procesa el formulario de cotización y guarda en la base de datos.
    También envía notificación por email.
    """
    cotizacion_enviada = False
    error_mensaje = None
    
    # Obtener datos del formulario
    nombre = request.POST.get('nombre', '').strip()
    empresa = request.POST.get('empresa', '').strip()
    email = request.POST.get('email', '').strip()
    telefono = request.POST.get('telefono', '').strip()
    pais = request.POST.get('pais', '').strip()
    cantidad = request.POST.get('cantidad', '').strip()
    mensaje = request.POST.get('mensaje', '').strip()
    
    # Validaciones
    if not nombre or not email or not pais or not cantidad:
        error_mensaje = "Por favor, completa todos los campos obligatorios."
        return render(request, 'boceto/cotizacion.html', {
            'cotizacion_enviada': False,
            'error_mensaje': error_mensaje,
            'paises': Cotizacion.PAISES_CHOICES
        })
    
    try:
        validate_email(email)
    except ValidationError:
        error_mensaje = "El correo electrónico ingresado no es válido."
        return render(request, 'boceto/cotizacion.html', {
            'cotizacion_enviada': False,
            'error_mensaje': error_mensaje,
            'paises': Cotizacion.PAISES_CHOICES
        })
    
    try:
        # Guardar en base de datos
        nueva_cotizacion = Cotizacion.objects.create(
            nombre=nombre,
            empresa=empresa,
            email=email,
            telefono=telefono,
            pais=pais,
            cantidad=cantidad,
            mensaje=mensaje
        )
        
        # Enviar email de confirmación al cliente
        subject_cliente = 'Hemos recibido tu solicitud de cotización - Cooperativa Oro Verde'
        message_cliente = f"""
Hola {nombre},

Gracias por tu interés en nuestro banano orgánico premium.

Hemos recibido tu solicitud de cotización con los siguientes datos:
- Empresa: {empresa or 'No especificada'}
- País: {dict(Cotizacion.PAISES_CHOICES).get(pais, pais)}
- Cantidad aproximada: {cantidad}

Nuestro equipo comercial se pondrá en contacto contigo en las próximas 24-48 horas.

Atentamente,
Cooperativa Agrícola Oro Verde
🍌 Banano Orgánico Premium de Ecuador

---
Este correo fue enviado automáticamente. Por favor no respondas directamente.
        """.strip()
        
        try:
            send_mail(
                subject=subject_cliente,
                message=message_cliente,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=True
            )
        except Exception as e:
            logger.error(f"Error al enviar email de confirmación: {str(e)}")
        
        # Notificar al equipo de ventas
        subject_admin = f'Nueva Cotización: {nombre} - {empresa or "Sin empresa"}'
        message_admin = f"""
🍌 NUEVA SOLICITUD DE COTIZACIÓN

Datos del Cliente:
- Nombre: {nombre}
- Empresa: {empresa or 'No especificada'}
- Email: {email}
- Teléfono: {telefono or 'No especificado'}
- País: {dict(Cotizacion.PAISES_CHOICES).get(pais, pais)}

Detalles:
- Cantidad: {cantidad}
- Mensaje: {mensaje or 'Sin mensaje adicional'}

Fecha: {nueva_cotizacion.created.strftime('%d/%m/%Y %H:%M')}

---
Accede al panel de administración para gestionar esta solicitud.
        """.strip()
        
        try:
            send_mail(
                subject=subject_admin,
                message=message_admin,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=True
            )
        except Exception as e:
            logger.error(f"Error al notificar al admin: {str(e)}")
        
        cotizacion_enviada = True
        logger.info(f"Nueva cotización registrada: {nombre} - {email}")
        
    except Exception as e:
        error_mensaje = "Hubo un problema al procesar tu solicitud. Por favor, intenta más tarde."
        logger.error(f"Error al crear cotización: {str(e)}")
    
    return render(request, 'boceto/cotizacion.html', {
        'cotizacion_enviada': cotizacion_enviada,
        'error_mensaje': error_mensaje,
        'paises': Cotizacion.PAISES_CHOICES
    })


# ============================================
# 📰 VISTAS DE NOTICIAS
# ============================================

def noticias(request):
    """Vista que muestra todas las noticias/posts."""
    posts = Post.objects.all()
    return render(request, "boceto/noticias.html", {"posts": posts})

def ver_noticia(request, noticia_id):
    """Vista para ver el detalle de una noticia específica."""
    noticia = get_object_or_404(Post, id=noticia_id)
    return render(request, "boceto/ver_noticia.html", {"noticia": noticia})

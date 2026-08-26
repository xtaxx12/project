/* Interacciones del sitio: menú móvil, navbar al hacer scroll y dropdown accesible.
   Reemplaza a jQuery + scrolly + dropotron + scrollex (el scroll suave lo hace CSS). */
(function () {
    'use strict';

    // Menú móvil
    var toggle = document.getElementById('navToggle');
    var menu = document.getElementById('navMenu');
    if (toggle && menu) {
        toggle.addEventListener('click', function () {
            var open = menu.classList.toggle('active');
            toggle.classList.toggle('active', open);
            toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
        });
    }

    // Fondo sólido del navbar al hacer scroll
    var navbar = document.getElementById('navbar');
    if (navbar) {
        var onScroll = function () {
            navbar.classList.toggle('scrolled', window.scrollY > 50);
        };
        window.addEventListener('scroll', onScroll, { passive: true });
        onScroll();
    }

    // Dropdown "Emprendimientos": accesible por teclado y táctil
    document.querySelectorAll('.nav-dropdown > button').forEach(function (btn) {
        btn.addEventListener('click', function () {
            var open = btn.parentElement.classList.toggle('open');
            btn.setAttribute('aria-expanded', open ? 'true' : 'false');
        });
        document.addEventListener('click', function (e) {
            if (!btn.parentElement.contains(e.target)) {
                btn.parentElement.classList.remove('open');
                btn.setAttribute('aria-expanded', 'false');
            }
        });
        btn.parentElement.addEventListener('keydown', function (e) {
            if (e.key === 'Escape') {
                btn.parentElement.classList.remove('open');
                btn.setAttribute('aria-expanded', 'false');
                btn.focus();
            }
        });
    });

    // Cerrar el menú móvil al navegar a un ancla interna
    if (menu) {
        menu.querySelectorAll('a[href*="#"]').forEach(function (link) {
            link.addEventListener('click', function () {
                menu.classList.remove('active');
                if (toggle) {
                    toggle.classList.remove('active');
                    toggle.setAttribute('aria-expanded', 'false');
                }
            });
        });
    }
})();

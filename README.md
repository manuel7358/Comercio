# COMSERTEL - Servicios Residenciales Claro

Sitio web de COMSERTEL, comercializadora de servicios telefónicos y distribuidor líder de Claro en El Salvador. Ofrecemos servicios residenciales de conectividad, entretenimiento y comunicación para hogares y familias.

## Acerca de COMSERTEL

### Misión
En COMSERTEL nos dedicamos a comercializar y brindar soluciones de conectividad y entretenimiento del portafolio residencial de Claro El Salvador, ofreciendo a nuestros clientes un servicio cercano, confiable y de calidad, que contribuya a mejorar su comunicación, productividad y calidad de vida en el hogar.

### Visión
Ser el distribuidor líder de Claro en El Salvador en la comercialización de servicios residenciales, reconocido por la excelencia en la atención al cliente, la innovación en nuestras estrategias de venta y la generación de valor para nuestros colaboradores, clientes y socios comerciales.

### Servicios Ofrecidos
- **Internet Residencial**: Conexión de alta velocidad para hogares
- **Televisión por Suscripción**: Amplia variedad de canales nacionales e internacionales
- **Telefonía Fija**: Llamadas locales e internacionales
- **Paquetes Combinados**: Triple Play con precios competitivos

### Características del Sitio Web
- **Diseño Responsive**: Compatible con PC, tablet y smartphone
- **Base de Datos**: SQLite con SQLAlchemy para persistencia de datos
- **Seguridad**: Validación de formularios con CSRF protection
- **Interfaz Moderna**: Bootstrap 5 con Font Awesome icons
- **Código Limpio**: Estructura organizada y bien documentada

## Información de la Empresa

- **Nombre**: COMSERTEL (Comercializadora de Servicios Telefónicos)
- **Fundación**: 2017
- **Tamaño**: Mediana Empresa
- **Empleados**: Más de 60 colaboradores
- **Ubicación Principal**: Santa Ana, El Salvador
- **Sede Secundaria**: Refugio Ahuachapán (inauguración 2025)
- **Actividad Principal**: Distribución y comercialización de servicios residenciales de Claro El Salvador
- **Mercado Objetivo**: Hogares y familias en zonas urbanas y semiurbanas de El Salvador

## Tecnologías Utilizadas

- **Backend**: Python Flask
- **Base de Datos**: SQLAlchemy con SQLite
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Formularios**: Flask-WTF con validación
- **Iconos**: Font Awesome

## Estructura del Proyecto

```
comercio_electronico/
├── app.py                 # Aplicación principal Flask
├── seed.py               # Script para poblar la base de datos
├── requirements.txt      # Dependencias del proyecto
├── templates/            # Plantillas Jinja2
│   ├── base.html
│   ├── inicio.html
│   ├── galerias.html
│   ├── creadores.html
│   └── contacto.html
├── static/               # Archivos estáticos
│   └── images/           # Imágenes del sitio
└── README.md
```

## Instalación y Configuración

1. **Clonar el repositorio** (o crear los archivos según la estructura)

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación**:
   ```bash
   python app.py
   ```

4. **Poblar la base de datos** (opcional, para datos de ejemplo):
   ```bash
   python seed.py
   ```

5. **Acceder al sitio**:
   Abrir el navegador en `http://localhost:5000`

## Funcionalidades

### Páginas Principales
- **Inicio**: Página de bienvenida con navegación a secciones principales
- **Galerías**: Muestra productos/servicios con imágenes y descripciones
- **Creadores**: Información del equipo con fotos, nombres, carnets y roles
- **Contacto**: Formulario de contacto con validación

### Navegación Responsive
- **Desktop**: Barra de navegación horizontal superior
- **Mobile**: Menú lateral oculto con toggle

### Seguridad
- Validación de formularios del lado del servidor
- Protección CSRF en formularios
- Sanitización de datos de entrada

## Equipo de Desarrollo

El sitio web fue desarrollado por el equipo de COMSERTEL:

- **Bayona Paiz Fernando José** (BP16010) - Desarrollador de Software
- **Grande Barrera Bryan Armando** (GB14024) - Analista de Sistemas
- **Linares Montes Manuel Eliseo** (LM20063) - Especialista en Telecomunicaciones

## Desarrollo y Personalización

### Agregar Nuevos Servicios
Editar el archivo `seed.py` para agregar nuevos servicios de COMSERTEL a la base de datos.

### Agregar Imágenes
Colocar las imágenes en la carpeta `static/images/` con los nombres especificados en `seed.py`:
- `internet_residencial.jpg`
- `television_suscripcion.jpg`
- `telefonia_fija.jpg`
- `triple_play.jpg`
- `internet_tv.jpg`
- `internet_telefono.jpg`
- `bayona_paiz.jpg`
- `grande_barrera.jpg`
- `linares_montes.jpg`

### Personalizar Estilos
Modificar los estilos CSS en `templates/base.html` o crear archivos CSS adicionales en `static/css/`.

### Extender Funcionalidades
- Sistema de cotizaciones en línea
- Portal de clientes para seguimiento de servicios
- Integración con WhatsApp Business
- Sistema de agendamiento de visitas técnicas

## Contribución

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear un Pull Request

## Modelo de Negocio Digital

COMSERTEL implementa un **modelo B2C (Business to Consumer)** enfocado en el **negocio de suscripción digital**, ofreciendo servicios residenciales de Claro a hogares y familias salvadoreñas.

### Estrategia Digital
- **Facebook**: Promociones y atención al cliente
- **Instagram**: Contenido visual atractivo
- **WhatsApp Business**: Atención personalizada
- **Sitio Web**: Información y contacto en línea

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Contacto

**COMSERTEL**
- **Dirección**: Barrio Nuevo, Octava Avenida Sur entre Veintiuno y Veintitrés calle poniente, casa número noventa y siete, Santa Ana, Santa Ana
- **Teléfono**: +503 1234-5678
- **Email**: info@comsertel.com
- **Horario**: Lunes a Viernes 8:00 AM - 5:00 PM, Sábado 8:00 AM - 12:00 PM

Para soporte técnico del sitio web, contacta al equipo de desarrollo.
from app import app, db, Producto, Creador

# Crear datos de COMSERTEL
def seed_data():
    with app.app_context():
        # Limpiar datos existentes
        Producto.query.delete()
        Creador.query.delete()
        db.session.commit()

        # Crear servicios de COMSERTEL
        productos = [
            Producto(
                nombre="Internet Residencial",
                descripcion="Servicio de conexión a internet de alta velocidad para hogares. Planes desde $20 hasta $45 según necesidades de navegación, trabajo, estudio y entretenimiento. Instalación y soporte técnico incluidos.",
                imagen="images/internet_residencial.jpg",
                plan_basico="Básico - 10 Mbps",
                precio_basico=20.00,
                plan_estandar="Estándar - 25 Mbps",
                precio_estandar=30.00,
                plan_premium="Premium - 50 Mbps",
                precio_premium=45.00
            ),
            Producto(
                nombre="Televisión por Suscripción",
                descripcion="Acceso a una variedad de canales nacionales e internacionales. Paquetes desde $15 hasta $35 con diferentes opciones: deportes, películas, infantiles, etc. Tecnología digital con equipos modernos.",
                imagen="images/television_suscripcion.jpg",
                plan_basico="Básico - 80 canales",
                precio_basico=15.00,
                plan_estandar="Estándar - 120 canales",
                precio_estandar=25.00,
                plan_premium="Premium - 160 canales",
                precio_premium=35.00
            ),
            Producto(
                nombre="Telefonía Fija",
                descripcion="Servicio de llamadas locales e internacionales. Planes desde $10 hasta $20 con opciones de minutos ilimitados o por consumo. Calidad de audio y conexión estable.",
                imagen="images/telefonia_fija.jpg",
                plan_basico="Básico - 100 minutos",
                precio_basico=10.00,
                plan_estandar="Estándar - 300 minutos",
                precio_estandar=15.00,
                plan_premium="Premium - Ilimitado",
                precio_premium=20.00
            ),
            Producto(
                nombre="Paquete Triple Play",
                descripcion="Combinación de internet, televisión y telefonía en un solo plan desde $35 hasta $65. Precios competitivos y ahorro en comparación con servicios individuales. Facilita la facturación y mejora la experiencia del cliente.",
                imagen="images/triple_play.jpg",
                plan_basico="Básico - Internet 10Mbps + TV 80 canales + Tel 100 min",
                precio_basico=35.00,
                plan_estandar="Estándar - Internet 25Mbps + TV 120 canales + Tel 300 min",
                precio_estandar=50.00,
                plan_premium="Premium - Internet 50Mbps + TV 160 canales + Tel Ilimitado",
                precio_premium=65.00
            ),
            Producto(
                nombre="Internet + TV",
                descripcion="Paquete combinado de internet de alta velocidad y televisión por suscripción. Ideal para familias que buscan conectividad y entretenimiento con precios especiales.",
                imagen="images/internet_tv.jpg",
                plan_basico="Básico - Internet 10Mbps + TV 80 canales",
                precio_basico=28.00,
                plan_estandar="Estándar - Internet 25Mbps + TV 120 canales",
                precio_estandar=40.00,
                plan_premium="Premium - Internet 50Mbps + TV 160 canales",
                precio_premium=55.00
            ),
            Producto(
                nombre="Internet + Teléfono",
                descripcion="Servicio combinado de internet residencial y telefonía fija. Comunicación completa para el hogar con precios competitivos y beneficios adicionales.",
                imagen="images/internet_telefono.jpg",
                plan_basico="Básico - Internet 10Mbps + Tel 100 min",
                precio_basico=25.00,
                plan_estandar="Estándar - Internet 25Mbps + Tel 300 min",
                precio_estandar=38.00,
                plan_premium="Premium - Internet 50Mbps + Tel Ilimitado",
                precio_premium=50.00
            )
        ]

        # Crear equipo de desarrollo de COMSERTEL
        creadores = [
            Creador(
                nombre="Fernando José Bayona Paiz",
                carnet="BP16010",
                rol="Analista de Sistemas y Desarrollador de software",
                foto="images/bayona_paiz.jpg"
            ),
            Creador(
                nombre="Bryan Armando Grande Barrera",
                carnet="GB14024",
                rol="Especialista en Telecomunicaciones",
                foto="images/grande_barrera.jpg"
            ),
            Creador(
                nombre="Manuel Eliseo Linares Montes",
                carnet="LM20063",
                rol="Analista de Sistemas",
                foto="images/linares_montes.jpg"
            )
        ]

        # Agregar productos a la base de datos
        for producto in productos:
            db.session.add(producto)

        # Agregar creadores a la base de datos
        for creador in creadores:
            db.session.add(creador)

        # Confirmar cambios
        db.session.commit()
        print("Datos de COMSERTEL agregados exitosamente. Base de datos limpia y actualizada.")

if __name__ == "__main__":
    seed_data()
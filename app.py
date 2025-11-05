from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_mail import Mail, Message
import os

# =======================
# CONFIGURACIÓN INICIAL
# =======================
app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comercio_electronico.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# --- Configuración de correo directa (sin .env) ---
app.config['MAIL_SERVER'] = 'smtp.gmail.com'              # Servidor SMTP (Gmail)
app.config['MAIL_PORT'] = 587                             # Puerto TLS
app.config['MAIL_USE_TLS'] = True                         # Activar TLS
app.config['MAIL_USE_SSL'] = False                        # No usar SSL
app.config['MAIL_USERNAME'] = 'impresorsa371@gmail.com'   # Tu dirección de correo
app.config['MAIL_PASSWORD'] = 'dlmq sard qnyh cuhf'       # App Password de Gmail (sin espacios si los hubiera)
app.config['MAIL_DEFAULT_SENDER'] = ('COMSERTEL', 'impresorsa371@gmail.com')  # Nombre y remitente
app.config['MAIL_NOTIFY_TO'] = 'lm20063@ues.edu.sv'       # Destino para notificaciones internas

mail = Mail(app)
db = SQLAlchemy(app)

# =======================
# MODELOS DE BASE DE DATOS
# =======================
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    imagen = db.Column(db.String(200), nullable=False)
    plan_basico = db.Column(db.String(100), nullable=False)
    precio_basico = db.Column(db.Float, nullable=False)
    plan_estandar = db.Column(db.String(100), nullable=False)
    precio_estandar = db.Column(db.Float, nullable=False)
    plan_premium = db.Column(db.String(100), nullable=False)
    precio_premium = db.Column(db.Float, nullable=False)


class Creador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    carnet = db.Column(db.String(20), nullable=False)
    rol = db.Column(db.String(50), nullable=False)
    foto = db.Column(db.String(200), nullable=False)


class Contacto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    mensaje = db.Column(db.Text, nullable=False)


class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False)
    nombre_cliente = db.Column(db.String(100), nullable=False)
    email_cliente = db.Column(db.String(100), nullable=False)
    telefono_cliente = db.Column(db.String(20), nullable=False)
    plan_seleccionado = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    metodo_pago = db.Column(db.String(50), nullable=False)
    numero_tarjeta = db.Column(db.String(20), nullable=True)
    fecha_expiracion = db.Column(db.String(5), nullable=True)
    cvv = db.Column(db.String(4), nullable=True)
    nombre_tarjeta = db.Column(db.String(100), nullable=True)
    fecha_pedido = db.Column(db.DateTime, default=db.func.current_timestamp())

    producto = db.relationship('Producto', backref=db.backref('pedidos', lazy=True))

# =======================
# FORMULARIOS
# =======================
class ContactoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Correo Electrónico', validators=[DataRequired(), Email()])
    mensaje = TextAreaField('Mensaje', validators=[DataRequired()])
    submit = SubmitField('Enviar')


class PagoForm(FlaskForm):
    nombre = StringField('Nombre Completo', validators=[DataRequired()])
    email = StringField('Correo Electrónico', validators=[DataRequired()])
    telefono = StringField('Teléfono', validators=[DataRequired()])
    plan = StringField('Plan Seleccionado', validators=[DataRequired()])
    metodo_pago = StringField('Método de Pago', validators=[DataRequired()])
    numero_tarjeta = StringField('Número de Tarjeta')
    fecha_expiracion = StringField('Fecha de Expiración')
    cvv = StringField('CVV')
    nombre_tarjeta = StringField('Nombre en la Tarjeta')
    submit = SubmitField('Confirmar Pago')


# =======================
# CREACIÓN DE TABLAS
# =======================
with app.app_context():
    db.create_all()

# =======================
# RUTAS DE LA APLICACIÓN
# =======================
@app.route('/')
def inicio():
    return render_template('inicio.html')


@app.route('/galerias')
def galerias():
    productos = Producto.query.all()
    return render_template('galerias.html', productos=productos)


@app.route('/creadores')
def creadores():
    creadores = Creador.query.all()
    return render_template('creadores.html', creadores=creadores)


@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    form = ContactoForm()
    if form.validate_on_submit():
        # 1) Guardar mensaje en BD
        nuevo_contacto = Contacto(
            nombre=form.nombre.data,
            email=form.email.data,
            mensaje=form.mensaje.data
        )
        db.session.add(nuevo_contacto)
        db.session.commit()

        # 2) Enviar correos
        errores_mail = []
        try:
            # Correo a COMSERTEL
            msg_admin = Message(
                subject="Nuevo mensaje de contacto - COMSERTEL",
                recipients=[app.config['MAIL_NOTIFY_TO']]
            )
            msg_admin.body = (
                f"Has recibido un nuevo mensaje desde el formulario de contacto.\n\n"
                f"Nombre: {form.nombre.data}\n"
                f"Email: {form.email.data}\n\n"
                f"Mensaje:\n{form.mensaje.data}\n"
            )
            mail.send(msg_admin)

            # Acuse al usuario
            msg_user = Message(
                subject="Hemos recibido tu mensaje - COMSERTEL",
                recipients=[form.email.data]
            )
            msg_user.body = (
                f"Hola {form.nombre.data},\n\n"
                "¡Gracias por escribirnos! Hemos recibido tu mensaje y uno de nuestros asesores "
                "se pondrá en contacto contigo a la brevedad.\n\n"
                "Si necesitas atención inmediata, llámanos al +503 1234-5678.\n\n"
                "— Equipo COMSERTEL"
            )
            mail.send(msg_user)

        except Exception as e:
            errores_mail.append(str(e))

        # 3) Mostrar resultado
        if errores_mail:
            flash("Tu mensaje fue guardado, pero hubo un problema al enviar el correo.", "danger")
        else:
            flash("¡Gracias por tu mensaje! Te hemos enviado un acuse de recibo por correo.", "success")

        return redirect(url_for('contacto'))

    return render_template('contacto.html', form=form)


@app.route('/pago/<int:producto_id>', methods=['GET', 'POST'])
def pago(producto_id):
    producto = Producto.query.get_or_404(producto_id)
    form = PagoForm()
    if form.validate_on_submit():
        # Normalizar valores del form
        plan_sel = (form.plan.data or '').strip().lower()            # 'basico' | 'estandar' | 'premium'
        metodo_pago = (form.metodo_pago.data or '').strip().lower()  # 'tarjeta' | 'efectivo'

        # Calcular precio según plan
        try:
            precio = float(getattr(producto, f'precio_{plan_sel}'))
        except Exception:
            flash("Plan inválido. Selecciona nuevamente.", "danger")
            return redirect(url_for('pago', producto_id=producto_id))

        # Crear pedido
        nuevo_pedido = Pedido(
            producto_id=producto_id,
            nombre_cliente=form.nombre.data,
            email_cliente=form.email.data,
            telefono_cliente=form.telefono.data,
            plan_seleccionado=plan_sel,
            precio=precio,
            metodo_pago=metodo_pago
        )

        # Si el método de pago es tarjeta, guardar los datos
        if metodo_pago == 'tarjeta':
            nuevo_pedido.numero_tarjeta = form.numero_tarjeta.data
            nuevo_pedido.fecha_expiracion = form.fecha_expiracion.data
            nuevo_pedido.cvv = form.cvv.data
            nuevo_pedido.nombre_tarjeta = form.nombre_tarjeta.data

        db.session.add(nuevo_pedido)
        db.session.commit()

        # ====== ENVIAR CORREOS DE CONFIRMACIÓN ======
        # Texto legible del plan
        plan_human = {
            'basico': producto.plan_basico,
            'estandar': producto.plan_estandar,
            'premium': producto.plan_premium
        }.get(plan_sel, plan_sel)

        asunto_admin = f"Nuevo pedido #{nuevo_pedido.id} - {producto.nombre} ({plan_sel.capitalize()})"
        asunto_cliente = f"Confirmación de pedido #{nuevo_pedido.id} – COMSERTEL"
        precio_txt = f"${precio:,.2f} / mes"

        cuerpo_admin = (
            f"Se ha confirmado un nuevo pedido en COMSERTEL.\n\n"
            f"Pedido #: {nuevo_pedido.id}\n"
            f"Producto: {producto.nombre}\n"
            f"Plan: {plan_human}\n"
            f"Precio: {precio_txt}\n"
            f"Método de pago: {metodo_pago}\n"
            f"Fecha: {nuevo_pedido.fecha_pedido}\n\n"
            f"Cliente: {nuevo_pedido.nombre_cliente}\n"
            f"Email: {nuevo_pedido.email_cliente}\n"
            f"Teléfono: {nuevo_pedido.telefono_cliente}\n"
        )

        cuerpo_cliente = (
            f"Hola {nuevo_pedido.nombre_cliente},\n\n"
            f"¡Gracias por tu compra en COMSERTEL! Hemos recibido tu pedido y está en proceso.\n\n"
            f"Resumen del pedido:\n"
            f"  • Pedido #: {nuevo_pedido.id}\n"
            f"  • Producto: {producto.nombre}\n"
            f"  • Plan: {plan_human}\n"
            f"  • Precio: {precio_txt}\n"
            f"  • Método de pago: {metodo_pago}\n"
            f"  • Fecha: {nuevo_pedido.fecha_pedido}\n\n"
            f"Si necesitas asistencia, contáctanos al +503 1234-5678 o responde a este correo.\n\n"
            f"— Equipo COMSERTEL"
        )

        try:
            # Correo a COMSERTEL (admin)
            msg_admin = Message(
                subject=asunto_admin,
                recipients=[app.config['MAIL_NOTIFY_TO']],
                body=cuerpo_admin
            )
            mail.send(msg_admin)

            # Correo al cliente
            msg_cliente = Message(
                subject=asunto_cliente,
                recipients=[nuevo_pedido.email_cliente],
                body=cuerpo_cliente
            )
            mail.send(msg_cliente)

            flash("¡Pedido confirmado! Te enviamos un correo con el resumen.", "success")

        except Exception:
            # No detenemos el flujo si falla el correo
            flash("Pedido confirmado, pero hubo un problema al enviar el correo de confirmación.", "warning")

        # Redirigir a la página de confirmación
        return redirect(url_for('confirmacion', pedido_id=nuevo_pedido.id))

    return render_template('pago.html', producto=producto, form=form)


@app.route('/confirmacion/<int:pedido_id>')
def confirmacion(pedido_id):
    pedido = Pedido.query.get_or_404(pedido_id)
    return render_template('confirmacion.html', pedido=pedido)


# =======================
# EJECUCIÓN DE LA APP
# =======================
if __name__ == '__main__':
    app.run(debug=True)

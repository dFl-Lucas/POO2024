from flask import Flask, render_template, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import Sucursal, Repartidor, Transporte, Paquete


@app.route('/')
def inicio():
    return render_template('inicio.html')


@app.route('/despachante', methods = ['GET','POST'])
def despachante():
    if request.method == 'POST':
        if not request.form.get('sucursales'):
            return render_template('listarSucursales.html', sucursales=Sucursal.query.all(), sucursal_seleccionada=None)
        else:
            sucursal_selecionada = Sucursal.query.get(request.form['sucursales'])
            session["sucursal"] = sucursal_selecionada.id #Guardamos la id de la sucucrsal seleccionada para luego utilizarla
            return render_template('OpcionesDespachante.html')      
    else:
        return render_template('listarSucursales.html', sucursales=Sucursal.query.all(), sucursal_selecionada=None)
    

@app.route('/registrar_paquete', methods = ['GET','POST'])
def registrar_paquete():
    if request.method == 'POST':
        #Aca preguntamos si se ingresearon todos los datos requeridos, en caso de que no sea asi se muestra un error
        if not request.form['peso'] or not request.form['nombre'] or not request.form['direccion']:
            return render_template('informa.html', dato="Por favor ingrese los datos requeridos")
        else:
            paquetes = Paquete.query.all() #Nos traemos todos los paquetes
            for paq in paquetes: #Realizamos un bucle for para obtener el ultimo numero de de envio del paquete
                n= paq.numeroenvio
            #Utilizamos el ultimo numero de envio de paquete para sumarle 20 y agregarselo al nuevo paquete

            #Creamos un nuevo modelo de paquete para agregarlo a la base de datos utilizando los datos que ingreso en el formulario
            nuevo_paquete = Paquete(numeroenvio=(n+20) ,peso=request.form['peso'], nomdestinatario=request.form['nombre'], dirdestinatario=request.form['direccion'], entregado=False, observaciones='', idsucursal=session['sucursal'], idrepartidor=0, idtransporte=0)
            try: #Este bloque se utiliza para chequar si se cargo correctamente el paquete
                db.session.add(nuevo_paquete)
                db.session.commit()
                return render_template('registrarPaquete.html', dato='Paquete cargado correctamente')
            except:
                db.session.rollback() #Esta funcion deshace todo los cambios recientes en la base de datos en caso de error
                return render_template('registrarPaquete.html', dato='Error al cargar el paquete')
    return render_template('registrarPaquete.html', dato='')


@app.route('/salida_de_transporte', methods = ['GET','POST'])
def salida_transporte():
    if request.method == 'POST':
        if not request.form.get('sucursales') and not request.form.get('paquetes'): #Aca abajo manda las sucursales menos la que se selecciono al inicio y los paquetes de esa misma sucursal que no fueron entregados y tampoco se les asigno repartidor
            return render_template('salidaTransporte.html', sucursales=Sucursal.query.filter(Sucursal.id != session['sucursal']), sucursal_seleccionada=None, paquetes=Paquete.query.filter(Paquete.id==session['sucursal'] , Paquete.entregado==False, Paquete.idrepartidor==0), paquete_seleccionado=None)
        else:
            paq_selec = request.form.getlist('paquetes') #Traemos la lista de paquetes seleccionados, que es una lista de los id
            suc_selec = Sucursal.query.get(request.form['sucursales']) #Traemos la sucursal seleccionada a la que enviaremos los paquetes seleccionados
            transportes = Transporte.query.all() #Obtenemos todos los transportes para poder sacar el numero de transporte del nuevo transporte

            for transp in transportes:
                numT = transp.numerotransporte

            #Creamos el nuevo transporte con los datos correspondientes
            nuevo_transporte = Transporte(numerotransporte=(numT+1), fechahorasalida=datetime.now(), fechahorallegada=None, idsucursal=suc_selec.id)
            db.session.add(nuevo_transporte) #Agregamos el nuevo transporte a la base de datos

            for paq in paq_selec: #Lo que hago es traer de los paquetes el paquete con id=paq para poder asignarle la id de transporte
                xpaquete = Paquete.query.get(paq)
                xpaquete.idtransporte = nuevo_transporte.id

            try: #Este bloque se utiliza para chequar si se cargo correctamente el transporte
                db.session.commit()
                return render_template('informa.html', dato='Registro de transporte exitoso')
            except:
                db.session.rollback() #Esta funcion deshace todo los cambios recientes en la base de datos en caso de error
                return render_template('informa.html', dato='Ocurrio un error al cargar el transporte')
    else:
        return render_template('salidaTransporte.html', sucursales=Sucursal.query.filter(Sucursal.id != session['sucursal']) , sucursal_seleccionada=None, paquetes=Paquete.query.filter(Paquete.id==session['sucursal'],Paquete.entregado==False, Paquete.idrepartidor==0), paquete_seleccionado=None)


@app.route('/llegada_de_transporte', methods = ['GET','POST'])
def llegada_transporte():
    if request.method == 'POST':
        if not request.form.get('transportes'):
            return render_template('llegadaTransporte.html', transportes=Transporte.query.filter(Transporte.idsucursal==session['sucursal'], Transporte.fechahorallegada==None), transp_selec=None)
        else:
            transp_selec = Transporte.query.get(request.form['transportes'])
            transp_selec.fechahorallegada = datetime.now()

            try: #Utilizo este bloque para captar los errores al modificar datos en la base de datos
                db.session.commit()
                return render_template('informa.html', dato='Se registro la llegada del transporte con éxito')
            except:
                db.session.rollback()
                return render_template('informa.html', dato='Ocurrio un error al registrar la llegada del transporte')
    else:
        return render_template('llegadaTransporte.html', transportes=Transporte.query.filter(Transporte.idsucursal==session['sucursal'], Transporte.fechahorallegada==None), transp_selec=None)


@app.route('/repartidor', methods = ['GET','POST'])
def repartidor():
    '''if request.method == 'POST':
        repartidor_actual = Repartidor.query.filter_by(dni = request.form['dni']).first()
        if repartidor_actual is None:
            return render_template('error.html', error="No hay repartidor registrado con ese dni")
        else:
            verificacion = repartidor_actual.numero == request.form['numero']
            if (verificacion):
                #Aca se lo redireccionaria a una ruta donde muestre las diferentes opciones que pude realizar el repartidor
                pass'''
    return render_template('repartidor.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
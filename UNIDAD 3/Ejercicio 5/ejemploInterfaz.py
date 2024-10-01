class Producto:
    __codigo: int
    __descripcion: str
    __precio: float

    def __init__(self, codigo, descripcion, precio):
        self.__codigo=codigo
        self.__descripcion=descripcion
        self.__precio=precio

    def __str__(self):
        cadena = 'Codigo \tDescripcion \tPrecio \n'
        cadena += f'{self.__codigo} \t{self.__descripcion} \t{self.__precio}'
        return cadena
    
    def getDescripcion(self):
        return self.__descripcion
    
    def getCodigo(self):
        return self.__codigo
    
    def modificarPrecio(self, precio):
        self.__precio=precio

from zope.interface import Interface
from zope.interface import implementer
'''Declaración de interface ICajero
El Cajero solo puede buscar productos por descripción
el método declarado es
buscarProductoPorDescripcion(descripcion)
'''
class ICajero(Interface):
    def buscarProductoPorDescripcion(descripcion):
        pass
    '''Declaración de interface ISupervisor
    El Supervisor modificar el precio de un producto, que busca por código
    Los métodos que declara la intereface es
    buscarProductoPorCodigo(codigo)
    modificarPrecioProducto(codigo, precio)
    '''
class ISupervisor(Interface):
    def buscarProductoPorCodigo(codigo):
        pass
    def modificarPrecioProducto(codigo, precio):
        pass

@implementer(ICajero)
@implementer(ISupervisor)
class ManejadorProductos:
    __productos: list

    def __init__(self):
        self.__productos=[]

    def agregarProducto(self, producto):
        self.__productos.append(producto)

        '''Método de la interface ICajero'''
    def buscarProductoPorDescripcion(self, descripcion):
        i=0
        bandera=False
        retorno=None
        while not bandera and i<len(self.__productos):
            unProducto=self.__productos[i]
            if unProducto.getDescripcion()==descripcion:
                bandera=True
            else:
                i+=1
        if bandera:
            retorno = self.__productos[i]
        return retorno

    '''Métodos de la interface ISupervisor'''
    def buscarProductoPorCodigo(self, codigo):
        i=0
        bandera=False
        retorno=None
        while not bandera and i<len(self.__productos):
            unProducto = self.__productos[i]
            if unProducto.getCodigo()==codigo:
                bandera=True
            else:
                i+=1
        if bandera:
            retorno = self.__productos[i]
        return retorno

    def modificarPrecio(self, codigo, precio):
        producto = self.buscarProductoPorCodigo(codigo)
        if producto == None:
            print('Producto código {}, no encontrado'.format(codigo))
        else:
            producto.modificarPrecio(precio)

def cajero(manejarVendedor: ICajero):
    descripcion = input('Descripcion de producto a buscar: ')
    producto = manejarVendedor.buscarProductoPorDescripcion(descripcion)
    if producto == None:
        print('Producto {}, no encontrado'.format(descripcion))
    else:
        print(producto)

def supervisor(manejarSupervisor: ISupervisor):
    codigo = int(input('Código del producto a cambiar precio: '))
    producto = manejarSupervisor.buscarProductoPorCodigo(codigo)
    if producto == None:
        print('No hay un Producto con código {}'.format(codigo))
    else:
        print(producto)
        precio=float(input('Nuevo precio: '))
        manejarSupervisor.modificarPrecio(codigo, precio)
        print(producto)

def testInterfaces():
    manejadorProductos = ManejadorProductos()
    unProducto = Producto(1,'Arroz 1kg',52)
    manejadorProductos.agregarProducto(unProducto)
    unProducto = Producto(2,'Yerba 1/2kg',120)
    manejadorProductos.agregarProducto(unProducto)
    usuario = input('Usuario (Admin/Cajero): ')
    clave = input('Clave:')
    if usuario.lower() == 'Admin'.lower() and clave =='a54321':
        '''testeando supervisor '''
        supervisor(ISupervisor(manejadorProductos))
    else:
        if usuario.lower() == 'Cajero'.lower() and clave == 'c12345':
            '''testeado cajero'''
            cajero(ICajero(manejadorProductos))
            
if __name__=='__main__':
    testInterfaces() 
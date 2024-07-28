class Clientes:

    def __init__(self):
        noIdentificacionCliente = None
        nombre = None
        apellido = None
        direccion = None
        telefono = None
        correoElectronico = None

    # crear la tabla servicios si no existe
    def crearTablaClientes(self, objetoConexion):
        objetoCursor = objetoConexion.cursor()
        crear = """CREATE TABLE IF NOT EXISTS Clientes(
                noIdentificacionCliente integer NOT NULL,
                nombre text NOT NULL,
                apellido text NOT NULL,
                direccion text NOT NULL,
                telefono integer NOT NULL,
                correoElectronico text NOT NULL,
                PRIMARY KEY(noIdentificacionCliente))
                """
        objetoCursor.execute(crear)
        objetoConexion.commit()

    # escribir un cliente para insertar luego
    def leerCliente(self):
        noIdentificacionCliente = input("Número de identificación del cliente: ").ljust(10)
        nombre = input("Nombre: ").lower()
        apellido = input("Apellido: ").lower()
        direccion = input("Direccion: ").lower()
        telefono = input("Teléfono: ")
        correoElectronico = input("Correo Electrónico: ").lower()
        cliente = (noIdentificacionCliente,nombre,apellido,direccion,telefono,correoElectronico)
        return cliente

    # inserta un registro
    def insertarTablaClientes(self, con, miCliente):
        objetoCursor = con.cursor()
        insertar = "INSERT INTO clientes VALUES(?,?,?,?,?,?)"
        objetoCursor.execute(insertar, miCliente)
        con.commit()
        print("Nuevo Cliente agregado.")

    # consultar todos los registros
    def consultarTablaClientes1(self, objetoConexion):
        objetoCursor = objetoConexion.cursor()
        consultar = "SELECT * FROM Clientes"
        objetoCursor.execute(consultar)
        resultadosBusqueda = objetoCursor.fetchall()
        if not resultadosBusqueda:
            print("Tabla vacia.")
        else:
            print("Los registro de la tabla clientes son: ")
            for n, (id, nom, ape, dir, tel, cor) in enumerate(resultadosBusqueda, start=1):
                print(f"{n}. | {id}, {nom} {ape}, {dir}, {tel}, {cor}")

    # consultar un dato especifico de un cliente
    def consultarTablaClientes2(self, objetoConexion, datoBusqueda, noIdentificacionCliente):
        objetoCursor = objetoConexion.cursor()
        consultar = f"SELECT {datoBusqueda} FROM Clientes WHERE noIdentificacionCliente = '{noIdentificacionCliente}'"
        objetoCursor.execute(consultar)
        resultadosBusqueda = objetoCursor.fetchone()[0]
        if not resultadosBusqueda:
            print("Dato inexistente")
        else:
            print("El dato",datoBusqueda,"del registro",noIdentificacionCliente,"es",resultadosBusqueda)
            return resultadosBusqueda

    # consultar cuantos registros hay en total
    def consultarTablaSClientes3(self, objetoConexion):
        objetoCursor = objetoConexion.cursor()
        consultar = "SELECT COUNT(*) FROM Clientes"
        objetoCursor.execute(consultar)
        total = objetoCursor.fetchone()[0]
        return total

    # consultar registro por nombre
    def consultarTablaClientes3(self,objetoConexion,nombre):
        objetoCursor=objetoConexion.cursor()
        consultar = f"SELECT * FROM Clientes WHERE nombre = '{nombre}'"
        objetoCursor.execute(consultar)
        resultadosBusqueda = objetoCursor.fetchall()
        if not resultadosBusqueda:
            print("Datos inexistentes")
        else:
            print("Coincidencias encontradas:")
            for n, (id, nom, ape, dir, tel, cor) in enumerate(resultadosBusqueda, start=1):
                print(f"{n}. | {id}, {nom} {ape}, {dir}, {tel}, {cor}")
            return resultadosBusqueda

    # consultar registros por letra inicial del nombre en la tabla de clientes
    def consultarTablaClientes4(self, objetoConexion, letraInicial):
        cursorObj = objetoConexion.cursor()
        consulta = f"SELECT * FROM Clientes WHERE nombre LIKE '{letraInicial}%'"
        cursorObj.execute(consulta)
        resultadosBusqueda = cursorObj.fetchall()
        if not resultadosBusqueda:
            print("Dato inexistente")
        else:
            print("Coincidencias encontradas:")
            for n, (id, nom, ape, dir, tel, cor) in enumerate(resultadosBusqueda, start=1):
                print(f"{n} | {id} | {nom} {ape} | {dir} | {tel} | {cor}")

    # actualiza un dato de un registro de la tabla de clientes
    def actualizarTablaClientes(self, objetoConexion, tipoDato, noIdentificacionCliente, datoActualizar):
        objetoCursor = objetoConexion.cursor()
        actualizar = f"UPDATE Clientes SET {tipoDato} = '{datoActualizar}' WHERE noIdentificacionCliente = '{noIdentificacionCliente}'"
        if objetoCursor.rowcount == 0:
            print("El registro que intenta actualizar no existe.")
        else:
            objetoCursor.execute(actualizar)
            # si el dato actualizado es 'noIdentificacionCliente', también actualiza la tabla de Ventas
            if tipoDato == "noIdentificacionCliente":
                actualizarEnVentas = f"UPDATE Ventas SET noIdentificacionCliente = '{datoActualizar}' WHERE noIdentificacionCliente = '{noIdentificacionCliente}'"
                objetoCursor.execute(actualizarEnVentas)
            objetoConexion.commit()

    # borra un registro
    def borrarRegistroTablaClientes(self, objetoConexion,noIdentificacionCliente):
        objetoCursor= objetoConexion.cursor()
        borrar = f"DELETE FROM clientes WHERE noIdentificacionCliente = '{noIdentificacionCliente}'"
        if objetoCursor.rowcount == 0:
            print("El registro que intenta eliminar no existe.")
            objetoConexion.rollback()
        else:
            objetoCursor.execute(borrar)
            objetoConexion.commit()
            print("Acción borrar registro ejecutada")

    # borrar toda la tabla de clientes
    def borrarTablaClientes(self, objetoConexion):
        objetoCursor = objetoConexion.cursor()
        borrar = 'DROP TABLE IF EXISTS Clientes'
        objetoCursor.execute(borrar)
        objetoConexion.commit()

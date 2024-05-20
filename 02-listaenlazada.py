#creo la clase nodo
class Nodo:
    #creo el contructor de la clase que por defecto lleva los datos de dato y punteo que es siguiente
    def __init__(self,dato=None,siguiente=None):
        #dato sera el valor que se guarde
        self.dato = dato
        #siguiente sera el puntero que ara referencia de a donde apunta
        self.siguiente = siguiente

#defino la clase lista para ir creano la lista enlazada
class Lista:
    #creo el constructor que en este cazo sera la cabeza
    def __init__(self):
        #debo crear vacio el valor porque esta lista se iniciara vacia
        self.head = None;

    #funcion para incertar al principio los valores
    def insertarinicio(self,dato):
        #le digo que en la cabeza guarde el nodo con el dato y el apuntador hacia la cabeza
        self.head = Nodo(dato = dato, siguiente = self.head);

    #creamos la funcion para incertar al final
    def insertarfinal(self,dato):
        
        if(self.head == None):
            #si la cabeza esta vacia le coloco al inicio
            self.head = Nodo(dato=dato,siguiente=None);
        else:
            #sino en el auxiliar le cargo los datos de la cabeza
            self.auxiliar = self.head;
            #recorro el auxiliar hasta que apunte a nulo
            while(self.auxiliar.siguiente!=None):
                self.auxiliar = self.auxiliar.siguiente;
            #si apunta a nulo quiere decir que es la ultim posicion y saliendo del bucle
            #a este apuntador le doy el dato que he creado
            self.auxiliar.siguiente = Nodo(dato=dato,siguiente=None);

    #comprobar que no este vacia la funcion
    def estaVacia(self):
        if(self.head==None):
            return True;
        else:
            return False;

    #contar elementos
    def contador(self):
        #compruebo que la lista no este vacia
        if (self.head==None):
            print("la lista esta vacia");
        else:
            #creo un contador para que determine el tamaño de datos
            contador=int(1);
            #cargo los datos en el auxiliar
            self.auxiliar=self.head;
            #le hago recorrer al auxiliar mientras no apunte a nulo
            while(self.auxiliar.siguiente!=None):
                self.auxiliar=self.auxiliar.siguiente;
                #al contador le aumento uno, inicie en uno porque asi contaria los casilleros llenos
                contador=contador+1;
            return contador;
    
    #funcion para eliminar la cabeza de la lista
    def eliminarCabeza(self):
        #compruebo que no este vacio
        if(self.head==None):
            print("la lista esta vacia");
        else:
            #si tiene elementos cargo en el auxiliar el puntero de cabeza a siguiente
            self.auxiliar=self.head.siguiente;
            #luego en la caveza vuelvo a colocar el resto de elementos guardados
            self.head=self.auxiliar;
            #por seguridad el auxiliar lo vacio apuntando a null
            self.auxiliar=None;

    #funcion para eliminar la cola
    def eliminarcola(self):
        #compruebo que la cabeza no este vacia
        if(self.head==None):
            print("esta vacia la lista");
        else:
            #cargo en el auxiliar los datos
            self.auxiliar = self.head;
            #recorro el auxiliar con dos apuntadores seguidos, porque asi estoy seguro que estara apuntando al null
            #un elemento que quiero mantenerlo y el segundo sera el que yo quiero removerlo
            while(self.auxiliar.siguiente.siguiente!=None):
                self.auxiliar=self.auxiliar.siguiente;
            #entonces si lo encuentra quiero que solo lo remueva al segundo apuntador y conservo el primero
            #y el segundo le apunto a null
            self.auxiliar.siguiente=None;
    
    #eliminar por posicion
    def aliminarporPosicion(self,posicion):
        #compruebo que no este vacia la lista
        if(self.head==None):
            print("la lista esta vacia");
        else:
            #cargo la lista en el auxiliar
            self.auxiliar=self.head;
            #creo la variable para ir contando
            sumando=int(0);
            #con el bucle recorro la lista
            #la posicion -1 es porque asi se que al que esta antes de posicion le quito el puntero
            #hacia el numero que tengo que eliminarlo y le apunto hacia el que esta luego de la posicion
            while(sumando<(posicion-1)):
                self.auxiliar=self.auxiliar.siguiente;
                sumando=sumando+1;
            #creo un temporar y aqui guardo como cabeza el que quiero eliminar
            self.temporal=self.auxiliar.siguiente;
            #entonces en la lista quedo un apuntador del que estaba antes del que buscaba
            #ahora ese apuntador señalo hacia el apuntador de la cabeza creada la linea anterior
            self.auxiliar.siguiente=self.temporal.siguiente;
            #como el temporal queda con esa cabeza artificial le alimino apuntando a null
            self.temporal=None;
    
    #reemplazar un elemento o editarlo
    def reemplazarelemento(self,numero,elemento):
        #compruebo si la lista esta vacia
        if(self.estaVacia()):
            print("esta vacia la lista");
        else:
            #paso los datos al auxiliar
            self.auxiliar = self.head;
            #recorro el auxiliar
            while(self.auxiliar != None):
                #si el dato guardado en el nodo es igual al numero le reemplazo
                if(self.auxiliar.dato == numero):
                    self.auxiliar.dato=elemento;
                self.auxiliar=self.auxiliar.siguiente;

    # Método para imprimir la lista de nodos
    def verlista( self ):
        #compruebo que la lista no este vacia
        if(self.head == None):
            print("en la cabeza esta vacia aun")
        else:
            #le paso al auxiliar los datos creados en la lista
            self.auxiliar = self.head
            #recorro los datos con el puntero
            while self.auxiliar != None:
                #imprimo los datos almacenados dentro del puntero
                print(self.auxiliar.dato, end =" => ")
                self.auxiliar = self.auxiliar.siguiente

#creo el objeto de lista
lista = Lista()
verdad = True
while(verdad):
    print("------opciones------");
    print("1 ingresar elemento al principio");
    print("2 ingresar elementos al final");
    print("3 eliminar la cabeza");
    print("4 eliminar la cola");
    print("5 eliminar por posicion");
    print("6 reemplazar un elemento");
    opcion = int(input("0 si desea salir"));
    if (opcion == 0):
        verdad = False 
    elif(opcion ==1):
        #aqui le pido un dato
        numero = input("ingrese un numero para colocar al frente de la lista: ");
        lista.insertarinicio(numero);
    elif(opcion==2):
        numero1 = input("ingrese un numero para colocar al final de la lista: ");
        lista.insertarfinal(numero1);
    elif(opcion==3):
        lista.eliminarCabeza();
    elif(opcion==4):
        lista.eliminarcola();
    elif(opcion==5):
        posicion=int(input("que posicion de la lista desea eliminar: "));
        lista.aliminarporPosicion(posicion);
    elif(opcion==6):
        numero1=input("que elemento de la lista desea reemplezar: ");
        nuevo=input("ingrese el valor que va a reemplar al antiguo: ");
        lista.reemplazarelemento(numero1,nuevo);
    #imprimo para ver el dato
    lista.verlista();
    print("");
    print("tamaño de la lista",lista.contador());
    print("")
    
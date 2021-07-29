class Contacto:
    def __init__(self,nombre,telefono,email):
        self.nombre=nombre
        self.telefono=telefono
        self.email=email
    
    
    def __str__(self):
        return f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t {self.telefono}\n" \
               f"DESCRIPCIÓN\t {self.email}\n"


def buscar_contacto(nom_cont,lista_agenda):
    """Se busca un contacto a partir del nombre """
    for x in lista_agenda:ULLDOG FRANCES
        if x.nombre == nom_cont:
            return x
    return None



def anadir_contacto(agenda):

    nombre=input('Ingrese nombre:\t')
    telefono=int(input('Ingrese telefono:\t'))
    email=input('Ingrese email:\t')
    x = Contacto(nombre,telefono,email)
    agenda.append(x)
    print('\nContacto añadido')

def listar_agenda(agenda):
    print()
    print('LISTA DE CONTACTOS')
    print()
    for x in agenda:
        x.mostrarAtributos()
        print('----------------------')

def imprimir_contacto(agenda):
    nombre_cont=input('Ingrese nombre a buscar:\t')
    contacto = buscar_contacto(nombre_cont,agenda)
    if contacto == None:
        print('\nNo se encontro el nombre  en la agenda')
    else:             
        print(f'Telefono: {contacto.telefono}')
        print(f'email: {contacto.email}')


def editar_contacto(agenda):
    nombre_cont=input('Ingrese nombre a buscar:\t')
    contacto = buscar_contacto(nombre_cont,agenda)
    if contacto == None:
        print('\nNo se encontró el nombre en la agenda')
    else:
        nombre = input('Ingrese nombre: ')
        telefono = int(input('Ingrese telefono: '))
        email = input('Ingrese email: ')
        contacto.nombre = nombre
        contacto.email = email
        contacto.telefono = telefono
        print('\nEdición terminada')
    

agenda=[]

while True:
    print('\nElegir opcion:')
    print('1. Añadir contactos')
    print('2. Lista de contactos')
    print('3. Buscar contactos')
    print('4. Editar contacto')
    print('5. Cerrar agenda')

    while True:     
        try:
            op =int(input('\nIngrese su opcion:\t'))
            
            if op==1:  #Añado contacto
                anadir_contacto(agenda)
                break
            elif op==2: #Imprimir lista de contactos
                listar_agenda(agenda)
                break
            elif op==3: # Busca contacto e imprime sus datos
                imprimir_contacto(agenda)
                break        
            elif op==4: #Edita contacto
                editar_contacto(agenda)
                break
                
            elif op==5:
                print("\nAGENDA CERRADA")
                break      
                
            else:
                print('\nERROR.Escriba un numero del 1 al 5')
                    
        except ValueError:
            print('\nERROR.Debe ingresar un NUMERO de 1 a 5')

    if op == 5:
        break    


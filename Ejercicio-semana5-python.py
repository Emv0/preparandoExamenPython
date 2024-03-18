import random;

bandas = [];

print("***ALTAVOZ ES TU VOZ***");
print("***********************");

opcion = 100;

while(opcion != 5):
    
    print("(1) Registrar banda");
    print("(2) Buscar banda");
    print("(3) Agenda del evento");
    print("(4) Modificar una banda");
    print("(5) Salir");
    
    try:
        opcion = int(input("Digita una opcion: "));
    except:
        print("********\nPor favor ingresa una opción valida\n********")
    
    if(opcion == 1):
        
        banda = {};
        banda["id"] = random.randint(1,100);
        banda["nombre"] = input("Nombre de la banda: ").lower();
        banda["genero"] = input("Genero: ");
        banda["clasificacion"] = input("Clasificacion: ");
        banda["tiempo"] = int(input("Tiempo: "));
        banda["costo"] = int(input("Costo: $"));
        bandas.append(banda);

    elif(opcion == 2):
        if bandas == [] :
            print("************\nDebes ingresar una banda antes de buscar\n************");
        else:
            bandaBuscada = input("************\nDigita el nombre de la banda que estas buscando: ").lower();
            for bandaAuxiliar in bandas:
                if(bandaAuxiliar["nombre"] == bandaBuscada):
                    bandaEncontrada = True;
                    nombreBanda = bandaAuxiliar["nombre"];
                    break;
                else:
                    bandaEncontrada = False;
            print(f"******\nBanda no encontrada\n******") if bandaEncontrada is False else print(f"************\nId: {bandaAuxiliar['id']}\nNombre: {nombreBanda.capitalize()}\nClasificacion: {bandaAuxiliar['clasificacion']}\nGenero: {bandaAuxiliar['genero']}\nTiempo: {bandaAuxiliar['tiempo']}\nCosto: ${bandaAuxiliar['costo']}\n************");
            
    elif(opcion == 3):
        if bandas == [] :
            print("************\nDebes ingresar una banda antes de consultar el evento\n************");
        else :
            for index,bandaAuxiliar in enumerate(bandas):
                print(f'************\nBanda n°{index+1}\nid: {bandaAuxiliar["id"]}\nNombre: {bandaAuxiliar["nombre"]}\nClasificacion: {bandaAuxiliar["clasificacion"]}\nGenero: {bandaAuxiliar['genero']}\nTiempo: {bandaAuxiliar["tiempo"]}\nCosto: ${bandaAuxiliar["costo"]}\n************');
    elif(opcion == 4):
        b = 0;
        if bandas == [] :
            print("************\nDebes ingresar una banda antes de consultar el evento\n************");
        else :
            bandaEncontrada = True;
            bandaBuscada = input("************\nDigita el nombre de la banda que deseas modificar: ").lower();
            for index,bandaAuxiliar in enumerate(bandas) : 
                if(bandaAuxiliar['nombre'] == bandaBuscada):
                    nombreBanda = bandaAuxiliar["nombre"];
                    (f"************\nId: {bandaAuxiliar['id']}\nNombre: {nombreBanda.capitalize()}\nClasificacion: {bandaAuxiliar['clasificacion']}\nGenero: {bandaAuxiliar['genero']}\nTiempo: {bandaAuxiliar['tiempo']}\nCosto: ${bandaAuxiliar['costo']}\n************");
                    try:    
                        opcionModificar = int(input("************\nDigita una opción dependiendo la accion que desees realizar con la banda\n1) Eliminar banda 2) Editar banda 3) Volver al menú : "));
                        print("************")
                    except:
                        print("************\nDigita una opción valida\n************");
                    if opcionModificar == 1 : 
                        bandas.pop(index)
                        print("Banda eliminada");
                        b = b+1
                        break;
                    elif opcionModificar == 2:
                        bandaAuxiliar['nombre'] = input("Nuevo nombre: ").lower();
                        bandaAuxiliar['clasificacion'] = input("Nueva clasificación: ");
                        bandaAuxiliar['genero'] = input("Nuevo genero: ");
                        bandaAuxiliar['tiempo'] = input("Nuevo tiempo: ");
                        bandaAuxiliar['costo'] = input("Nuevo costo: ");
                        print("************\nBanda editada satisfactoriamente\n************");
                        break;
                    elif opcionModificar == 3: 
                        break;
                else:
                    bandaEncontrada = False;
            print(f"************\n No se encontro ninguna banda con el nombre {bandaBuscada} \n************") if bandaEncontrada is False and b==0 else print("************\nSolicitud finalizada\n************");
    '''
    1) validar que una entrada sea un número
    2) 
    ''' 
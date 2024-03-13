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
    
    opcion = int(input("Digita una opcion: "));
    
    if(opcion   == 1):
        
        banda = {};
        banda["id"] = random.randint(1,100);
        banda["nombre"] = input("Nombre de la banda: ");
        banda["genero"] = input("Genero: ");
        banda["clasificacion"] = input("Clasificacion: ");
        banda["tiempo"] = int(input("Tiempo: "));
        banda["costo"] = int(input("Costo: $"));
        bandas.append(banda);

    elif(opcion == 2):
    
        bandaBuscada = input("Digita el nombre de la banda que estas buscando");
        for bandaAuxiliar in bandas:
            if(bandaAuxiliar["nombre"] == bandaBuscada):
                print(f"************ \n Id: {bandaAuxiliar["id"]} \n Nombre: {bandaAuxiliar["nombre"]} \n Clasificacion: {bandaAuxiliar["clasificacion"]} \n Tiempo: {bandaAuxiliar["tiempo"]} \n Costo: {bandaAuxiliar["costo"]}")
            else:
                print("Banda no encontrada")
    
    elif(opcion == 3):
        for index,bandaAuxiliar in enumerate(bandas):
            print(f'************ \n Banda {index+1} \n {bandaAuxiliar["id"]} \n {bandaAuxiliar["nombre"]} \n {bandaAuxiliar["clasificacion"]} \n {bandaAuxiliar["tiempo"]} \n {bandaAuxiliar["costo"]} \n ************');
    elif(opcion == 4):
        pass;
    
    '''
    1) validar que una entrada sea un número
    2) 
    
    '''
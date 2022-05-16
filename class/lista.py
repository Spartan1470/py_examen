lista=[]
while(True):
    print("")
    print("***************")
    print("1->para registrar ciclista.")
    print("2->para mostrar ciclistas registrados.")
    print("3->para mostrar  el tiempo de los ciclistas.")
    print("4->finalizar.")
    print("***************")
    option=int(input("ingrese una option:"))

    if(option==1):
        nombre=input("registre nombre del ciclista:")
        edad=input("registre edad del ciclista:")
        nacionalidad=input("registre nacionalidad ciclista:")
        tiempo=input("registre el tiempo del ciclista:")
        lista.append(lista)

    elif(option==2):
            print(lista)

    elif(option==3):
            print(tiempo)
    elif(option==4):
        print("operacion finalizada!")
        break
    else:
        print("Error")

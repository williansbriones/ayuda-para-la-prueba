import numpy as np
boleto=["6"]
nombrePasajero=["willy"]
rut=["20811954"]
telefono=["50945356"]
banco=["Banco DUOC"]
compra=[nombrePasajero,rut,telefono,banco,boleto]
###########################################################################################
def menu():
    accion=int(input("Indique que accion decea realizar\n1)asientos disponibles\n2)comprar boletos\n3)anular vuelos\n4)Modificar datos de pasajero\n5)salir"))
    while True:
            if accion<0 or accion>5:

                accion=int(input("Indique una accion correcta\n1)asientos disponibles\n2)comprar boletos\n3)anular vuelos\n4)Modificar datos de pasajero\n5)salir"))
            else:
                break
    return(accion)
def arrays():
    acum=0
    asientos_normal=np.ones([5,6],dtype="int32")
    for i in range(5):
        for e in range(6):
            asientos_normal[i][e]=asientos_normal[i][e]+acum
            acum=acum+1
    asientos_vip=np.ones([2,6],dtype="int32")
    for i in range(2):
        for e in range(6):
            asientos_vip[i][e]=asientos_vip[i][e]+acum
            acum=acum+1
    total_asientos_n=np.concatenate((asientos_normal,asientos_vip),axis=0,dtype="int32")
    total_asientos=np.concatenate((asientos_normal,asientos_vip),axis=0,dtype="str")
    return(total_asientos,total_asientos_n)
def disponibles_num(total_asientos,total_asientos_n):
    tabla=""
    acum_c=0
    for i in range(7):
        for e in range(6):
            acum_c=acum_c+1
            if total_asientos[i][e].isnumeric():
                numero=total_asientos_n[i][e]
                
                if numero < 10:
                    tabla=tabla + "| "+ total_asientos[i][e]
                if numero > 9:
                    tabla=tabla + "|"+ total_asientos[i][e]
            else:
                tabla=tabla + "| "+ total_asientos[i][e]
            if acum_c==6:
                acum_c=0
                tabla=tabla + "\n"
    print(tabla)
    return(tabla)
def compra_fun(total_asientos,total_asientos_n,check):
    c=disponibles_num(total_asientos, total_asientos_n)
    compra_us=input("que boleto comprara")
    result=np.where(total_asientos==compra_us)
    while True:
        if compra_us in total_asientos:
            break
        else:
            compra_us=input("indique un boleto valido")
            result=np.where(total_asientos==compra_us)
    if total_asientos_n[result]<31:
        nombre=input("el valor de este vuelo es de: $78.900\nCual es su nombre:")
        while True:
            if len(nombre)>2:
                 break
            else:
                nombre=input("indique un nombre valido")
        rut=input("induque su rut sin DV")
        while True:
            if len(rut)<9 and len(rut)>6:
                break
            else:
                rut=input("induque un rut valido")
        telefono=input("indique su telefon sin el 9")
        while True:
            if len(telefono)==8:
                break
            else:
                telefono=input("induque un telefono valido")
        banco=input("Indique cual es su banco\n 1) Banco DUOC UC 2) Banco Chile")
        while True:
            if banco=="1":
                print ("su banco es el *banco DUOC UC*")
                break
            elif banco=="2":
                print ("su banco es el *banco De Chile*")
                break
            else:
                banco=input("Indique un banco correcto\n 1) Banco DUOC UC 2) Banco Chile")
        valor=78900
        if banco=="1":
            valor_des=78900*0.15
            input(f"usted tiene un total a pagar de {valor-valor_des} de un total de {valor}")
            check.append([nombre,rut,telefono,"banco Duoc",compra_us])
        else:
            valor_des=78900*0.15
            input(f"usted tiene un total a pagar de {valor} de un total de {valor}")
            check.append([nombre,rut,telefono,"banco De Chile",compra_us])

    else :
        nombre=input("el valor de este vuelo es de: $240.000\nCual es su nombre:")
        while True:
            if len(nombre)>2:
                 break
            else:
                nombre=input("indique un nombre valido")
        rut=input("induque su rut sin DV")
        while True:
            if len(rut)<9 and len(rut)>6:
                break
            else:
                rut=input("induque un rut valido")
        telefono=input("indique su telefon sin el 9")
        while True:
            if len(telefono)==8:
                break
            else:
                telefono=input("induque un telefono valido")
        banco=input("Indique cual es su banco\n 1) Banco DUOC UC 2) Banco Chile")
        while True:
            if banco=="1":
                print ("su banco es el *banco DUOC UC*")
                break
            elif banco=="2":
                print ("su banco es el *banco De Chile*")
                break
            else:
                banco=input("Indique un banco correcto\n 1) Banco DUOC UC 2) Banco Chile")
        valor=240000
        if banco=="1":
            valor_des=valor*0.15
            input(f"usted tiene un total a pagar de {valor-valor_des} de un total de {valor}")
            check.append([nombre,rut,telefono,"banco Duoc",compra_us])
        else:
            valor_des=valor*0.15
            input(f"usted tiene un total a pagar de {valor} de un total de {valor}")
            check.append([nombre,rut,telefono,"banco De Chile",compra_us])
    total_asientos[result]="x"
    return(total_asientos,check)
def anulacion(bol,check,total_asientos,total_asientos_n):
    anulacion=input("Que pasaje desea elimir")
    while True:
        if anulacion in bol and anulacion.isnumeric():
            dele=bol.index(anulacion)
            print(dele)
            break
        else:
            anulacion=input("indica un ticket valido")
    anulacion_int=int(anulacion)
    result=np.where(total_asientos_n==anulacion_int)
    total_asientos[result]=anulacion
    
    del check [0][dele]
    del check [1][dele]
    del check [2][dele]
    del check [3][dele]
    del check [4][dele]
    return(check,total_asientos)
def edit(run_li,asiento_li,compra):
    run=input("Ingrese su rut")
    asiento=input("ingrese su asiento")
    while True:
        if (run in run_li) and (asiento in asiento_li) and (asiento_li.index(asiento)==run_li.index(run)):
            print ("correcto")
            break
        else:
            run=input("Ingrese un rut correcto")
            asiento=input("ingrese un correcto asiento")

    accion=input("Que accion decea realizar\n 1)editar nombre\n 2)editar numero")
    while True:
        if accion=="1" or accion=="2":
            break
        else:
            accion=input("indique una accion correcta\n 1)editar nombre\n 2)editar numero")
    if accion=="1":
        nombre=input("cual es el nuevo nombre que decea colocar")
        while len(nombre)<3:
                nombre=input("ingrese un nombre correcto")
        compra[0][asiento_li.index(asiento)]=nombre
    if accion=="2":
        telefono=input("cual es el nuevo telefono")
        while True:
            if len(telefono)==8:
                break
            else:
                telefono=input("ingrese un telefono correcto")
        compra[2][asiento_li.index(asiento)]=telefono
    return(compra)
###########################################################################################
###########################################################################################
a,b=arrays()
a[0][5]="x"
###########################################################################################
while True:
    print(compra)
    d=menu()
    if d==1:
        c=disponibles_num(a,b)
        input("ENTER..................")
    if d==2:
        a,compra=compra_fun(a,b,compra)
        print(compra)
    if d==3:
        compra,a=anulacion(boleto,compra,a,b)
        pass
    if d==4:
        compra=edit(rut,boleto,compra)
        pass
    if d==5:
        break
input("gracias por comprar en duoc uc")
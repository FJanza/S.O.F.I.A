# pip install wikipedia

#---------------------------LIBRERIAS----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import wikipedia as wiki

#---------------------------BUSCAR-INFORMACION------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#cambiar metodo de busqueda por nivel de importancia


def Buscar_info(lista_entrada) -> str :

    entrada = " ".join(lista_entrada)                                                                      #convierto la lista de entrada en un str

    query = entrada

    informacion = wiki.set_lang("Es")                                                       

    informacion = wiki.summary(query)                                                                      #busco la informacion requerida

                                                                                                           #REDUZCO-LA-INFORMACION
    
    punto = '.'                                                                                            # seteo el char que busco

    lst = []

    for pos,char in enumerate(informacion):

        if(char == punto):                                                                                 # cada vez que encuentre ese char, guardo su posicion 

            lst.append(pos)                                                                                # guardo la posicion 

            if(len(lst) == 2):                                                                             # una vez que guarde dos posiciones dejar de guardar info
                break



    informacion_lst = list(informacion)                                                                     # convierto la informacion en una lista

    for x in range(lst[1],len(informacion_lst)-1):                                                          #recorro la lista apartir del ultimo caracter que quiero
        informacion_lst.pop(lst[1] + 1)                                                                     #elimino los caracteres que no me importan

    informacion = "".join(informacion_lst)                                                                  #con la lista de caracteres nueva armo un str de la informacion importante


    return(informacion)
        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

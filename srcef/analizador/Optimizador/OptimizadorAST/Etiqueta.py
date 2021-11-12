from Optimizador.OptimizadorAST.Instruccion import Instruccion
from Optimizador.OptimizadorAST.GoTo import GoTo
from Optimizador.OptimizadorCondicionales.If import If
from Optimizador.OptimizadorValorImplicito.Asignacion import Asignacion
from Optimizador.OptimizadorReporteria.Optimizacion import Optimizacion 
import Optimizador.OptimizadorReporteria.ReporteOptimizacion as ReporteOptimizacion

class Etiqueta(Instruccion):
    def __init__(self,  id, instrucciones, linea, columna):
        self.id = id
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna
        self.codigoOptimizado = ""
        self.imprimirEtiqueta = True

    def aplicarRegla24(self,ast,instrucciones,codigoAnterior):
        asignacionPrevia = None
        contador = 0
        codigoGenerado = ""
        
        bandera = False
        
        for ins in instrucciones:
            if(isinstance(ins,Asignacion)):
                ins.instruccionPrevia = asignacionPrevia
                asignacionPrevia = ins
                optimizado =  optimizado = ins.optmimizarCodigo().codigo
                if(optimizado!=""):
                    codigoGenerado += "    "+optimizado
            else:
                
                if(codigoGenerado!=""):
                    bandera = True
                codigoGenerado +="\n"+self.id+":\n"
                for i in instrucciones[contador:]:
                    if(isinstance(i,Asignacion)):
                        ins.instruccionPrevia = asignacionPrevia
                        asignacionPrevia = ins
                    elif(isinstance(i,GoTo)):
                        optimizado = "goto "+i.id+";\n"

                    optimizado = i.optmimizarCodigo().codigo
                    if(optimizado!=""):
                        codigoGenerado += "    "+optimizado
                    
                break

            contador = contador + 1
        
        if(bandera):
            optimizacion = Optimizacion() #si hay optimización
            optimizacion.linea = str(self.linea)
            codigoOptimizar="<div>"+codigoAnterior+"</div>"
            optimizacion.antes = codigoOptimizar
            optimizacion.regla = "Regla 24"
            optimizacion.tipo = "Bloques - Redundancia Parcial Código Invariante"
            optimizacion.despues = "<div>"+codigoGenerado+"</div>"
            ReporteOptimizacion.func(optimizacion)

        return codigoGenerado

    def traducirCodigo(self,ast,instrucciones,aplicaBloque):
                contador = 0
                codigoOptimizado = ""
                instruccionAnterior = None
                asignacionPrevia = None
                codigoAnterior = ""
                banderaIf = False

                for ins in instrucciones:
                    # try:
                        if(isinstance(ins,Asignacion)):
                            ins.instruccionPrevia = asignacionPrevia
                            asignacionPrevia = ins
                        elif(isinstance(ins,GoTo)):
                            ins.ast = ast
                            if(ins.id == self.id and not banderaIf): #validacion regla 24
                                self.codigoOptimizado = ""
                                codigoOptimizado = self.aplicarRegla24(ast,instrucciones,codigoOptimizado)
                                contador = contador +1
                                codigoAnterior = ""
                                instruccionAnterior = ins
                                break

                        elif(isinstance(ins,If)):
                            ins.instrucciones = instrucciones[contador+1:]
                            banderaIf = True

                        optimizado = ""
                        if(isinstance(ins,If)): 
                            optimizado = ins.optmimizarCodigo(ast).codigo
                            if(len(ReporteOptimizacion.func(None))>0):
                                if(ReporteOptimizacion.func(None)[-1].regla=="Regla 19"):
                                    if(len(instrucciones[contador+1:]) == 0): continue  #si no existen mas instrucciones no hay optimización
                                    optimizacion = Optimizacion() #si hay optimización
                                    optimizacion.linea = str(ins.linea)
                                    codigoOptimizar="<div>"
                                    for i in instrucciones[contador+1:]:
                                        if(isinstance(i,GoTo)):
                                            i.ast = ast
                                        elif(isinstance(ins,If)):
                                            continue
                                        codigoOptimizar+="<p>"+i.optmimizarCodigo().codigo+"</p>"
                                    codigoOptimizar+="</div>"
                                    optimizacion.antes = codigoOptimizar
                                    optimizacion.despues = ""
                                    optimizacion.regla = "Regla 20"
                                    optimizacion.tipo = "Bloques - Eliminación de Código Muerto"
                                    ReporteOptimizacion.func(optimizacion)
                                    codigoAnterior = ''
                                    break    
                        else:
                            optimizado = ins.optmimizarCodigo().codigo
                        #Regla 2 Mirilla
                        if(isinstance(ins,GoTo)):
                            if(codigoAnterior.startswith('goto')):
                                if(isinstance(instruccionAnterior,If)):
                                    codigoAnterior = ""
                                    continue
                                else:
                                    optimizacion = Optimizacion() #si hay optimización
                                    optimizacion.linea = str(ins.linea)
                                    optimizacion.antes = codigoOptimizar
                                    optimizacion.despues = ""
                                    optimizacion.regla = "Regla 20"
                                    optimizacion.tipo = "Bloques - Eliminación de Código Muerto"
                                    ReporteOptimizacion.func(optimizacion)
                                    codigoAnterior = ''
                            elif(ast.existeEtiqueta(ins.id)):
                                if(optimizado!=""):
                                    codigoOptimizado += "    "+optimizado
                                    codigoAnterior = optimizado
                                if(len(instrucciones[contador+1:]) == 0): continue  #si no existen mas instrucciones no hay optimización
                                optimizacion = Optimizacion() #si hay optimización
                                optimizacion.linea = str(ins.linea)
                                codigoOptimizar="<div>"
                                for i in instrucciones[contador+1:]:
                                    if(isinstance(i,GoTo)):
                                        i.ast = ast
                                    elif(isinstance(ins,If)):
                                        continue
                                    codigoOptimizar+="<p>"+i.optmimizarCodigo().codigo+"</p>"
                                codigoOptimizar+="</div>"
                                optimizacion.antes = codigoOptimizar
                                optimizacion.despues = ins.id+":"
                                optimizacion.regla = "Regla 2"
                                optimizacion.tipo = "Mirilla - Eliminación de Código Inalcanzable"
                                ReporteOptimizacion.func(optimizacion)
                                codigoAnterior = ''
                                break
                            else:
                                if(optimizado!=""):
                                    codigoOptimizado += "    "+optimizado
                                    codigoAnterior = optimizado
                        else:
                            if(optimizado!=""):
                                codigoOptimizado += "    "+optimizado
                                codigoAnterior = optimizado

                        instruccionAnterior = ins
                        contador = contador + 1
                    # except:
                    #    pass
                return codigoOptimizado


    def optmimizarCodigo(self,ast,aplicaBloque=False):
        self.codigoOptimizado = ""
        if(self.imprimirEtiqueta):
            self.codigoOptimizado += self.id+":\n"
        strResultado = self.traducirCodigo(ast,self.instrucciones,aplicaBloque)
        self.codigoOptimizado +=strResultado
        return self.codigoOptimizado

    def generarAugus(self):
        pass
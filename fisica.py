import math

#def main, separando as variáveis e dados:
def main():
    #v0 = m/s; Tempo = s; AnguloInicial = em graus; AltInicial = m. 
    #Inputs para aparecerem no console:
    v0 = float(input("Velocidade inicial: "))
    Tempo = float(input("Tempo: "))
    AnguloInicial = float(input("Angulo inicial: "))
    AltInicial = float(input("Altura inicial: "))
    #Cálculo em radianos:
    AnguloInicial = math.radians(AnguloInicial)
    #Valor gravidade (m/s²):
    g = 9.8
    #Velocidade inicial de x e y:
    v0x = vox(v0, AnguloInicial)
    v0y = voy(v0, AnguloInicial)
    #Prints velocidades:
    print("v0x = %.2f" % v0x)
    print("v0y = %.2f" % v0y)


    #Exercícios:

    #Ex 1:
    #Dados do exercício 1:
    #v0 = 35.8 m/s;
    #AnguloInicial = 35.1º;
    #Altura = 14 cm do solo.
    
    #Posição da bola de beisebol pelo tempo input:
    xd = posicaoX(v0x, Tempo)
    yd = posicaoY(v0y, AltInicial, g, Tempo)
    print("xd = %.2f" % xd)
    print("yd = %.2f" % yd)
    
    #Tempo que a bola de beisebol está no ar:
    t = tempoTotal(v0, AnguloInicial, g)
    print("tar = %.2f" % t)

    #Velocidade da bola de beisebol pelo tempo input:
    print("vx = %.2f" % v0x)
    print("vy = %.2f" % vy(v0,Tempo, AnguloInicial, g))
    print("v = %.2f" % velModulo(v0x, vy(v0,Tempo, AnguloInicial, g)))

    #Quando a bola de beisebol está em altura máxima:
    print("vxAlturaMax = %.2f" % vxalturaMaxima(v0, AnguloInicial))
    print("vyAlturaMax = %.2f" % vyalturaMaxima(v0, AnguloInicial, g, t))
    print("vAlturaMax = %.2f" % valturaMaxima(vxalturaMaxima(v0, AnguloInicial), vyalturaMaxima(v0, AnguloInicial, g, t)))

    #Cálculo altura máxima:
    print("Altura Máxima = %.5f" % alturaMaxima(v0, AnguloInicial, g))
    
    #Cálculo alcance máximo:
    print("Alcance Máximo = %.2f" % alcanceMaximo(v0x, t))

    #Velocidade antes da bola de beisebol encostar no chão:
    print("vxToque = %.2f" % vxToque(v0, AnguloInicial))
    print("vyToque = %.2f" % vyToque(v0, AnguloInicial, g, t))
    print("vToque = %.2f" % velModuloToque(vxToque(v0, AnguloInicial), vyToque(v0, AnguloInicial, g, t)))
    

    

#Exercício 2 grilos Chirpy e Milada:
#Fazer velocidadeInicial * 
def exercicio2(t, velocidadeInicial):
    x = velocidadeInicial*t
    return x

    #Dados da 2:
    #Tempo = 2.5s
    #velocidadeInicial = 80.1 cm/s
    #print("x griloMilada = %.3f" % exercicio2(t,velocidadeInicial))


#Exercício 3:
#Dados do exercício 3:
#Velocidade inicial (v0) = 55km/h;
#Ângulo inicial = 26.3º;
#Altura = 95cm do solo.

#Componente do eixo x da velocidade inicial da bola:
def vox(vo, theta):
    v0x = vo*(math.cos(theta))
    return v0x

#Componente do eixo y da velocidade inicial da bola:
def voy(vo, theta):
    v0y = vo*(math.sin(theta))
    return v0y

#Posição da bola de beisebol tempo input eixo x:
def posicaoX(v0x, Tempo):
    x = (v0x*Tempo)
    return x
    
#Posição da bola de beisebol tempo input eixo y:
def posicaoY(v0y, AltInicial, g, Tempo):
    y = AltInicial + (v0y*Tempo) - (g*(math.pow(Tempo, 2)))/2
    return y

#Tempo da bola de beisebol enquanto está no ar:
def totalTempo(v0, theta, g):
    t = 2*(v0*(math.sin(theta)))/g
    return t

#Velocidade eixo y da bola de beisebol tempo input:
def vy(v0,Tempo, theta, g):
    vy = v0*math.sin(theta) - g*Tempo
    return vy

#Módulo velocidade bola beisebol:
def velModulo(vx,vy):
    v = math.sqrt(math.pow(vx,2) + math.pow(vy,2))
    return v

#Módulo de velocidade antes da bola de beisebol tocar no chão:
def velModuloToque(vx,vy):
    v = math.sqrt(math.pow(vx,2) + math.pow(vy,2))
    return v

#Altura máxima da bola de beisebol:
def alturaMaxima(v0, theta, g):
    alturaMaxima = ((1/2)*(pow(v0,2)*pow(math.sin(theta),2)))/g
    return alturaMaxima

#Momento em que a bola está em altura máxima (velocidade eixos x e y):
def vxalturaMaxima(v0, theta):
    vx = v0*math.cos(theta)
    return vx
def vyalturaMaxima(v0, theta, g, tar):
    vy = v0*math.sin(theta) - g*(tar/2)
    return vy
def valturaMaxima(vx, vy):
    v = math.sqrt(math.pow(vx,2) + math.pow(vy,2))
    return v

#Alcance máximo da bola de beisebol:
def alcanceMaximo(v0x, tar):
    alcanceMaximo = v0x*tar
    return alcanceMaximo

#Bola de beisebol ao tocar no chão eixo x:
def vxToque(v0, theta):
    vxToque = v0*math.cos(theta)
    return vxToque

#Bola de beisebol ao tocar no chão eixo y:
def vyToque(v0, theta, g, tar):
    vyToque = v0*math.sin(theta) - g*tar
    return vyToque

main()

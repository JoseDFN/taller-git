# def cal(a=0,b=0,oper=str):
#     match (oper):
#         case '+':
#             suma=a+b
#             print(f'La suma de {a} y {b} es {suma}')
#         case '-':
#             resta=a-b
#             print (f'La resta de {a} y {b} es {resta}')
#         case '*':
#             multi=a*b
#             print(f'La multiplicacion de {a} y {b} es {multi}')
#         case '/':
#             divi=a/b
#             print (f'La division de {a} y {b} es {divi}')
#         case _:
#             print('Informacion no valida')
        
# i=bool(input('Desea entrar a la calculadora? SI(S) NO(ENTER)'))
# while (i==True):
#     oper=str(input('Ingrese la operacion que desea realizat +, -, *, / '))
#     a=int(input('Ingrese eñ primer numero: '))
#     b=int(input('Ingrese otro valor: '))
#     cal(a,b,oper)
#     i=(bool(input('Desea hacer otra operacion: SI(S) NO(ENTER)')))
    
# def diasS(a:int):
#         match a:
#             case 1:
#                 print(f'El dia {a} es Lunes')
#             case 2:
#                 print (f'El di {a} es Martes')
#             case 3:
#                 print (f'El dia {a} es Miercoles')
#             case 4:
#                 print(f'El dia {a} es Jueves')
#             case 5:
#                 print(f'El dia {a} es Viernes')
#             case 6:
#                 print(f'El dia {a} es Sabado')
#             case 7:
#                 print(f'El dia {a} es Domingo')
#             case _:
#                 print('Intente de nuevo')
# i=bool(input('Desea conocer el dia de la semana SI(S) NO(ENTER)'))
# while (i==True):
#     a=int(input('Ingrese el numero de la semana: '))
#     diasS(a)
#     i=(bool(input('Desea continuar: SI(S) NO(ENTER)')))

#Escribe un programa que determine si un número es positivo, negativo o cero usando if .

# n=int(input('Ingrese un numeo: '))

# if (n==0):
#     print(f'El numero {n} es 0')
# elif (n<0):
#     print(f'El numero {n} es negativo')
# elif (n>0):
#     print(f'El numero {n} es positivo')

#Solicita la edad de la persona e indica si es niño (0-12 años), adolescente (13-17 años), adulto (18-64 años) o anciano (65 años o más).

# def edad(a=int):
#      if (a>=0) and (a<=12):
#         print('Es niño')
#      elif (a>=13) and (a<=17):
#         print('Es adolescente')
#      elif (a>=18) and (a<=64):
#         print('Es adulto')
#      elif (a>=65):
#         print('Es anciano')

# i=bool(input('Desea entrar a categoria de edad SI(S) NO(ENTER): '))
# while (i==True):

#     a=int(input('Ingrese su edad: '))
#     edad(a)

#     i=bool(input('Desea ingresar otra edad SI(S) NO(ENTER): '))

#El programa genera un número aleatorio entre 1 y 10. El usuario debe adivinar el número, y el programa indica si el número ingresado es mayor, menor o igual al número generado.
# import random
# numsec= random.randint(1,10)

# def num(n=0):
#     if (n<numsec):
#         print('El numero ingresado es menor')
#     elif (n>numsec):
#         print(f'El numero ingresado es mayor')
#     else:
#         print('El numero es correcto')

# i=bool(input('Deseas entrar a un juego de adivinanzas? SI(S) NO(ENTER): '))
# while (i==True):
#     n=int(input('Adivina el numero: '))
#     num(n)
#     i=bool(input('Deseas seguir jugando? SI(S) NO(ENTER): '))

#XD

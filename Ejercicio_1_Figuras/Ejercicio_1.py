'''
Tarea:

Crea un script con las clase triangulo, cuadrado y circulo que herede de una clase llamada figura que solicite
dependiendo de la figura los campos para calcular el area y el perimetro y me lo imprima en consola, 
debe de darle la opción al usuario de seleccionar la figura que va a crear 



Código Creado por: Robinson Stiven Inagan Ochoa
Version de Python = 3.11.2
'''
Pi=3.14159 # Variable Global para calculos referentes a el ciruclo.

class Figure(): #Clase Principal de donde van a heredar las demás figuras.

    def __init__(self,sides): #Inicialización de Variables mediante el método __init__.
        self.numSides = sides

    def CalculatePerimeter(): #Método para calcular el perimetro, el cual cambia según la figura.
        pass

    def CalculateArea(): #Método para calcular el área, el cual cambia según la figura.
        pass

class Triangle(Figure):

    def __init__(self): #Método para inicializar las variables de la Clase Triangle
        super().__init__(3) # Llamamos al método init de la clase de la cuál estamos heredando para decirle que tiene 3 lados.
        self.base=int(input('Ingrese el valor de la base \n ----> Base = ')) # Se solicita el valor de cada lado
        self.height=int(input('Ingrese el valor de la altura \n ----> Altura = '))
        self.side3=int(input('Ingrese el valor del lado faltante \n ----> L = '))
        if(self.base<0 or self.height<0 or self.side3<0):
            print('\nError, ningún lado puede ser menor que 0.')
            self.base='error'
    
    def CalculatePerimeter(self):
        return self.base+self.height+self.side3 #Se devuelve el valor del perimetro sumando cada uno de sus lados
    def CalculateArea(self):
        return (self.base*self.height)/2 #Se devuelve el valor de el área de un triungalo usando la formula A=b*h/2    
    '''
    def CalculateArea(self):
        s = (self.base+self.height+self.side3)/2 
        return math.sqrt((s)*(s-self.base)*(s-self.height)*(self.side3))
        #Se devuelve el valor de el área de un triungalo usando la formula de herón
    '''
class Circle(Figure):

    def __init__(self):#Método para inicializar las variables de la Clase Circle
        super().__init__(0) # Llamamos al método init de la clase de la cuál estamos heredando para decirle que tiene 0 lados.
        self.radio=int(input('Ingrese el valor del radio \n ----> r = '))# Se solicita el valor del radio
        if(self.radio<0 ):
            print('\nError, el radio no puede ser menor que 0.')
            self.radio="error"        

    def CalculatePerimeter(self):
        return 2*Pi*self.radio #Se devuelve el valor del perimetro mediante: P = 2 π R
    
    def CalculateArea(self):
        return Pi*self.radio*self.radio#Se devuelve el valor del área mediante: A = π r²

class Square(Figure):
    
    def __init__(self,):#Método para inicializar las variables de la Clase Square
        super().__init__(4)
        self.sides=int(input('Ingrese el valor de los lados \n ----> L = '))# Se solicita el valor del los lados
        if(self.sides<0 ):
            print('\nError, el valor de los lados no pueden ser menores que 0.')
            self.sides="error"

    def CalculatePerimeter(self):
        return self.sides*4 # Se retorna el valor del permietro usando P = L+L+L+L, que es lo mismo que P = 4*L
    
    def CalculateArea(self):
        return self.sides*self.sides # Se retorna el valor del área usando P = L*L
    
def __main__(): # Método principal de ejecución del programa
    opt=0 # Opción para manejar el menú

    while(opt!=4): # Ciclo que mantiene el programa activo hasta que el usuario presione la opción 4
        print('\n\n\n\n\n\n\n\n\n\n\n\n\nSeleccione una figura en la que desee calcular área y perimetro.\n')
        print('1. Triangulo')
        print('2. Circulo')
        print('3. Cuadrado')
        print('4. Salir\n')
        try: # Manejo de la excepción cuando el usuario pulsa enter sin haber escrito nada.
            opt=int(input('-----> '))
        except ValueError:
            input('Error. Ingrese una opción correcta, presione ENTER para continuar ....')
            opt=0

        if(opt==1):
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n-----------Triangulo--------------\n')
            Figure1=Triangle()
            if Figure1.base=='error':
                input('\n\nPresione ENTER para continuar...')
            else:
                print('\n\nEl valor del perimetro para el triangulo ingresado es: ',Figure1.CalculatePerimeter())
                print('El valor del área para el triangulo ingresado es: ',Figure1.CalculateArea())
                input('\n\nPresione ENTER para continuar...')
        elif(opt==2):
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n-----------Circulo--------------\n')
            Figure1=Circle()
            if Figure1.radio=='error':
                input('\n\nPresione ENTER para continuar...')
            else:
                print('\n\nEl valor del perimetro para el circulo ingresado es: ',Figure1.CalculatePerimeter())
                print('El valor del área para el circulo ingresado es: ',Figure1.CalculateArea())
                input('\n\nPresione ENTER para continuar...')
        elif(opt==3):
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n-----------Cuadrado--------------\n')
            Figure1=Square()
            if Figure1.sides=='error':
                input('\n\nPresione ENTER para continuar...')
            else:            
                print('\n\nEl valor del perimetro para el cuadrado ingresado es: ',Figure1.CalculatePerimeter())
                print('El valor del área para el cuadrado ingresado es: ',Figure1.CalculateArea())
                input('\n\nPresione ENTER para continuar...')
        elif(opt<0 or opt>4): # Manejo de error cuando el usuario selecciona una opción que no hay en el menu
            input('Error. Ingrese una opción correcta, presione ENTER para continuar ....')
            opt=0
            
__main__()
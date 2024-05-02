
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import serial, time
def set_print_x(row, column, color):
    # Aquí iría la lógica para imprimir la forma x en las coordenadas dadas con el color especificado
    print(f"Imprimir x en fila {row}, columna {column}, con color {color}")

    # Función para ejecutar la instrucción set_print_o
def set_print_o(row, column, color):
    # Aquí iría la lógica para imprimir la forma o en las coordenadas dadas con el color especificado
    print(f"Imprimir o en fila {row}, columna {column}, con color {color}")


def set_print_triangulo(row, column, color):
    # Aquí iría la lógica para imprimir la forma o en las coordenadas dadas con el color especificado
    print(f"Imprimir triangulo en fila {row}, columna {column}, con color {color}")


def set_print_estrella(row, column, color):
    # Aquí iría la lógica para imprimir la forma o en las coordenadas dadas con el color especificado
    print(f"Imprimir estrella en fila {row}, columna {column}, con color {color}")

def get_data(name):

    array = [['-' for _ in range(3)] for _ in range(3)]

    with open(name, 'r') as archivo:
        for line in archivo:
            if not line.strip().startswith('#'):
                instruction = line.replace(')', '')
                instruction = instruction.replace(';', '')
                instruction = instruction.replace('\n', '')
                instruction = instruction.replace('\'', '')
                instruction = instruction.split('(')
                if instruction[0].lower() == 'set_print_x':
                    data = instruction[1].split(',')
                    if len(data) == 3:
                        row = int(data[0])
                        column = int(data[1])
                        color = data[2].strip().lower()


                        if 1<= row <= 3 and 1<= column <= 3 and color in ['cyan', 'negro', 'magenta', 'amarillo']:
                            if array[row-1][column-1] == '-':

                                set_print_x(row, column, color)
                                array[row-1][column-1] = ['x',color,1]
                            else:
                                print('posicion ya ocupada',data[0], data[1])
                                break
                        else:
                            print('Informacion incorrecta, por favor corregir los datos')
                            print(data[0], data[1], data[2])
                            break

                elif instruction[0].lower() == 'set_print_o':
                    data = instruction[1].split(',')
                    if len(data) == 3:
                        row = int(data[0])
                        column = int(data[1])
                        color = data[2].strip().lower()
                        if 1 <= row <= 3 and 1 <= column <= 3 and color in ['cyan', 'negro', 'magenta', 'amarillo']:
                            if array[row - 1][column - 1] == '-':
                                array[row-1][column-1] = ['o',color,1]
                                set_print_o(row, column, color)
                            else:
                                print('posicion ya ocupada',data[0], data[1])
                                break
                        else:
                            print('Informacion incorrecta, por favor corregir los datos')
                            print(data[0], data[1], data[2])
                            break

                elif instruction[0].lower() == 'set_print_triangulo':
                    data = instruction[1].split(',')
                    if len(data) == 3:
                        row = int(data[0])
                        column = int(data[1])
                        color = data[2].strip().lower()
                        if 1 <= row <= 3 and 1 <= column <= 3 and color in ['cyan', 'negro', 'magenta', 'amarillo']:
                            if array[row - 1][column - 1] == '-':
                                array[row-1][column-1] = ['triangulo',color,1]
                                set_print_triangulo(row, column, color)
                            else:
                                print('posicion ya ocupada',data[0], data[1])
                                break
                        else:
                            print('Informacion incorrecta, por favor corregir los datos')
                            print(data[0], data[1], data[2])
                            break

                elif instruction[0].lower() == 'set_print_estrella':
                    data = instruction[1].split(',')
                    if len(data) == 3:
                        row = int(data[0])
                        column = int(data[1])
                        color = data[2].strip().lower()
                        if 1 <= row <= 3 and 1 <= column <= 3 and color in ['cyan', 'negro', 'magenta', 'amarillo']:
                            if array[row - 1][column - 1] == '-':
                                array[row-1][column-1] = ['estrella',color,1]
                                set_print_estrella(row, column, color)
                            else:
                                print('posicion ya ocupada',data[0], data[1])
                                break
                        else:
                            print('Informacion incorrecta, por favor corregir los datos')
                            print(data[0], data[1], data[2])
                            break

    for i in range(len(array)):
        for j in range(len(array)):

            if array[i][j] == '-':
                array[i][j] = ['0','0','0']

    print(array)
    return array


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_data('archivo de prueba.orga')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


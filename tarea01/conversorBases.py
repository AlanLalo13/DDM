# Función para convertir un número de base m a base n
def convertir_base(numero, base_origen, base_destino):
  # Si el número tiene un punto decimal, se separa en dos partes
  if "." in numero:
    parte_entera, parte_decimal = numero.split(".")
  else:
    parte_entera = numero
    parte_decimal = ""

  # Se convierte la parte entera a base 10
  decimal_entero = int(parte_entera, base_origen)

  # Se convierte la parte decimal a base 10
  decimal_decimal = 0
  for i, digito in enumerate(parte_decimal):
    decimal_decimal += int(digito, base_origen) * (base_origen ** -(i + 1))

  # Se convierte la parte entera de base 10 a base destino
  resultado_entero = ""
  while decimal_entero > 0:
    residuo = decimal_entero % base_destino
    resultado_entero = format(residuo, "X") + resultado_entero
    decimal_entero //= base_destino

  # Se convierte la parte decimal de base 10 a base destino
  resultado_decimal = ""
  while decimal_decimal > 0 and len(resultado_decimal) < 10:
    producto = decimal_decimal * base_destino
    parte_entera = int(producto)
    resultado_decimal += format(parte_entera, "X")
    decimal_decimal = producto - parte_entera

  # Se une la parte entera y la parte decimal con un punto
  if resultado_decimal:
    resultado = resultado_entero + "." + resultado_decimal
  else:
    resultado = resultado_entero

  return resultado

# Función para validar si una cadena representa un número de una base
def validar_numero(cadena, base):
  # Se convierte la cadena a mayúsculas
  cadena = cadena.upper()
  # Se verifica si la cadena es alfanumérica o contiene un punto
  if cadena.isalnum() or "." in cadena:
    # Se verifica si la cadena tiene un solo punto
    if cadena.count(".") <= 1:
      # Se verifica si la base es menor o igual que 10
      if base <= 10:
        # Se verifica si la cadena solo contiene dígitos menores que la base o un punto
        for caracter in cadena:
          if caracter.isdigit():
            if int(caracter) >= base:
              return False
          elif caracter != ".":
            return False
        return True
      # Se verifica si la base es mayor que 10 y menor o igual que 36
      elif base <= 36:
        # Se verifica si la cadena solo contiene dígitos y/o letras menores que la base o un punto
        for caracter in cadena:
          if caracter.isdecimal():
            if int(caracter) >= base:
              return False
          elif caracter.isalpha():
            if ord(caracter) - ord('A') + 10 >= base:
              return False
          elif caracter != ".":
            return False
        return True
      # Se devuelve False si la base es mayor que 36
      else:
        return False
    # Se devuelve False si la cadena tiene más de un punto
    else:
      return False
  # Se devuelve False si la cadena no es alfanumérica ni contiene un punto
  else:
    return False


# Se pide al usuario un número y sus bases
numero = input("Ingrese el número: ")
base_origen = int(input("Ingrese la base de origen: "))
base_destino = int(input("Ingrese la base de destino: "))

# Se valida que el número sea válido para la base de origen
if validar_numero(numero, base_origen):
  # Se llama a la función para convertir el número
  resultado = convertir_base(numero, base_origen, base_destino)
  # Se muestra el resultado
  print(f"El número {numero} en base {base_origen} es {resultado} en base {base_destino}")
else:
  # Se muestra un mensaje de error
  print("El número que ingresó no es válido para la base de origen")

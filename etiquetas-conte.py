
import pandas as pd
from colorama import Fore, Style

def printWelcome():
  print(Fore.GREEN  + """
  __________.__                                 .__    .___       
  \______   \__| ____   _______  __ ____   ____ |__| __| _/____   
  |    |  _/  |/ __ \ /    \  \/ // __ \ /    \|  |/ __ |/  _ \  
  |    |   \  \  ___/|   |  \   /\  ___/|   |  \  / /_/ (  <_> ) 
  |______  /__|\___  >___|  /\_/  \___  >___|  /__\____ |\____/  
          \/        \/     \/          \/     \/        \/        
  """)
  print("                                      Por: Gilberto JV Skirlo\n\n\n")


def readInfo():
  flag = 'y'
  numbers = []
  containers = []
  models = []
  colors = []
  ftcs = []
  result = []

  counter = int(input('Inicializar contador en: '))-1
  container = input('Ingrese el contenedor: ')

  while flag == 'y' or flag == 'Y':
    ftc = input('Ingrese el fabricante: ')
    model = input('Ingrese el modelo abreviado: ')
    color = input('Ingrese el color abreviado: ')

    if len(f'{"%04d" % (counter,)}|{container}|{model}|{color}') >= 50:
      print(Fore.RED  + "---> ¡El codigo a generar supera los 50 caracteres! <---")
      print(Fore.RED + "FAVOR DE REINGRESAR VALORES." + Fore.GREEN)
    else:
      qty = int(input('Numero de etiquetas: '))
      for i in range(qty):
        counter += 1
        numbers.append(f'{"%04d" % (counter,)}')
        containers.append(container)
        models.append(model)
        colors.append(color)
        ftcs.append(ftc)
        result.append(f'{"%04d" % (counter,)}|{container}|{ftc}|{model}|{color}')
      
      flag = input("Continuar? [y] -> si:  ")
    
  MakeCsv(numbers,containers,ftcs,models,colors,result)

def MakeCsv(numbers,containers,ftcs,models,colors,result):
  my_dict = {
    'NUMEROS':numbers, 
    'CONTENEDOR':containers,    
    'MODEL':models,
    'COLOR':colors,
    'Formula':result,
    'FTC':ftcs
    }

  my_df_news = pd.DataFrame(my_dict)

  my_df_news.to_csv(f'CONTES-NUEVA.csv')

def main():
  printWelcome()
  readInfo()
  print(Style.RESET_ALL)

if __name__ == '__main__':
  main()
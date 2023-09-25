from process import crearArchivoFinal
import os


def main():
  dir = [f'./db chicas/{ar}' for ar in os.listdir('./db chicas')]
  for i in range(len(dir)):
    print(f"Realizando {i+21} {dir[i]}... chicas{i+21}")
    crearArchivoFinal(dir[i], f"chicas{i+21}")
    print(f"Fin {i+21} {dir[i]}...")
  print("Done!")
  
  

if __name__ == '__main__':
  main()
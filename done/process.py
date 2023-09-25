from converter.pgn_data import PGNData
import pandas as pd


def crearCSV(ar, out):
  pgn_data = PGNData(ar, out)
  a = pgn_data.export()
  del pgn_data, a
  return True


def transformar_linea(line):
  return line.replace("(", "").replace(")", "").replace("'", "").replace(" ", "")


def escribirPly(ar, out):
  pgn = open(ar, "r")
  csv_ply = open(out, "w")

  id = ""
  linea_ant = []

  while True:
      line = pgn.readline()
      
      if not line:
        linea_csv = f"{linea_ant[0],linea_ant[1],linea_ant[2]}\n"
        linea_csv = transformar_linea(linea_csv)
        csv_ply.write(linea_csv)
        break
      
      line = line.replace("\n", "").split(",")
      if id != line[0]:
        if linea_ant:
          linea_csv = f"{linea_ant[0],linea_ant[1],linea_ant[2]}\n"
          linea_csv = transformar_linea(linea_csv)
          csv_ply.write(linea_csv)
        id = line[0]
      
      linea_ant = line
      
  pgn.close()
  csv_ply.close()
  return True
  
  
def generarDF(game_info, ply_info, out):
  ply = pd.read_csv(ply_info)
  df = pd.read_csv(game_info)
  df_main = pd.merge(df, ply, on="game_id", how="outer")
  df_main.drop(['ply_count', 'file_name', 'date_created'], axis=1, inplace=True)
  df_main.rename(columns={'move_no': 'ply_count'}, inplace=True)
  df_main.to_csv(f"./res/{out}.csv", index=False)
  return True
  
  
def crearArchivoFinal(ar, out):
  inter = "./intermediate/"
  gm = "games_moves.csv"
  gi = "games_game_info.csv"
  ply = "ply.csv"
  crearCSV(ar, f"{inter}games")
  escribirPly(f"{inter}{gm}", f"{inter}{ply}")
  generarDF(f"{inter}{gi}", f"{inter}{ply}", out)
def tictac():
   return [
  [' ', ' ', ' '],
  [' ', ' ', ' '],
  [ ' ', ' ',' ']
 ] 

def i (test):
   for row in test:
     print("|".join(row))
     print("-----")
  
def add_symbole (tab,row,col,symbole):
   if 0 <= row <len(tab) and 0 <= col <len(tab[row]):
      tab[row][col]= symbole
   else:
      print("position invalide")
tab=tictac()
i(tab)


def check_win (player_pos,cur_player):
 solution = [[1,2,3],[4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
 for x in solution:
    if all (y in player_pos[cur_player] for y in x ):
       return True
 return False

def check_draw (player_pos):
   if len(player_pos["X"]) + len(player_pos["O"]) == 9:
      return True
   return False

def alternate_tour(current_player, current_sybol, name_1, name_2): 
    if current_player == name_1: 
      return name_2, "O" 
    else: 
        return name_1, "X"

def mouvement ():
   tab = tictac()
   name_1 = input("Entrer le nom du joueur 1:")
   name_2 = input("Entrer le nom du joueur 2: ")
   current_player = name_1
   current_symbol = "X"
   player_pos = {"X": [], "O": []} 
   while True:
      i(tab)
      print(f"C'est au tour de {current_player} ({current_symbol})")
      row = int(input(f"Ligne (0-2): "))
      col = int(input(f"Colonne (0-2): "))
      add_symbole(tab, row, col, current_symbol)
      player_pos[current_symbol].append(row * 3 + col)

      if check_win(player_pos, current_symbol):
                i(tab)
                print(f"{current_player} a gagné!")
                break
      if check_draw(player_pos):
                i(tab)
                print("Match nul!")
                break
      current_player, current_symbol = alternate_tour(current_player,current_symbol, name_1, name_2) 
   else:
    print("position invalide essaye encore")
mouvement()
      

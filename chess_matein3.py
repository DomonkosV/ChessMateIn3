pip install chess

import chess

def b_or_w(fen):  #fen-ből kinyerjük, hogy sötét vagy világossal vagyunk-e
  return(fen.split(" ",1)[1][0])

def ends(board):  #vége van-e a partinak
  outcome = board.outcome()
  if not outcome:
    return False
  else:
    return True

def result(board, bw):  #ki nyert
  outcome = board.outcome()
  a = 1
  if bw == "b": #ha sötéttel vagyunk, akkor fordítva van minden
    a = -1
  if ends(board):
    if outcome.winner == chess.WHITE:
      return a
    elif outcome.winner == chess.BLACK:
      return -a
    else: #döntetlen
      return 0
  return 100 #nincsen vége a meccsnek

def solver(board, x):
  solution = "" #aktuális legrövidebb matthoz vezető lépés

  move1 = list(board.legal_moves)  #1. lépések halmaza

  for m1 in move1:

    board1 = chess.Board(board.fen()) #betöltjuk a táblát
    board1.push(m1)

    if result(board1, x) == 1: #nyertünk akkor kész
      return m1

    elif result(board1, x) <= 0: #patt akkor tovább lépünk
      continue

    else:
      move2 = list(board1.legal_moves)  #2. lépések halmaza

      for m2 in move2:
        board2 = chess.Board(board1.fen())

        in2 = True  #feltesszük, hogy 2 lépésből mattot adunk
        pot_1 = True #m1 potenciálisan jó megoldás

        board2.push(m2)

        if result(board2, x) <= 0: #kikaptunk/patt új 1. lépés
          pot_1 = False #m1 nem lehet megoldás
          break

        else:
          move3 = list(board2.legal_moves)  #3. lépések halmaza

          for m3 in move3:  #megnézzük, hogy van-e m1-re 2lépéses matt
            board3 = chess.Board(board2.fen())
            board3.push(m3)

            if result(board3, x) <= 0: #patt, ehelyett a lépés helyett a következő
              continue

            elif result(board3, x) == 1: #nyertünk, ellenfél lépésén tovább iterálunk
              pot_1 = True
              break

          for m3 in move3:  #m1-re nincsen 2lépésből matt, ezért tovább nézzük, hogy 3-ból van-e
            board3 = chess.Board(board2.fen())
            board3.push(m3)

            if result(board3, x) <= 0: #patt, ehelyett a lépés helyett a következő
              continue

            elif result(board3, x) == 1: #nyertünk, ellenfél lépésén tovább iterálunk
              pot_1 = True
              break

            else:
              move4 = list(board3.legal_moves)  #4. lépések halmaza

              for m4 in move4:
                board4 = chess.Board(board3.fen())

                pot_1 = True
                pot_2 = False #feltesszük, hogy a 2.lépésünk nem vezet jó megoldáshoz

                board4.push(m4)

                if result(board4, x) <= 0: #kikaptunk/patt új 3. lépés
                  pot_1 = False
                  break

                else:
                  move5 = list(board4.legal_moves)  #5. lépések halmaza

                  for m5 in move5:

                    board5 = chess.Board(board4.fen())
                    board5.push(m5)

                    if result(board5, x) == 1: #nyertünk, ellenfél lépésén tovább iterálunk
                      pot_2 = True #aktuális m4-re (ellenfél lépése) van mattot adó lépésünk
                      in2 = False #legalább 3lépés kell, hogy m1-ből mattot adjuk
                      break

                  if not pot_2:  #nincs nyerő lépés egyik esetben (nincs potenciál), ezért move3 halmazon tovább iterálunk
                    pot_1 = False
                    break

              if pot_1: #aktuális m2-re mindig tudunk mattot adni
                break

          if not pot_1: #aktuális m1-re találtunk olyan lépéseket, amelyre nem tudunk mattotadni, move1-en tovább iterálunk
            break

      if pot_1: #aktuális m1 matthoz vezet
        solution = m1
        if in2: #aktuális m1 2lépéses matthoz vezet
          return m1

  if solution:
    return solution

  return print("There is no checkmate in 3 moves")

#ellenfél lépését bekérjük
def opp_move(board):
  moves = list(board.legal_moves)
  print("Possible moves: ")
  print(moves)
  ready = False
  while not ready:
    move = chess.Move.from_uci(input("Paste opponent's move: "))

    if move in moves:
      board.push(move)
      ready = True

    else:
      print("It is not a legal move!")

  return board

#összefogjuk a gép és játékos által adott lépéseket és vizualizáljuk
def start_solving():
  board = chess.Board()
  first = True
  while not board.outcome():
    if first:
      FEN = input("Paste FEN: ")
      board=chess.Board(FEN)
    else:
      board = opp_move(board)
      display(board)

    first = False

    move = solver(board, b_or_w(FEN))
    print(f"Our move: {move}")

    if move in board.legal_moves:
      board.push(move)
    else:
      break
    display(board)

start_solving()

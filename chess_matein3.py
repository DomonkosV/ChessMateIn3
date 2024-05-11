pip install chess

import chess

def b_or_w(fen):
  return(fen.split(" ",1)[1][0])

def ends(board):
  outcome = board.outcome()
  if not outcome:
    return False
  else:
    return True

def result(board, bw):
  outcome = board.outcome()
  a = 1
  if bw == "b":
    a = -1
  if ends(board):
    if outcome.winner == chess.WHITE:
      return a
    elif outcome.winner == chess.BLACK:
      return -a
    else:
      return 0
  return 100

def solver(board, x):
  solution = ""
  winning_moves=[]
  move1 = list(board.legal_moves)

  for m1 in move1:  #1. lépések halmaza

    board1 = chess.Board(board.fen())
    board1.push(m1)

    if result(board1, x) == 1: #nyertünk akkor kész
      return m1

    elif result(board1, x) <= 0: #patt akkor tovább lépünk
      continue

    else:
      move2 = list(board1.legal_moves)  #2. lépések halmaza

      for m2 in move2:
        board2 = chess.Board(board1.fen())

        in2 = True
        pot_3 = True

        board2.push(m2)

        if result(board2, x) <= 0: #kikaptunk/patt új 1. lépés
          pot_3 = False
          break

        else:
          move3 = list(board2.legal_moves)  #3. lépések halmaza

          for m3 in move3:
            board3 = chess.Board(board2.fen())
            board3.push(m3)

            if result(board3, x) <= 0: #patt, ehelyett a lépés helyett a következő
              continue

            elif result(board3, x) == 1: #nyertünk, ellenfél lépésén tovább iterálunk
              pot_3 = True
              break

          for m3 in move3:
            board3 = chess.Board(board2.fen())
            board3.push(m3)

            if result(board3, x) <= 0: #patt, ehelyett a lépés helyett a következő
              continue

            elif result(board3, x) == 1: #nyertünk, ellenfél lépésén tovább iterálunk
              pot_3 = True
              break

            else:
              move4 = list(board3.legal_moves)  #4. lépések halmaza

              for m4 in move4:
                board4 = chess.Board(board3.fen())

                pot_3 = True
                pot_5 = False

                board4.push(m4)

                if result(board4, x) <= 0: #kikaptunk/patt új 3. lépés
                  pot_3 = False
                  break

                else:
                  move5 = list(board4.legal_moves)  #5. lépések halmaza

                  for m5 in move5:
                    board5 = chess.Board(board4.fen())
                    board5.push(m5)

                    if result(board5, x) == 1: #nyertünk, ellenfél lépésén tovább iterálunk
                      pot_5 = True #van
                      in2 = False
                      break

                  if not pot_5:  #nincs nyerő lépés egyik esetben (nincs potenciál), ezért 3. lépésben tovább iterálunk
                    pot_3 = False
                    break

              if pot_3:
                break

          if not pot_3:
            break

      if pot_3:
        solution = m1
        if in2:
          return m1

  if solution:
    return solution

  return print("There is no checkmate in 3 moves")

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

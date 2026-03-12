import random, string
def initial_state():
  return random.randint(10,25)
def possible_new_state(state):
  return [state-take for take in (1,2,3) if state-take >= 0]

def evaluate(state,is_maximizing):
  if state == 0:
    return +1 if is_maximizing else -1
  return None
def minimax(state,is_maximizing):
  score = evaluate(state,is_maximizing)
  if score is not None:
    return score
  moves = [
    minimax(new_state,not is_maximizing)
    for new_state in possible_new_state(state)
  ]
  return max(moves) if is_maximizing else min(moves)
def best_move(state):
  return max(
    possible_new_state(state),
    key=lambda s: minimax(s, is_maximizing=True)
  )
def game_over(score):
  print("you win!" if score>0 else "you lose!")
def input_choice(choices,text='Choice:'):
  inputs=dict(zip(string.ascii_letters,choices))
  for letter,choice in inputs.items():
    print(f"{letter}) {choice}")
  while True:
    c=input(text)
    if c in inputs:
      return inputs[c]
    print(f"Select one of {', '.join(inputs)}")
    
def play_nim():
  state=initial_state()
  while True:
    print(f"Current state: {state}")
    state=input_choice(possible_new_state(state))
    score=evaluate(state,is_maximizing=False)
    if score is not None:
      return game_over(score)
    ai_move=best_move(state)
    print(f"I move from {state} to {ai_move}")
    state=ai_move
    score=evaluate(state,is_maximizing=True)
    if score is not None:
      return game_over(score)
play_nim()
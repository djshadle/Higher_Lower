# from random import randint
# from replit import clear
# from game_data import data
# from art import logo, vs

# def game_loop():
#   game_data = data
#   number_in_list = (len(game_data)-1)
#   should_run = True
#   score = 0

  def two_variables(game_data):
    """ Use game_data to select two random variables """
    random_position_one = randint(0, number_in_list)
    random_position_two = randint(0, number_in_list)
    while random_position_two == random_position_one:
      random_position_two = randint(0, number_in_list)
    first_choice = game_data[random_position_one]
    second_choice = game_data[random_position_two]
    return first_choice, second_choice

  def higher_lower(variable_one, variable_two, score):
    user_choice = input("---------\nWho has more followers? Type 'A' or 'B': ").lower()
    follower_count_a = variable_one['follower_count']
    follower_count_b = variable_two['follower_count']
    if follower_count_a > follower_count_b and user_choice == "a":
      modified_score = score + 1
      print(f"You're right! Current score: {modified_score}.")
      return True, modified_score
    elif follower_count_a < follower_count_b and user_choice == "b":
      modified_score = score + 1
      print(f"You're right! Current score: {modified_score}.")
      return True, modified_score
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      return False, score

  while should_run:
    clear()
    choices = two_variables(game_data)
    choice_one = choices[0]
    choice_two = choices[1]
    print(logo)
    print(f"Current score: {score}")
    print(f"Compare A: {choice_one['name']}, a {choice_one['description']}, from {choice_one['country']}.")
    print(vs)
    print(f"Against B: {choice_two['name']}, a {choice_two['description']}, from {choice_two['country']}.")
    game_check = higher_lower(choices[0], choices[1], score)
    should_run = game_check[0]
    score = game_check[1]

  if input("\nDo you want to play again? 'Y' or 'N': ").lower() == 'y':
    game_loop()
  else:
    print("Have a good day!")


game_loop()
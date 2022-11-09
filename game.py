import random

class game:
	def __init__(self, name, school, num_matches):
		print("Welcome to `Harry Potter: the Game`")
		print("Here are the rules: ....")
		self.school = school
		self.name = name
		self.no_of_matches = self.check_count_of_matches(num_matches)
		self.opponent = self.opponent_house_generator(self.school)
	
	def opponent_house_generator(self, school):
		# Generates the house of the opponent team
		list_of_houses = ["Griffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]
		# Removing the player's school from list of houses, to choose opponent
		list_of_houses.remove(school)
		house_of_opponent_team = random.choice(list_of_houses)
		print(f"YOUR OPPONENT IS: {house_of_opponent_team}")
		return house_of_opponent_team

	def check_count_of_matches(self, no_of_matches):
		# checks if number of matches entered are odd or not,
		# else, adds an extra match to make it odd.
		if no_of_matches%2 == 0:
			no_of_matches += 1
		print(f"Number of Matches : {no_of_matches} (Could have been changed as it must be an odd number)")
		return no_of_matches

	def play(self):
		#initialising score variables
		scores = {
			self.school : 0,
			self.opponent : 0
		}

		# initialising ball tracker
		ball_is_with = self.opponent

		for _ in range(self.no_of_matches):
			goal = False
			pass_counter = 0 # max value is 5
			while not goal:
				# initialising player jersey number bearer
				player_jersey_numbers = {
					self.opponent : random.randint(1,7),
					self.school : int(input("insert the predicted player number (between 1 and 7): "))
				}

				if pass_counter == 5:
					goal = True
					scores[ball_is_with] += 1
					print(f"Goal by {ball_is_with}!!!")
					print(f"""Current scores are:
					 {self.school + " : " + str(scores[self.school])}
					 {self.opponent + " : " + str(scores[self.opponent])}""")
				elif player_jersey_numbers[self.opponent] != player_jersey_numbers[self.school]:
					pass_counter += 1
					print(f"Pass by {ball_is_with} and current passes are {pass_counter}")
					print(f"Player chosen by {ball_is_with}: {player_jersey_numbers[ball_is_with]}")
				else:
					pass_counter = 0
					teams = [self.school, self.opponent]
					teams.remove(ball_is_with)
					ball_is_with = teams[0]
					print(f"Ball is caught by {ball_is_with}")

		if scores[self.school] > scores[self.opponent]:
			print(f"{self.school} wins over {self.opponent} by {scores[self.school] - scores[self.opponent]} points!!")
		else:
			print(f"{self.opponent} wins over {self.school} by {scores[self.opponent] - scores[self.school]} points!!")

		print("GAME OVER")


if __name__ == "__main__":
	name = input("please enter your name: ")
	school = input("please choose your school out of \"Griffindor\", \"Ravenclaw\", \"Hufflepuff\", \"Slytherin\": ")
	num_matches = int(input("please input number of matches (Odd Number): "))

	game(name, school, num_matches).play()


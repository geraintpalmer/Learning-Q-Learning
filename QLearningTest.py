# 9 states, 1 goal and 1 death

from random import random, seed


#######################################################################
#######################################################################
# ACTUAL INPUTS
# states:	[3, 6, 10, g]
#			[2, d, 9, 12]
#			[1, 5, 8, d]
#			[0, 4, 7, 11]
# transition probabilities given state and action
# s1an : state 1 action north

s0an = [1.0, 0.0]
s0ae = [0.0, 1.0]

s1an = [1.0, 0.0, 0.0]
s1ae = [0.0, 1.0, 0.0]
s1as = [0.0, 0.0, 1.0]

s2an = [1.0, 0.0, 0.0]
s2ae = [0.0, 1.0, 0.0]
s2as = [0.0, 0.0, 1.0]

s3ae = [1.0, 0.0]
s3as = [0.0, 1.0]

s4an = [1.0, 0.0, 0.0]
s4ae = [0.0, 1.0, 0.0]
s4aw = [0.0, 0.0, 1.0]

s5an = [1.0, 0.0, 0.0, 0.0]
s5ae = [0.0, 1.0, 0.0, 0.0]
s5as = [0.0, 0.0, 1.0, 0.0]
s5aw = [0.0, 0.0, 0.0, 1.0]

s6ae = [1.0, 0.0, 0.0]
s6as = [0.0, 1.0, 0.0]
s6aw = [0.0, 0.0, 1.0]

s7an = [1.0, 0.0, 0.0]
s7ae = [0.0, 1.0, 0.0]
s7aw = [0.0, 0.0, 1.0]

s8an = [1.0, 0.0, 0.0, 0.0]
s8ae = [0.0, 1.0, 0.0, 0.0]
s8as = [0.0, 0.0, 1.0, 0.0]
s8aw = [0.0, 0.0, 0.0, 1.0]

s9an = [1.0, 0.0, 0.0, 0.0]
s9ae = [0.0, 1.0, 0.0, 0.0]
s9as = [0.0, 0.0, 1.0, 0.0]
s9aw = [0.0, 0.0, 0.0, 1.0]

s10ae = [1.0, 0.0, 0.0]
s10as = [0.0, 1.0, 0.0]
s10aw = [0.0, 0.0, 1.0]

s11an = [1.0, 0.0]
s11aw = [0.0, 1.0]

s12an = [1.0, 0.0, 0.0]
s12as = [0.0, 1.0, 0.0]
s12aw = [0.0, 0.0, 1.0]

transition_probs = {0:[s0an, s0ae], 1:[s1an, s1ae, s1as], 2:[s2an, s2ae, s2as], 3:[s3ae, s3as], 4:[s4an, s4ae, s4aw], 5:[s5an, s5ae, s5as, s5aw], 6:[s6ae, s6as, s6aw], 7:[s7an, s7ae, s7aw], 8:[s8an, s8ae, s8as, s8aw], 9:[s9an, s9ae, s9as, s9aw], 10:[s10ae, s10as, s10aw], 11:[s11an, s11aw], 12:[s12an, s12as, s12aw]}

# neighbours
# [north, east, south, west]

n0 = ({'North':1, 'East':4}, ['North', 'East'])
n1 = ({'North':2, 'East':5, 'South':0}, ['North', 'East', 'South'])
n2 = ({'North':3, 'East':13, 'South':1}, ['North', 'East', 'South'])
n3 = ({'East':6, 'South':2}, ['East', 'South'])
n4 = ({'North':5, 'East':7, 'West':0}, ['North', 'East', 'West'])
n5 = ({'North':13, 'East':8, 'South':4, 'West':1}, ['North', 'East', 'South', 'West'])
n6 = ({'East':10, 'South':13, 'West':3}, ['East', 'South', 'West'])
n7 = ({'North':8, 'East':11, 'West':4}, ['North', 'East', 'West'])
n8 = ({'North':9, 'East':14, 'South':7, 'West':5}, ['North', 'East', 'South', 'West'])
n9 = ({'North':10, 'East':12, 'South':8, 'West':13}, ['North', 'East', 'South', 'West'])
n10 = ({'East':15, 'South':9, 'West':6}, ['East', 'South', 'West'])
n11 = ({'North':14, 'West':9}, ['North', 'West'])
n12 = ({'North':15, 'South':14, 'West':9}, ['North', 'South', 'West'])

neighbours = {0:n0[0], 1:n1[0], 2:n2[0], 3:n3[0], 4:n4[0], 5:n5[0], 6:n6[0], 7:n7[0], 8:n8[0], 9:n9[0], 10:n10[0], 11:n11[0], 12:n12[0]}
neighbours_order = {0:n0[1], 1:n1[1], 2:n2[1], 3:n3[1], 4:n4[1], 5:n5[1], 6:n6[1], 7:n7[1], 8:n8[1], 9:n9[1], 10:n10[1], 11:n11[1], 12:n12[1]}

number_of_deaths = 2

# rewards and costs
cost_per_move = -1
reward_for_goal = 10
cost_of_death = -10

#######################################################################
#######################################################################




#######################################################################
#######################################################################
# INPUTS FOR TESTS
# states:	[2, g]
#			[1, d]
#			[0, 3]
test_s0an = [1.0, 0.0]
test_s0ae = [0.0, 1.0]
test_s1an = [1.0, 0.0, 0.0]
test_s1ae = [0.0, 1.0, 0.0]
test_s1as = [0.0, 0.0, 1.0]
test_s2ae = [1.0, 0.0]
test_s2as = [0.0, 1.0]
test_s3an = [1.0, 0.0]
test_s3aw = [0.0, 1.0]
test_transition_probs = {0:[test_s0an, test_s0ae], 1:[test_s1an, test_s1ae, test_s1as], 2:[test_s2ae, test_s2as], 3:[test_s3an, test_s3aw]}
test_n0 = ({'North':1, 'East':3}, ['North', 'East'])
test_n1 = ({'North':2, 'East':4, 'South':0}, ['North', 'East', 'South'])
test_n2 = ({'East':5, 'South':1}, ['East', 'South'])
test_n3 = ({'North':4, 'West':0}, ['North', 'West'])
test_neighbours = {0:test_n0[0], 1:test_n1[0], 2:test_n2[0], 3:test_n3[0]}
test_neighbours_order = {0:test_n0[1], 1:test_n1[1], 2:test_n2[1], 3:test_n3[1]}
test_number_of_deaths = 1
test_cost_per_move = -1
test_reward_for_goal = 10
test_cost_of_death = -10
#######################################################################
#######################################################################

class Squares():

	def __init__(self, square_id, transitions, neighbours, neighbours_order, reward):
		"""
			>>> s = Squares(1, test_transition_probs[1], test_neighbours[1], test_neighbours_order[1], test_cost_per_move)
			>>> s.square_id
			1
			>>> s.neighbours
			{'East': 4, 'North': 2, 'South': 0}
			>>> s.Q
			[0, 0, 0]
			>>> s.V
			0
			>>> s.reward
			-1
			>>> s.num_actions
			3
		"""
		self.square_id = square_id
		self.num_actions = len(neighbours)
		self.transitions = transitions
		self.V = 0
		self.cum_transitions = self.find_cum_transitions()
		self.neighbours = neighbours
		self.neighbours_order = neighbours_order
		self.Q = [0 for i in range(len(self.neighbours))]
		self.reward = reward
		self.cum_random_action_probs = self.find_random_action_probs()

	def find_cum_transitions(self):
		"""
			>>> s = Squares(1, test_transition_probs[1], test_neighbours[1], test_neighbours_order[1], cost_per_move)
			>>> s.transitions
			[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
			>>> s.find_cum_transitions()
			[[1.0, 1.0, 1.0], [0.0, 1.0, 1.0], [0.0, 0.0, 1.0]]
		"""
		cum_transitions = []
		for action in range(len(self.transitions)):
			sum_p = 0
			cum_transitions.append([])
			for p in range(len(self.transitions[action])):
				sum_p += self.transitions[action][p]
				cum_transitions[action].append(sum_p)
		return cum_transitions

	def next_destination(self, action):
		"""
			>>> seed(1)
			>>> s = Squares(1, test_transition_probs[1], test_neighbours[1], test_neighbours_order[1], test_cost_per_move)
			>>> s.next_destination(0)
			2
			>>> s.next_destination(0)
			2
			>>> s.next_destination(2)
			0
		"""
		rnd_num = random()
		for p in range(self.num_actions):
			if rnd_num < self.cum_transitions[action][p]:
				return self.neighbours[self.neighbours_order[p]]

	def find_random_action_probs(self):
		"""
			>>> s = Squares(3, test_transition_probs[3], test_neighbours[3], test_neighbours_order[3], test_cost_per_move)
			>>> s.find_random_action_probs()
			[0.5, 1.0]
		"""
		random_action_probs = [1.0/self.num_actions for i in range(self.num_actions)]
		cum_random_action_probs = [sum(random_action_probs[:i+1]) for i in range(len(random_action_probs))]
		return cum_random_action_probs

class GoalSquare():

	def __init__(self, square_id, reward):
		"""
			>>> g = GoalSquare(15, test_reward_for_goal)
			>>> g.square_id
			15
			>>> g.reward
			10
			>>> g.Q
			0
			>>> g.V
			0
		"""
		self.square_id = square_id
		self.reward = reward
		self.Q = 0
		self.V = 0
	
	def next_destination(self, action):
		return 0

class DeathSquare():

	def __init__(self, square_id, reward):
		"""
			>>> d = DeathSquare(14, test_cost_of_death)
			>>> d.square_id
			14
			>>> d.reward
			-10
			>>> d.Q
			0
			>>> d.V
			0
		"""
		self.square_id = square_id
		self.reward = reward
		self.Q = 0
		self.V = 0
	
	def next_destination(self, action):
		return 0


class Board():

	def __init__(self, transition_probs, neighbours, neighbours_order, number_of_deaths, cost_per_move, cost_of_death, reward_for_goal, number_of_rounds, alpha=0.5, beta=0.5):
		"""
			>>> b = Board(test_transition_probs, test_neighbours, test_neighbours_order, test_number_of_deaths, test_cost_per_move, test_cost_of_death, test_reward_for_goal, 100)
			>>> b.BoardSquares[1].square_id
			1
			>>> b.number_of_rounds
			100
			>>> b.current_round
			0
		"""
		self.number_of_normal_squares = len(neighbours)
		self.BoardSquares = [Squares(i, transition_probs[i], neighbours[i], neighbours_order[i], cost_per_move) for i in range(self.number_of_normal_squares)] + [DeathSquare(self.number_of_normal_squares+i+1, cost_of_death) for i in range(number_of_deaths)] + [GoalSquare(self.number_of_normal_squares+number_of_deaths+1, reward_for_goal)]
		self.number_of_rounds = number_of_rounds
		self.current_round = 0
		self.alpha = alpha
		self.beta = beta
		self.epsilon = (1/number_of_rounds)
		self.transition_probs = transition_probs
		self.neighbours = neighbours
		self.neighbours_order = neighbours_order
		self.number_of_deaths = number_of_deaths
		self.cost_per_move = cost_per_move
		self.test_cost_of_death = test_cost_of_death
		self.reward_for_goal = reward_for_goal

	def simulate(self):
		"""
			>>> seed(1)
			>>> b = Board(test_transition_probs, test_neighbours, test_neighbours_order, test_number_of_deaths, test_cost_per_move, test_cost_of_death, test_reward_for_goal, 1)
			>>> b.simulate()

		"""
		self.player = Individual(self)
		while self.current_round < self.number_of_rounds:
			#print 'Player is at square %i' % self.player.current_square
			self.player.choose_next_square()
			if self.player.current_square > len(self.neighbours) + self.number_of_deaths - 1:
				self.current_round += 1
				self.player.current_square = 0
				#print 'Goal - New round...'
				self.epsilon += (1/self.number_of_rounds)
			elif self.player.current_square > len(self.neighbours) - 1:
				self.current_round += 1
				self.player.current_square = 0
				#print 'Death - New round...'
				self.epsilon += (1/self.number_of_rounds)
		self.Q_dict = self.dictionary_of_Qs()

	def dictionary_of_Qs(self):
		"""
			>>> seed(1)
			>>> b = Board(test_transition_probs, test_neighbours, test_neighbours_order, test_number_of_deaths, test_cost_per_move, test_cost_of_death, test_reward_for_goal, 1000)
			>>> b.simulate()
			>>> b.dictionary_of_Qs()
			{0: {'East': -1.2890625, 'North': 1.0}, 1: {'East': -5.0, 'North': 4.0, 'South': -0.6875}, 2: {'East': 10.0, 'South': 0}, 3: {'West': -1.296875, 'North': -5.0}}
		"""
		return {sqr.square_id:{sqr.neighbours_order[a]:sqr.Q[a] for a in range(sqr.num_actions)} for sqr in self.BoardSquares[:self.number_of_normal_squares]}

class Individual():

	def __init__(self, board):
		"""
			>>> i = Individual(False)
			>>> i.current_square
			0
		"""
		self.current_square = 0
		self.board = board

	def choose_action(self):
		"""
			>>> seed(1)
			>>> b = Board(test_transition_probs, test_neighbours, test_neighbours_order, test_number_of_deaths, test_cost_per_move, test_cost_of_death, test_reward_for_goal, 1)
			>>> i = Individual(b)
			>>> i.choose_action()
			1
			>>> i.choose_action()
			0
			>>> i.choose_action()
			0
			>>> i.choose_action()
			1
		"""
		rnd_num1 = random()
		if rnd_num1 < self.board.epsilon:
			rnd_num2 = random()
			for p in range(len(self.board.BoardSquares[self.current_square].cum_random_action_probs)):
				if rnd_num2 < self.board.BoardSquares[self.current_square].cum_random_action_probs[p]:
					return p
		else:
			return self.board.BoardSquares[self.current_square].Q.index(max(self.board.BoardSquares[self.current_square].Q))

	def choose_next_square(self):
		"""
			>>> seed(1)
			>>> b = Board(test_transition_probs, test_neighbours, test_neighbours_order, test_number_of_deaths, test_cost_per_move, test_cost_of_death, test_reward_for_goal, 1)
			>>> i = Individual(b)
			>>> i.current_square
			0
			>>> i.board.BoardSquares[i.current_square].Q
			[0, 0]
			>>> i.choose_next_square()
			>>> i.current_square
			3
			>>> i.board.BoardSquares[i.current_square].Q
			[0, 0]
			>>> i.choose_next_square()
			>>> i.current_square
			4
			>>> i.board.BoardSquares[i.current_square].Q
			0

		"""
		old_state = self.current_square
		action = self.choose_action()
		self.current_square = self.board.BoardSquares[self.current_square].next_destination(action)
		self.board.BoardSquares[old_state].Q[action] = (1 - self.board.alpha)*self.board.BoardSquares[old_state].Q[action] + self.board.alpha*(self.board.BoardSquares[self.current_square].reward + self.board.beta*self.board.BoardSquares[self.current_square].V)
		self.board.BoardSquares[old_state].V = max(self.board.BoardSquares[old_state].Q)



B = Board(transition_probs, neighbours, neighbours_order, number_of_deaths, cost_per_move, cost_of_death, reward_for_goal, 500)
B.simulate()
print B.Q_dict
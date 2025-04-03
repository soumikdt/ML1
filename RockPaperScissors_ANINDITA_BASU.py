import numpy as np


class AninditaBasu:
    """"
    466254
    Anindita Basu
    """    
    def get_action(self, your_past_actions, opponent_past_actions):
        if opponent_past_actions == []:
            return np.random.choice(['rock', 'paper', 'scissors'])

        else:
            list = [x for x in ['rock', 'paper', 'scissors'] if x != opponent_past_actions[-1]]
            return np.random.choice(list)

class RockPaperScissorsMasters:
    """
    444444: Alfred Nobel
    555555: John Doe
    666666: Jane Doe
    """

    def get_action(self, your_past_actions, opponent_past_actions):
        if opponent_past_actions == []:
            return 'rock'
        else:
            return opponent_past_actions[-1]


class Evaluator:
    
    def action_is_valid(self, action):
        if action not in ['rock', 'paper', 'scissors']:
            return False
        return True

    def evaluate(self, participant_1, participant_2):
        team1_name = participant_1.__class__.__name__
        team2_name = participant_2.__class__.__name__
        print(f"Evaluating {team1_name} vs {team2_name}")

        team1_score = 0
        team2_score = 0

        team1_past_actions = []
        team2_past_actions = []

        for i in range(100000):
            team1_action = participant_1.get_action(team1_past_actions, team2_past_actions)
            team2_action = participant_2.get_action(team2_past_actions, team1_past_actions)

            if not self.action_is_valid(team1_action):
                print(f"Team 1 action {team1_action} is invalid")
                team2_score += 1
                team1_past_actions.append('invalid')
                team2_past_actions.append(team2_action)
                continue
            if not self.action_is_valid(team2_action):
                print(f"Team 2 action {team2_action} is invalid")
                team1_score += 1
                team1_past_actions.append(team1_action)
                team2_past_actions.append('invalid')
                continue

            if team1_action == team2_action:
                if np.random.rand() < 0.5:
                    team1_score += 1
                else:
                    team2_score += 1
            elif team1_action == 'rock' and team2_action == 'scissors':
                team1_score += 1
            elif team1_action == 'scissors' and team2_action == 'rock':
                team2_score += 1
            elif team1_action == 'paper' and team2_action == 'rock':
                team1_score += 1
            elif team1_action == 'rock' and team2_action == 'paper':
                team2_score += 1
            elif team1_action == 'scissors' and team2_action == 'paper':
                team1_score += 1
            else:
                team2_score += 1
            
            team1_past_actions.append(team1_action)
            team2_past_actions.append(team2_action)
            

        print(f"Team 1 score: {team1_score}")
        print(f"Team 2 score: {team2_score}")
        if team1_score > team2_score:
            print(f"Winner: {team1_name}")
        elif team2_score > team1_score:
            print(f"Winner: {team2_name}") 
        else:
            print("Tie!")

instance1 = AninditaBasu()
instance2 = RockPaperScissorsMasters()

evaluator = Evaluator()
evaluator.evaluate(instance1, instance2)
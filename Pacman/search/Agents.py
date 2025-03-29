from game import Agent, Directions
import random
class DumbAgent(Agent):
    "An agent that goes East until it can't."

    def getAction(self, state):
        
        print("Location: ", state.getPacmanPosition())
        
        legalActions = state.getLegalPacmanActions()
        print("Actions available: ", legalActions)
        
        if Directions.EAST in legalActions:
            print("Going East.")
            return Directions.EAST
        else:
            print("Stopping.")
            return Directions.STOP
        
# Create A Random Agent Class
class RandomAgent(Agent):
    def getAction(self, state):
        legalActions = state.getLegalPacmanActions()
        return random.choice(legalActions)  # Choose random action

    
# Create A Better Random Agent Class
class BetterRandomAgent(Agent):
    "An agent that chooses a random action but never stops."
    def getAction(self, state):
        legalActions = state.getLegalPacmanActions()

        if Directions.STOP in legalActions:
            legalActions.remove(Directions.STOP)

        return random.choice(legalActions) 

# Create ReflexAgent class

class ReflexAgent(Agent):
    "An agent that prioritizes eating food if possible."

    def getAction(self, state):
        "Chooses an action that eats food if available; otherwise, moves randomly (excluding STOP)."
        legalActions = state.getLegalPacmanActions()
        foodList = state.getFood().asList()

        # Choose an action that eats food if possible
        for action in legalActions:
            successor = state.generatePacmanSuccessor(action)
            if successor and successor.getPacmanPosition() in foodList:
                return action

        # If no immediate food, pick a random move (excluding STOP)
        if Directions.STOP in legalActions:
            legalActions.remove(Directions.STOP)
        return random.choice(legalActions)


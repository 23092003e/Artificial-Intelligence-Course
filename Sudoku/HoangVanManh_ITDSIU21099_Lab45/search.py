"""
In search.py, you will implement Backtracking and AC3 searching algorithms
for solving Sudoku problem which is called by sudoku.py
"""

from csp import *
from copy import deepcopy
import util
from collections import deque



def Backtracking_Search(csp):
    """
    Backtracking search initialize the initial assignment
    and calls the recursive backtrack function
    """
    # Create a deep copy of the initial assignment
    assignment = deepcopy(csp.values)
    
    # Call recursive backtracking with the initial assignment
    result = Recursive_Backtracking(assignment, csp)
    
    if result == "FAILURE":
        return "FAILURE"
    return result


def Recursive_Backtracking(assignment, csp):
    """
    The recursive function which assigns value using backtracking
    """
    # If assignment is complete, return it
    if isComplete(assignment):
        return assignment
    
    # Select the next unassigned variable using MRV heuristic
    var = Select_Unassigned_Variables(assignment, csp)
    
    # Try each value in the domain of the selected variable
    for value in Order_Domain_Values(var, assignment, csp):
        # Check if the value is consistent with the current assignment
        if isConsistent(var, value, assignment, csp):
            # Make a copy of the current assignment
            new_assignment = deepcopy(assignment)
            new_assignment[var] = value
            
            # Apply forward checking
            inferences = {}
            result = Inference(new_assignment, inferences, csp, var, value)
            
            if result != "FAILURE":
                # Recursively continue with the new assignment
                result = Recursive_Backtracking(new_assignment, csp)
                if result != "FAILURE":
                    return result
    
    # If no value leads to a solution, backtrack
    return "FAILURE"
    

def Inference(assignment, inferences, csp, var, value):
    """
    Forward checking using concept of Inferences
    """

    inferences[var] = value

    for neighbor in csp.peers[var]:
        if neighbor not in assignment and value in csp.values[neighbor]:
            if len(csp.values[neighbor]) == 1:
                return "FAILURE"

            remaining = csp.values[neighbor] = csp.values[neighbor].replace(value, "")

            if len(remaining) == 1:
                flag = Inference(assignment, inferences, csp, neighbor, remaining)
                if flag == "FAILURE":
                    return "FAILURE"

    return inferences

def Order_Domain_Values(var, assignment, csp):
    """
    Returns string of values of given variable
    """
    return csp.values[var]

def Select_Unassigned_Variables(assignment, csp):
    """
    Selects new variable to be assigned using minimum remaining value (MRV)
    """
    unassigned_variables = dict((squares, len(csp.values[squares])) for squares in csp.values if squares not in assignment.keys())
    mrv = min(unassigned_variables, key=unassigned_variables.get)
    return mrv

def isComplete(assignment):
    """
    Check if assignment is complete
    """
    return set(assignment.keys()) == set(squares)

def isConsistent(var, value, assignment, csp):
    """
    Check if assignment is consistent
    """
    for neighbor in csp.peers[var]:
        if neighbor in assignment.keys() and assignment[neighbor] == value:
            return False
    return True

def forward_checking(csp, assignment, var, value):
    csp.values[var] = value
    for neighbor in csp.peers[var]:
        csp.values[neighbor] = csp.values[neighbor].replace(value, '')

def display(values):
    """
    Display the solved sudoku on screen
    """
    for row in rows:
        if row in 'DG':
            print("-------------------------------------------")
        for col in cols:
            if col in '47':
                print(' | ', values[row + col], ' ', end=' ')
            else:
                print(values[row + col], ' ', end=' ')
        print(end='\n')

def write(values):
    """
    Write the string output of solved sudoku to file
    """
    output = ""
    for variable in squares:
        output = output + values[variable]
    return output

def AC3(csp):
    """
    AC-3 algorithm for enforcing arc consistency
    Returns False if an inconsistency is found, True otherwise
    """
    # Initialize queue with all arcs (constraints)
    queue = deque(csp.constraints)
    
    while queue:
        # Get the next arc to process
        (Xi, Xj) = queue.popleft()
        
        # If we can revise the domain of Xi
        if revise(csp, Xi, Xj):
            # If domain of Xi becomes empty, problem is unsolvable
            if len(csp.values[Xi]) == 0:
                return False
                
            # Add all arcs (Xk, Xi) where Xk is a peer of Xi (except Xj)
            for Xk in csp.peers[Xi]:
                if Xk != Xj:
                    queue.append((Xk, Xi))
    
    return True

def revise(csp, Xi, Xj):
    """
    Returns True if we revise the domain of Xi
    """
    revised = False
    
    # For each value in the domain of Xi
    for x in csp.values[Xi]:
        # If no value in Xj's domain is consistent with x
        if not any(x != y for y in csp.values[Xj]):
            # Remove x from Xi's domain
            csp.values[Xi] = csp.values[Xi].replace(x, '')
            revised = True
    
    return revised

def AC3_Search(csp):
    """
    AC-3 search algorithm for solving Sudoku
    """
    # First apply AC-3 to reduce domains
    if not AC3(csp):
        return "FAILURE"
    
    # If all variables have single values, we have a solution
    if all(len(csp.values[s]) == 1 for s in squares):
        return csp.values
    
    # Select the variable with minimum remaining values
    var = min((s for s in squares if len(csp.values[s]) > 1), 
              key=lambda s: len(csp.values[s]))
    
    # Try each value in the domain
    for value in csp.values[var]:
        # Create a copy of the CSP
        new_csp = deepcopy(csp)
        new_csp.values[var] = value
        
        # Recursively solve the new CSP
        result = AC3_Search(new_csp)
        if result != "FAILURE":
            return result
    
    return "FAILURE"

# Create a Sudoku puzzle string (0 represents empty cells)
puzzle = "003020600900305001001806400008102900700000008006708200002609500800203009005010300"

# Create CSP instance
sudoku = csp(grid=puzzle)

# Solve using Backtracking
solution = Backtracking_Search(sudoku)

# Or solve using AC3
# solution = AC3_Search(sudoku)

# Display the solution
if solution != "FAILURE":
    display(solution)
else:
    print("No solution found")
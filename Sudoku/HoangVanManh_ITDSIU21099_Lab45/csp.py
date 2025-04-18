# CLASS DESCRIPTION FOR CONSTRAINT SATISFACTION PROBLEM (CSP)

from util import *

class csp:

    # INITIALIZING THE CSP
    def __init__(self, domain=digits, grid=""):
        """
        Unitlist consists of the 27 lists of peers
        Units is a dictionary consisting of the keys and the corresponding lists of peers
        Peers is a dictionary consisting of the 81 keys and the corresponding set of 27 peers
        Constraints denote the various all-different constraints between the variables
        """
        self.variables = squares
        self.domain = domain
        self.values = self.getDict(grid)
        
        # Create row units
        row_units = [cross(r, cols) for r in rows]
        
        # Create column units
        column_units = [cross(rows, c) for c in cols]
        
        # Create box units
        box_units = []
        for rs in ('ABC', 'DEF', 'GHI'):
            for cs in ('123', '456', '789'):
                box_units.append(cross(rs, cs))
        
        # Combine all units
        self.unitlist = row_units + column_units + box_units
        
        # Create units dictionary
        self.units = dict((s, [u for u in self.unitlist if s in u]) for s in squares)
        
        # Create peers dictionary
        self.peers = dict((s, set(sum(self.units[s], [])) - set([s])) for s in squares)
        
        # Create constraints
        self.constraints = []
        for unit in self.unitlist:
            for i in range(len(unit)):
                for j in range(i + 1, len(unit)):
                    self.constraints.append((unit[i], unit[j]))

    def getDict(self, grid=""):
        """
        Getting the string as input and returning the corresponding dictionary
        """
        i = 0
        values = dict()
        for cell in self.variables:
            if grid[i] != '0':
                values[cell] = grid[i]
            else:
                values[cell] = digits
            i = i + 1
        return values
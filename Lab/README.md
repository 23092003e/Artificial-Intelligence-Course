# Pac-Man AI - README

## **Introduction**
This lab implements various Pac-Man agents to navigate through different maze environments using different decision-making strategies.

## **Setup Instructions**
### **1. Clone the Repository**
If you haven't already cloned the repository, run:
```bash
git clone https://github.com/23092003e/Artificial-Intelligence-Course
cd Lab1
```

### **2. Install Python (If Not Installed)**
Ensure you have Python 3 installed:
```bash
python --version
```
If not, download and install Python from [python.org](https://www.python.org/downloads/).

### **3. Run the Pac-Man Game**
Navigate to the directory where `pacman.py` is located:
```bash
cd search
```
To test the default Pac-Man game, run:
```bash
python pacman.py
```

## **Using Different Agents**
Below are the available Pac-Man agents and how to run them.

### **1. DumbAgent**
This agent always moves east (`EAST`) until it hits a wall, then stops.
#### **Run DumbAgent in Tiny Maze:**
```bash
python pacman.py --layout tinyMaze --pacman DumbAgent
```
#### **Run DumbAgent in Medium Maze:**
```bash
python pacman.py --layout mediumMaze --pacman DumbAgent
```

### **2. RandomAgent**
This agent picks a random action from the list of legal moves.
#### **Run RandomAgent:**
```bash
python pacman.py --layout tinyMaze --pacman RandomAgent
python pacman.py --layout mediumMaze --pacman RandomAgent
```

### **3. BetterRandomAgent**
This agent picks a random action but never chooses `STOP`.
#### **Run BetterRandomAgent:**
```bash
python pacman.py --layout openSearch --pacman BetterRandomAgent
python pacman.py --layout myLayout --pacman BetterRandomAgent
```

### **4. ReflexAgent**
This agent prioritizes eating food when possible. If no immediate food is available, it picks a random action (excluding STOP).
#### **Run ReflexAgent:**
```bash
python pacman.py --layout openSearch --pacman ReflexAgent
python pacman.py --layout myLayout --pacman ReflexAgent
```

## **Creating Your Own Maze**
You can create custom mazes by adding `.lay` files to the `layouts/` directory. Example of a simple custom layout (`myLayout.lay`):
```
%%%%%%%%
%......%
%.P..%.%
%......%
%%%%%%%%
```
Save it as `layouts/myLayout.lay` and run:
```bash
python pacman.py --layout myLayout --pacman RandomAgent
```

## **Game Controls & Display Options**
- **Change the view zoom:**
```bash
python pacman.py --layout bigMaze --zoom 0.5
```
- **Run without graphics (for speed-up):**
```bash
python pacman.py --layout mediumMaze --pacman ReflexAgent --frameTime 0
```

## **Conclusion**
This project provides different AI approaches to control Pac-Man, from basic movement to decision-making strategies. You can modify the agents in `Agents.py` to improve their intelligence. Happy coding!

---



# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from util import Stack, Queue, PriorityQueue
import util
class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    s=Stack()
    state=problem.getStartState()
    path=[state]
    dict={}
    parent={}
    temp=[]
    while(not(problem.isGoalState(state))):
        dict[state]='false'
        z=problem.getSuccessors(state)
        for y in z:
            if(not(y[0] in dict)):
                s.push(y)
                if(temp):
                    parent[y]=temp
        temp=s.pop()
        state=temp[0]
        print temp

    path=Stack()
    path.push(temp[1])
    while(temp in parent):
        path.push(parent[temp][1])
        temp=parent[temp]

    print path.list
    path.list.reverse()
    """
    print "Start:", problem.getStartState()
    s = Stack()
    state=problem.getStartState()
    z=problem.getSuccessors(state)

    dict={}
    temp=state
    p=1
    dict[temp]='false'
    for c in range(len(z)):
     if(not(dict.has_key(z[c][0]))):
      s.push(z[c])
      dict[z[c][0]]='false'
      p=0

    print p
    ty=[]
    lastbranching=Stack()
    lastbranching.push(temp)
    while(not(problem.isGoalState(state))):
     temp=s.pop()
     state=temp[0]
     if(p==0):
        ty.append(temp)
        print 'append',temp
     else:
         zr=lastbranching.pop()
         tr=[]
         while(not(tr==zr)):
          tr=ty.pop()
          print 'pop',tr
     p=1
     z=problem.getSuccessors(state)
     print 'range',range(len(z))
     while(c<=len(z)):
      if(not(z[c][0] in dict)):
         print 'Before delete',z
         del z[c-1]
         print 'after delete',z
         print 'len',len(z)
         c=0
         if(len(z)==0):
          break
     c=c+1
     if(len(z)>1):
         lastbranching.push(temp)
         print len(z)
         print 'lastbranching',lastbranching

     for c in range(len(z)):
       s.push(z[c])
       dict[z[c][0]]='false'
       p=0
       print 'children',z[c]
    l=[]
    print "Goal",state
    print "TY:",ty
    s=ty
    from game import Directions
    sa = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    if(problem.isGoalState(state)):
     print "reached goal:,"
     while(s):
      q=s.pop()
      print q
      if(q[1]=='South'):
        l.append(sa)
      elif(q[1]=='West'):
        l.append(w)
      elif(q[1]=='North'):
        l.append(n)
      else:
        l.append(e)
    print l
    l.reverse()
    """
    print 'function ending'

    return path.list

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    currentcost=0
    state=problem.getStartState()
    queue=PriorityQueue()
    parent={}
    while(not(problem.isGoalState(state))):
        successors=problem.getSuccessors(state)
        for a in successors:
            if(not(parent.has_key(a[0]))):

                c=currentcost+heuristic(a[0],problem)
                queue.push(a[0],c)
                parent[a[0]]=state
        currentcost=currentcost+1
        temp=queue.pop()
        state=temp[0]
    path=[]
    while(not(parent.has_key(temp[0]))):
        path.append(temp[1])
        temp=parent[temp[0]]
    print path
    return path

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

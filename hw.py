def path_finder(maze):
  #set start
  S = [0,0]
  #set end
  E = maze[len(maze)-1][len(maze)-1]
  #hold level value
  level = {s:0}
  #hold parent dictionary
  parent = {s: None}
  #hold explored values
  frontier = [s]
  #hold length of maze
  length = len(maze)

  #while loop to navigate in cardinal directions
  while frontier:
      #add values that come next
      next = []
      #for loop to check possible directions
      for x,y in frontier: #error here stops the code from running
        #for loop to check cardinal directions
        for x, y in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
           #

        if 0 <= x < length and 0 <= y < length:
      if x, y not in frontier:
                  #add value
        frontier.append(x,y)
              #find end
        if x, y == E:
                  #return True
          return True
  #return False if end not reached
  return False


          #add find_edges function from previous atom file




    return # can go to lower right corner from upper left one

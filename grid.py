class Grid:
  def __init__( self ):
    self.grid = []
    self.depend =  {
        "a0": 0,
        "a1": 0,
        "a2": 0,
        "a3": 0,
        "s0": 0,
        "s1": 0,
        "s2": 0,
        "s3": 0,
        "s4": 0,
        "s5": 0,
        "s6": 0,
        "s7": 0,
        "t0": 0,
        "t1": 0,
        "t2": 0,
        "t3": 0,
        "t4": 0,
        "t5": 0,
        "t6": 0,
        "t7": 0,
        "t8": 0,
        "t9": 0,
        "zero": 0,
        "v0": 0,
        "v1": 0
    }
    self.value =  {
        "a0": 0,
        "a1": 0,
        "a2": 0,
        "a3": 0,
        "s0": 0,
        "s1": 0,
        "s2": 0,
        "s3": 0,
        "s4": 0,
        "s5": 0,
        "s6": 0,
        "s7": 0,
        "t0": 0,
        "t1": 0,
        "t2": 0,
        "t3": 0,
        "t4": 0,
        "t5": 0,
        "t6": 0,
        "t7": 0,
        "t8": 0,
        "t9": 0,
        "zero": 0,
        "v0": 0,
        "v1": 0
    }


    # Insert line into grid - Sebastian
    def insertLine( self, line ):
        return

    # Prints out in the grid - Joe
    def printGrid( self ):
        return


    # Shifts arrays around to insert nop where needed
    def resolveHazard( self, depend, registers, forward ):
        return


    # Goes through line and returns what the instruction is and what each operation is - Kevin
    def stripLine( self ):
        return
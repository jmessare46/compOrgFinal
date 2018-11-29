class Grid:
    def __init__(self):
        self.grid = []              # 2d array which holds each row to be printed
        self.numOfRows = 0          # contains the number of rows in grid
        self.depend = {             # Dictionary which contains number of dependencies on each register
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
        self.value = {              # Dictionary which contains the value stored in each register
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

    # Main loop that prints out every iteration of output by calling printGrid in a loop
    # Inputs: None
    # Outputs: Prints the entire output for the program
    def runSimulation(self):

        pass

    # Insert line into grid - Sebastian
    # Inputs: line to be inserted into grid
    # Outputs: Updates 2d grid and numOfRows
    def insertLine(self, line):

        pass

    # Prints out a single cycle of the grid out - Joe
    # Input: cycle - The cycle number we are print (to determine visibility)
    # Outputs: Prints the output for this cycle of the simulation
    def printGrid(self, cycle):

        pass

    # Shifts arrays around to insert nop where needed
    # Inputs: None
    # Outputs: Updates grid and numOfRows to correct for hazards
    def resolveHazards(self, forwardingMode):

        pass

    # Goes through line and returns what the instruction is and what each operation is - Kevin
    # Inputs: instruction string
    #
    # Outputs:
    #           For instructions in the form of "instruction a,b,c"
    #           output1 - instruction
    #           output2 - operand a
    #           output3 - operand b
    #           output4 - operand c
    #
    #           For instructions in the form of "instruction $a,offset($b)"
    #           output1 - instruction
    #           output2 - operand a
    #           output3 - operand b
    #           output4 - NoneType (since there are only two registers used in this case)
    def stripLine(self, instruction):

        pass

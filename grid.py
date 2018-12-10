<<<<<<< HEAD
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
    
=======
class Grid:
    def __init__(self, forwardingMode, fileName):
        self.forwardingMode = forwardingMode    # Forwarding mode for simulation
        self.instructions = []                  # A list containing the set of instructions
        self.grid = []                          # 2d array which holds each row to be printed
        self.instructionIndex = 0               # Keeps track of which instruction we are running
                                                #  (need to maintain for branches)
        self.file = fileName                    # Name of file to be read with bne or beq
        self.loopVar = None                     # Variable to return to on loop
        self.cycle = 1                          # Keeps track of current cycle of simulation
        self.branchStartLoc = None              # Start location of where to start inserting * for branch not taken
        self.branchEndLoc = None                # End location of where to start inserting * for branch not taken
        self.values = {                         # Dictionary which contains the value stored in each register
            "$s0": 0,
            "$s1": 0,
            "$s2": 0,
            "$s3": 0,
            "$s4": 0,
            "$s5": 0,
            "$s6": 0,
            "$s7": 0,
            "$t0": 0,
            "$t1": 0,
            "$t2": 0,
            "$t3": 0,
            "$t4": 0,
            "$t5": 0,
            "$t6": 0,
            "$t7": 0,
            "$t8": 0,
            "$t9": 0,
            "$zero": 0
        }
        self.forwardingBus = {                  # Dictionary to keep track of if a register is available to be forwarded
            "$s0": False,
            "$s1": False,
            "$s2": False,
            "$s3": False,
            "$s4": False,
            "$s5": False,
            "$s6": False,
            "$s7": False,
            "$t0": False,
            "$t1": False,
            "$t2": False,
            "$t3": False,
            "$t4": False,
            "$t5": False,
            "$t6": False,
            "$t7": False,
            "$t8": False,
            "$t9": False,
            "$zero": False
        }

    # Prints a bar of '-' to output
    # Inputs: None
    # Outputs: A bar of '-' will be printed to standard output
    def printBar(self):

        # Print bar
        print('-' * 82)

    def printCPUCyclesLine(self):

        print("{0: <20}".format("CPU Cycles ===>"), end='')

        for i in range(1, 16):

            print("{0: <4}".format(i), end='')

        print(16)

    # Setup grid row for printing where "IF" is equal to the current cycle
    # Inputs: Takes the instruction from the instructions list
    # Outputs: Places instruction with its 16 pipeline stage cycles into a list and inserts them into the grid object
    def initNewGridRow(self, instruction):

        row = []
        count = 0

        # First append instruction into index 0
        row.append(instruction)

        count += 1

        # Next append '.' and 'IF' for remaining indexes
        while count <= 16:

            if count == self.cycle:

                row.append('IF')

            else:

                row.append('.')

            count += 1

        # Insert new row into grid
        self.grid.append(row)

    # Finds the index of the final instance of target in row
    # Inputs: row - list to search
    #           target - value to search for
    # Outputs: returns index of last encountered target in row
    def getIndex(self, row, target):

        index = 0

        for i, item in enumerate(row):

            if item == target:

                index = i

        return index

    # Takes an grid row index and checks the previous two instructions to see if this instruction is dependent on any
    # previous instructions
    # Inputs: gridRowIndex - The row index of the instruction we are working on
    #         possibleDep1 - The 'b' register
    #         possibleDep2 - The 'c' register
    # Outputs: Returns an integer indicating how many instructions cycles the dependency will take to clear
    def checkForDependency(self, gridRowIndex, possibleDep1, possibleDep2):

        retVal = 0

        # First instruction can't be dependent
        if gridRowIndex == 0:

            pass

        # Second instruction only look at previous line
        elif gridRowIndex == 1:

            inst, a, b, c = self.stripLine(self.grid[0][0])

            if a == possibleDep1 or a == possibleDep2:

                retVal = 1

            if self.forwardingMode == 'F' and self.forwardingBus[a] == True:

                retVal = 0

        # Third instruction or greater look at previous 2 lines
        elif gridRowIndex > 1:

            inst, a, b, c = self.stripLine(self.grid[gridRowIndex - 1][0])
            inst1, a1, b1, c1 = self.stripLine(self.grid[gridRowIndex - 2][0])

            if a1 == possibleDep1 or a1 == possibleDep2:

                retVal = 1

            if a == possibleDep1 or a == possibleDep2:

                retVal = 2

            if self.forwardingMode == 'F' and self.forwardingBus[a] == True and self.forwardingBus[a1] == True:

                retVal = 0

        return retVal

    # Inserts bubbles into any rows that occur after a nop row
    # Inputs: nopRowIndex - The index of the nop row
    # Outputs: Bubbles are inserted into all rows after the nop row
    def insertBubble(self, nopRowIndex):

        # Locate '*' in nop row to obtain index
        starIndex = self.getIndex(self.grid[nopRowIndex], '*')

        # Insert bubble in each row after that
        for i in range(nopRowIndex + 1, len(self.grid)):

            # Only operate if row is not a nop row
            if self.grid[i][0] != "nop":

                # Collect value to duplicate
                valToDupe = self.grid[i][starIndex - 1]

                # Duplicate it
                self.grid[i].insert(starIndex, valToDupe)

    # Returns a nop row template initialized to the correct spot
    # Inputs: cycleToStartOn - Determines which cycle the "IF" instruction lands on
    # Outputs: returns a nop row
    def getNopRow(self, cycleToStartOn):

        row = []
        count = 0

        # First append instruction into index 0
        row.append("nop")

        count += 1

        # Next append '.' and 'IF' for remaining indexes
        while count <= 16:

            if count == cycleToStartOn:

                row.append("IF")

            elif count == cycleToStartOn + 1:

                row.append("ID")

            elif count == cycleToStartOn + 2:

                row.append("*")

            else:

                row.append('.')

            count += 1

        return row

    # Advance grid row to next pipeline cycle
    # Inputs: A grid row index to operate on
    # Outputs: Updates that grid row to next pipeline cycle
    #           Returns bool indicating if instruction has reached "WB" stage
    def advanceGridRow(self, gridRowIndex):

        retValue = False

        # Only operate if row has not already reached "WB" stage
        if "WB" not in self.grid[gridRowIndex]:

            inst, a, b, c = self.stripLine(self.grid[gridRowIndex][0])

            # Remove last element of row
            # TODO: Use this when the bubble is created
            # del self.grid[gridRowIndex][16]

            # Handle adding stars to nop instructions
            if "nop" in self.grid[gridRowIndex]:

                # If this is a nop row but it has less than 3 stars add a star
                if self.grid[gridRowIndex].count("*") < 3:

                    self.grid[gridRowIndex].insert(self.getIndex(self.grid[gridRowIndex], "*") + 1, "*")

            elif "MEM" in self.grid[gridRowIndex] and "*" not in self.grid[gridRowIndex]:
                self.grid[gridRowIndex].insert(self.getIndex(self.grid[gridRowIndex], "MEM") + 1, "WB")

                # Instruction has advanced to WB stage
                retValue = True

            elif "EX" in self.grid[gridRowIndex]:
                # Accounts for branch prediction
                if self.branchStartLoc is not None and gridRowIndex >= self.branchStartLoc and gridRowIndex < self.branchEndLoc and self.grid[gridRowIndex].count("*") < 2:
                    self.grid[gridRowIndex].insert(self.getIndex(self.grid[gridRowIndex], "EX") + 1, "*")
                elif self.grid[gridRowIndex].count("*") == 0:
                    self.grid[gridRowIndex].insert(self.getIndex(self.grid[gridRowIndex], "EX") + 1, "MEM")

            elif "ID" in self.grid[gridRowIndex]:

                # Before advancing instruction to EX check previous two instructions to see if dependency exists
                dep = self.checkForDependency(gridRowIndex, b, c)

                # If a dependency is found we must insert nop and bubbles
                if dep:

                    # Insert nop row to current index
                    self.grid.insert(gridRowIndex, self.getNopRow(self.cycle - 2))

                    # Insert bubbles in each row after nop
                    self.insertBubble(gridRowIndex)

                # Else no dependency is found advance pipeline as normal
                else:
                    # Accounts for branch prediction
                    if self.branchStartLoc is not None and gridRowIndex >= self.branchStartLoc and gridRowIndex < self.branchEndLoc and self.grid[gridRowIndex].count("*") < 3 and self.grid[gridRowIndex-1].count("*") > 0:
                        self.grid[gridRowIndex].insert(self.getIndex(self.grid[gridRowIndex], "ID") + 1, "*")
                    elif self.grid[gridRowIndex].count("*") == 0:
                        self.grid[gridRowIndex].insert(self.getIndex(self.grid[gridRowIndex], "ID") + 1, "EX")

                        # Make available to be forwarded
                        self.forwardingBus[a] = True

            elif "IF" in self.grid[gridRowIndex]:
                # Accounts for branch prediction
                if self.branchStartLoc is not None and gridRowIndex >= self.branchStartLoc and gridRowIndex < self.branchEndLoc and self.grid[gridRowIndex].count("*") < 4 and self.grid[gridRowIndex - 1].count("*") > 0:
                    self.grid[gridRowIndex].insert(self.getIndex(self.grid[gridRowIndex], "IF") + 1, "*")
                elif self.grid[gridRowIndex].count("*") == 0:
                    self.grid[gridRowIndex].insert(self.getIndex(self.grid[gridRowIndex], "IF") + 1, "ID")

        return retValue

    # Executes the instruction and updates any registers
    def executeInstruction(self, instruction):

        # Do nothing is this is a nop instruction
        if instruction == "nop":

            return

        inst, a, b, c = self.stripLine(instruction)

        if inst == "add":

            self.values[a] = self.values[b] + self.values[c]

        elif inst == "addi":

            self.values[a] = self.values[b] + int(c)

        elif inst == "and":

            self.values[a] = self.values[b] & self.values[c]

        elif inst == "andi":

            self.values[a] = self.values[b] & int(c)

        elif inst == "or":

            self.values[a] = self.values[b] | self.values[c]

        elif inst == "ori":

            self.values[a] = self.values[b] | int(c)

        elif inst == "slt":
            if(self.values[b] < self.values[c]):
                self.values[a] = 1
            else:
                self.values[a] = 0

        elif inst == "slti":
            if(self.values[b] < int(c)):
                self.values[a] = 1
            else:
                self.values[a] = 0

        elif inst == "beq":
            if self.values[a] == self.values[b]:
                return c
            else:
                self.branchLoc = None
                return "cont"
            # TODO: Make this work

        elif inst == "bne":
            if self.values[a] != self.values[b]:
                return c
            else:
                self.branchLoc = None
                return "cont"
            # TODO: Make this work.

        return None

        # TODO: Finish implementing other instructions

    # Main loop that prints out every iteration of output by calling printGrid in a loop
    # Inputs: None
    # Outputs: Prints the entire output for the program
    def runSimulation(self, fp):

        self.fp = fp

        # Print simulation header
        if self.forwardingMode == 'N':

            print("START OF SIMULATION (no forwarding)")

        else:

            print("START OF SIMULATION (forwarding)")

        self.printBar()

        while True:

            loop = None

            # Add a pipeline cycle to previously ran lines already in grid
            for i in range(0, len(self.grid)):

                # Advance each row in grid to next pipeline stage and capture if the row has reached "WB"
                wbReached = self.advanceGridRow(i)

                # If an instruction has reached WB stage then update 'a' register value for that instruction
                if wbReached:

                    loop = self.executeInstruction(self.grid[i][0])         # Loop is set to continue or revert to branch based on bne beq
                    # TODO: Finish this
                    if self.loopVar is not None and isinstance(loop, str) and self.loopVar not in loop:

                        # Continue on after bne or beq
                        with open(self.file) as fp:
                            for line in fp:
                                # Strip newline
                                line = line.rstrip('\n')

                                # Checks for branches
                                # Insert line into instruction list
                                # Inputs: line to be inserted into instruction list
                                # Outputs: updates instruction list
                                if (line.__contains__(':')):
                                    self.loopVar = line.split(':', 1)[0]
                                else:
                                    if (self.loopVar is not None) and (self.loopVar in line):
                                        self.instructions.append(line)
                                    else:
                                        self.instructions.append(line)

                    else:
                        # Go back to loop variable start location

                        read = None  # Whether or not to read lines in
                        with open(self.file) as fp:
                            for line in fp:

                                # Strip newline
                                line = line.rstrip('\n')

                                # TODO: Fix this so it loops the second time for printing starts
                                if (line.__contains__(':')):
                                    self.loopVar = line.split(':', 1)[0]

                                # Checks for branches
                                # Insert line into instruction list
                                # Inputs: line to be inserted into instruction list
                                # Outputs: updates instruction list
                                if self.loopVar is not None and line.__contains__(':') and self.loopVar in line:
                                    read = True
                                elif read:
                                    if self.loopVar is not None and self.loopVar in line:
                                        self.instructions.append(line)
                                        self.loopVar = None  # Resets loop variable
                                    else:
                                        self.instructions.append(line)

                            # Something like this needs to replace the above (need to reset the branch start and end locations to the right place)
                            #         if (grid.loopVar is not None) and (grid.loopVar in line):
                            #             grid.instructions.append(line)
                            #             grid.branchStartLoc = len(grid.instructions)
                            #         else:
                            #             grid.instructions.append(line)
                            #
                            # grid.branchEndLoc = len(grid.instructions)


            # Append line for this cycle to grid if there are still instructions left to add
            if self.instructionIndex != len(self.instructions):

                # Insert instruction into grid
                self.initNewGridRow(self.instructions[self.instructionIndex])

                # Update instructionIndex to next instruction to run
                # TODO: instructionIndex should be set based on if there is a branch or not
                self.instructionIndex += 1

            # Print grid
            self.printCPUCyclesLine()
            self.printGrid()
            self.printBar()

            # Inc cycle counter
            self.cycle += 1

            # End of while loop iteration, move to next iteration or break out
            # Breakout condition - ran all 16 cycles or last instruction has reached "WB"
            if self.cycle == 17 or "WB" in self.grid[len(self.grid) - 1]:

                break

        # Print end of simulation message
        print("END OF SIMULATION")

    # Insert line into instruction list
    # Inputs: line to be inserted into instruction list
    # Outputs: updates instruction list
    def insertLine(self, line):
        if(line.__contains__(':')):
            loopEnd = line.split(':', 1)[0]

        else:
            self.instructions.append(line)

    # Prints out a single cycle of the grid out
    # Input: cycle - The cycle number we are print (to determine visibility)
    # Outputs: Prints the output for this cycle of the simulation
    def printGrid(self):

        for row in self.grid:

            print("{0: <20}".format(row[0]), end='')

            for i in range(1, 16):
                print("{0: <4}".format(row[i]), end='')

            print(row[16])

        regSet = ["$s0","$s1","$s2","$s3","$s4","$s5","$s6","$s7",
                  "$t0","$t1","$t2","$t3","$t4","$t5","$t6","$t7","$t8","$t9"]

        print()

        for i in range(len(regSet)):

            strToPrint = "{0} = {1}".format(regSet[i], self.values[regSet[i]])

            if i % 4 == 3 or i == 17:

                print(strToPrint)

            else:

                print("{0: <20}".format(strToPrint), end='')

    # Goes through line and returns what the instruction is and what each operation is
    # Inputs: instruction string
    # Outputs:
    #           For instructions in the form of "instruction a,b,c"
    #           output1 - instruction
    #           output2 - operand a
    #           output3 - operand b
    #           output4 - operand c
    def stripLine(self, instruction):

        # Perform first split to split instruction from registers
        if("nop" not in instruction):
            instr, operands = instruction.split(' ')

            # Second split get each register
            a, b, c = operands.split(',')
        else:
            a, b, c = None, None, None
            instr = "nop"

        return instr, a, b, c
>>>>>>> master

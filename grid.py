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
    def __init__(self, forwardingMode):
        self.forwardingMode = forwardingMode    # Forwarding mode for simulation
        self.instructions = []                  # A list containing the set of instructions
        self.grid = []                          # 2d array which holds each row to be printed
        self.instructionIndex = 0               # Keeps track of which instruction we are running
                                                #  (need to maintain for branches)
        self.cycle = 1                          # Keeps track of current cycle of simulation
        self.depends = {                        # Dictionary which contains number of dependencies on each register
            "$a0": 0,
            "$a1": 0,
            "$a2": 0,
            "$a3": 0,
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
            "$zero": 0,
            "$v0": 0,
            "$v1": 0
        }
        self.values = {                     # Dictionary which contains the value stored in each register
            "$a0": 0,
            "$a1": 0,
            "$a2": 0,
            "$a3": 0,
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
            "$zero": 0,
            "$v0": 0,
            "$v1": 0
        }

    # Prints a bar of '-' to output
    # Inputs: None
    # Outputs: A bar of '-' will be printed to standard output
    def printBar(self):

        # Print bar
        print('-' * 82)

    def printCPUCyclesLine(self):

        print("{0: <20}".format("CPU Cycles ===>"), end='')

        for i in range(1, 17):

            print("{0: <4}".format(i), end='')

        print()

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

    # Advance grid row to next pipeline cycle
    # Inputs: A grid row index to operate on
    # Outputs: Updates that grid row to next pipeline cycle
    #           Returns bool indicating if instruction has reached "WB" stage
    def advanceGridRow(self, gridRowIndex):

        retValue = False

        # Only operate if row has not already reached "WB" stage
        if "WB" not in self.grid[gridRowIndex]:

            # Remove last element of row
            del self.grid[gridRowIndex][16]

            if "MEM" in self.grid[gridRowIndex]:

                self.grid[gridRowIndex].insert(self.getIndex(self.grid[gridRowIndex], "MEM") + 1, "WB")

                # Instruction has advanced to WB stage
                retValue = True

            elif "EX" in self.grid[gridRowIndex]:

                self.grid[gridRowIndex].insert(self.getIndex(self.grid[gridRowIndex], "EX") + 1, "MEM")

            elif "ID" in self.grid[gridRowIndex]:

                self.grid[gridRowIndex].insert(self.getIndex(self.grid[gridRowIndex], "ID") + 1, "EX")

            elif "IF" in self.grid[gridRowIndex]:

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
            return
            # TODO: Make this work

        elif inst == "bne":
            return
            # TODO: Make this work.

        # TODO: Finish implementing other instructions

    # Get the number of dependencies on a register
    # Inputs: reg - Register to get the dependencies of
    # Outputs: returns number of clock cycles until dependencies is cleared
    #           or 0 if the 'reg' passed was actually a constant
    def getDependency(self, reg):

        if reg not in self.depends:

            return 0

        else:

            return self.depends[reg]

    # Insert a nop instruction into the grid
    # Inputs: None
    # Outputs: Inserts a nop instruction at the proper space in the grid
    def insertNop(self):

        self.initNewGridRow("nop")

    # Main loop that prints out every iteration of output by calling printGrid in a loop
    # Inputs: None
    # Outputs: Prints the entire output for the program
    def runSimulation(self):

        # Print simulation header
        if self.forwardingMode == 'N':

            print("START OF SIMULATION (no forwarding)")

        else:

            print("START OF SIMULATION (forwarding)")

        self.printBar()

        while True:

            # Add a pipeline cycle to previously ran lines already in grid
            for i in range(0, len(self.grid)):

                # Advance each row in grid to next pipeline stage and capture if the row has reached "WB"
                wbReached = self.advanceGridRow(i)

                # If an instruction has reached WB stage then update 'a' register value for that instruction
                if wbReached:

                    self.executeInstruction(self.grid[i][0])

            # Append line for this cycle to grid if there are still instructions left to add
            if self.instructionIndex != len(self.instructions):

                # Parse instruction and decide if any dependencies exist
                inst, a, b, c = self.stripLine(self.instructions[self.instructionIndex])

                # Update dependencies on 'a' register
                self.depends[a] = 3

                # If dependencies exist on 'b' or 'c' register then insert bubble and nop
                if self.getDependency(b) > 0 or self.getDependency(c) > 0:

                    # TODO: nop insertion needs some work to get inserted at the right spot (could possibly move this logic inside advanceGridRow())
                    self.insertNop()

                # Insert instruction into grid
                self.initNewGridRow(self.instructions[self.instructionIndex])

                # Update instructionIndex to next instruction to run
                # TODO: instructionIndex should be set based on if there is a branch or not
                self.instructionIndex += 1

            # Print grid
            self.printCPUCyclesLine()
            self.printGrid()
            self.printBar()

            # Dec depends
            for i in self.depends:

                if self.depends[i] > 0:

                    self.depends[i] -= 1

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

        self.instructions.append(line)

    # Prints out a single cycle of the grid out
    # Input: cycle - The cycle number we are print (to determine visibility)
    # Outputs: Prints the output for this cycle of the simulation
    def printGrid(self):

        for row in self.grid:

            print("{0: <20}".format(row[0]), end='')

            for i in range(1, 17):
                print("{0: <4}".format(row[i]), end='')

            print()

        regSet = ["$s0","$s1","$s2","$s3","$s4","$s5","$s6","$s7",
                  "$t0","$t1","$t2","$t3","$t4","$t5","$t6","$t7","$t8","$t9"]

        for i in range(len(regSet)):

            # If just printed 4th column print a new line
            if i % 4 == 0:

                print()

            strToPrint = "{0} = {1}".format(regSet[i], self.values[regSet[i]])

            print("{0: <20}".format(strToPrint), end='')

        print()

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
        instr, operands = instruction.split(' ')

        # Second split get each register
        a, b, c = operands.split(',')

        return instr, a, b, c
>>>>>>> master

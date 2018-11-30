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

    # Setup grid row for printing where "IF" is equal to the current cycle
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

    # Advance grid row to next pipeline cycle
    # Inputs: A grid row index to operate on
    # Outputs: Updates that grid row to next pipeline cycle
    def advanceGridRow(self, gridRowIndex):

        pass

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

                # If an instruction has reached WB stage then update 'a' register value for that instruction

            # Parse instruction and decide if any dependencies exist

                # Update dependencies on 'a' register

                # If dependencies exist on 'b' or 'c' register then insert bubble and nop

                # else no dependencies execute instruction

            # Append line for this cycle to grid if there are still instructions left to add
            if self.instructionIndex != len(self.instructions):

                self.initNewGridRow(self.instructions[self.instructionIndex])

                # Update instructionIndex to next instruction to run
                # TODO: instructionIndex should be set based on if there is a branch or not
                self.instructionIndex += 1

            # Print grid
            self.printGrid()
            self.printBar()

            # Dec depends
            for i in self.depends:

                if self.depends[i] > 0:

                    self.depends[i] -= 1

            # Inc cycle counter
            self.cycle += 1

            # End of while loop iteration, move to next iteration or break out
            # TODO: correct breakout condition, should be if last row in grid contains 'WB' or 16 cycles have passed
            if self.cycle == 17:

                break

        # Print end of simulation message
        print("END OF SIMULATION")

    # Insert line into instruction list
    # Inputs: line to be inserted into instruction list
    # Outputs: updates instruction list
    def insertLine(self, line):

        self.instructions.append(line)

    # Prints out a single cycle of the grid out - Joe
    # Input: cycle - The cycle number we are print (to determine visibility)
    # Outputs: Prints the output for this cycle of the simulation
    def printGrid(self):

        for row in self.grid:

            # TODO: Update code to print rows with proper formatting and also print register values
            print(row)


    # Goes through line and returns what the instruction is and what each operation is - Kevin
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

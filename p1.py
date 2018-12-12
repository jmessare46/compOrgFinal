# n<<<<<<< HEAD
import grid

# Step 1: Read in the file

# Step 2: Populate grid

# Step 3: Check for hazards

# Step 4: Loop through and print each line

# Reads in input for printing operation
# # TODO: 10 needs to be set to number of input lines
# grid = []
# for inst in range (0,10):
#     list = []
#     for col in range (0,16):
#         list.append()
#     grid.append()


#
# register = new register()
#
# # Check for hazards and insert nop into grid
# haz.checkHazards( register, dependencies, grid )
#
# # Prints out the pipeline state
# printpipe.printPipeline( registers, dependencies, grid )

# =======
import grid
import sys

# Check proper number of params were passed to the program
if len(sys.argv) != 3:
    # TODO: print out specific error message
    # Exit with error if wrong number of parameters were passed
    print("Error: Incorrect Arguments!", file=sys.stderr)
    exit(1)

# Assign params to variables
forwardingMode = sys.argv[1]
inFileName = sys.argv[2]

# Read lines into grid
with open(inFileName) as fp:

    # Instantiate Grid object
    grid = grid.Grid(forwardingMode, inFileName)

    for line in fp:

        # Strip newline
        line = line.rstrip('\n')

        if line.isspace() or line == '':
            continue

        # print("printing in main\n")

        # Checks for branches
        # Insert line into instruction list
        # Inputs: line to be inserted into instruction list
        # Outputs: updates instruction list
        if (line.__contains__(':')):
            grid.loopVar = line.split(':', 1)[0]
        else:
            if (grid.loopVar is not None) and (grid.loopVar in line):
                grid.instructions.append(line)
                grid.branchStartLoc = len(grid.instructions)
            else:
                grid.instructions.append(line)

        grid.branchEndLoc = len(grid.instructions)

# Print all output

# grid.runSimulation()

grid.runSimulation( fp )


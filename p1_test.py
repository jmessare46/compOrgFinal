import grid_test
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
    grid = grid_test.Grid(forwardingMode, inFileName)

    for line in fp:

        # Strip newline
        line = line.rstrip('\n')

        # Checks for branches
        # Insert line into instruction list
        # Inputs: line to be inserted into instruction list
        # Outputs: updates instruction list
        if (line.__contains__(':')):
            grid.loopVar = line.split(':', 1)[0]
        else:
            if (grid.loopVar != None) and (grid.loopVar in line):
                grid.instructions.append(line)
                # break
            else:
                grid.instructions.append(line)

# Print all output
grid.runSimulation( fp )
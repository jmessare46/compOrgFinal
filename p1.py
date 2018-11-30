import grid
import sys

# Check proper number of params were passed to the program
if len(sys.argv) != 3:

    # Exit with error if wrong number of parameters were passed
    exit(1)

# Assign params to variables
forwardingMode = sys.argv[1]
inFileName = sys.argv[2]

# Instantiate Grid object
grid = grid.Grid()

# Step 1: Read lines into grid
with open(inFileName) as fp:

    for line in fp:

        # Strip newline
        line = line.rstrip('\n')

        # Insert into grid
        grid.insertLine(line)

# Step 2: Run hazard correction routine
grid.resolveHazards(forwardingMode)

# Step 3: Print all output
grid.runSimulation()

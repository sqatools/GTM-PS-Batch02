from behave import given, when, then
from rover import Rover

@given("the plateau size is {x:d} {y:d}")
def step_impl(context, x, y):
    context.plateau_size = (x, y)

@given("a rover at position {x:d} {y:d} facing {direction}")
def step_impl(context, x, y, direction):
    context.rover = Rover(x, y, direction)

@when("the rover receives instructions {instructions}")
def step_impl(context, instructions):
    context.rover.move(instructions)

@then("the rover should be at position {x:d} {y:d} facing {direction}")
def step_impl(context, x, y, direction):
    assert context.rover.position == (x, y)
    assert context.rover.direction == direction



#google

dirs = "NESW"                   # Notations for directions
shifts=[(0,1),(1,0),(0,-1),(-1,0)] # delta vector for each direction
# One letter function names corresponding to each robot instruction
r = lambda x, y, a: (x, y, (a + 1) % 4)
l = lambda x, y, a: (x, y, (a - 1 + 4) % 4)
m = lambda x, y, a: (x + shifts[a][0], y + shifts[a][1], a)
raw_input()                     # Ignore the grid size
while 1:
    # parse initial position triplet
    x, y, dir = raw_input().split()
    pos = (int(x),int(y),dirs.find(dir))
    # parse instructions
    instrns = raw_input().lower()
    # Invoke the corresponding functions passing prev position
    for i in instrns: pos = eval('%s%s' % (i, str(pos)))
    print pos[0], pos[1], dirs[pos[2]]


############################################
import Data.List

dirs = "NESW"

shifts
0 = (0, 1)
shifts
1 = (1, 0)
shifts
2 = (0, -1)
shifts
3 = (-1, 0)

instrn(x, y, a)
'R' = (x, y, mod(a + 1) 4)
instrn(x, y, a)
'L' = (x, y, mod(a - 1 + 4) 4)
instrn(x, y, a)
'M' = (x + fst(shifts a), y + snd(shifts
a), a)

showpos(x, y, a) = show
x + + " " + + show
y + + " " + + [dirs !! a]
finddir
dirchar =
case
elemIndex
dirchar
dirs
of
Nothing -> error
"invalid direction"
Just
position -> position
readpos
line = (x, y, a)
where
a = finddir $ head $ drop
1
line3
[(y, line3)] = reads
line2:: [(Integer, String)]
[(x, line2)] = reads
line:: [(Integer, String)]

robo = do
posn < - getLine
instrns < - getLine
putStrLn(showpos(foldl
instrn(readpos
posn) instrns))
robo

main = do
skip < - getLine
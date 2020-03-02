'''Sarvagaya is trapped in maze. The Masai command center sent him a string which decodes to come out from the maze. He is initially at (0, 0). String contains L, R, U, D denoting left, right, up and down. In each command he will traverse 1 unit distance in the respective direction.

For example if he is at (2, 0) and the command is L he will go to (1, 0).
'''

send = str(input())
send.upper()

x = 0
y = 0

if len(send)<200:
    for cmd in send:
        if cmd == 'L':
            x = x-1
        elif cmd == 'R':
            x = x+1
        elif cmd == 'D':
            y = y-1
        elif cmd == 'U':
            y = y+1
        else:
            break

print(x,y)

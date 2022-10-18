import pygame

scale = 5
#pygame.font.init = True
display = pygame.display.set_mode()
count = 0
#font = pygame.font.Font(None, 14)
upper_limit = 20
iters = {}
max_so_far = 0

def n_sequence(n):
  count = 0
  while not n==1:
    if n%2 == 0:
      n = int(n/2)
    else:
      n = int(3*n+1)
    #print(n)
    count +=1
  #print(count)
  return count
  #print("it took " + count + " loops for the sequence to reach 1.")

#----------------------------------------------------------------
  
for start in range(2, upper_limit+1):
#  count = 0
  iters[start] = n_sequence(start)
if len(iters) > 1:
  pygame.draw.lines(display, 'white', False, (list(iters.items())*scale))4
  
new_display = pygame.transform.flip(display, False, True)
display.blit(new_display, (0, 0))


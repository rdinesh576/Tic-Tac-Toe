import random

def initial_Board(grid,grid_n):

    if grid_n == 3:
        for i in range(0, grid_n ):
          print ("                |                   |                   ")
          print ("      ",grid[i*3+0],"       |","       ",grid[i*3+1],"        |","       ",grid[i*3+2],"        ")
          print ("                |                   |                   ")
          if( i!= 2):
           print ("--------------------------------------------------------")

    elif grid_n == 4:
        for i in range(0, grid_n):
            print ("                |                   |                   |                   ")
            print ("      ", grid[i * 4 + 0], "       |", "       ", grid[i * 4 + 1], "        |", "       ", grid[
                i * 4 + 2], "        |", "       ", grid[i * 4 + 3], "        ")
            print ("                |                   |                   |                   ")
            if (i != 3):
                print ("------------------------------------------------------------------------")


poss=[]
poss1=[]

def pickRandom(grid,nop1,grid_n):

 if nop1 == 2:
   #For horizontal block opponent validation
   for q in ['O','X']:
        for i in range(0, grid_n):
            for n in range(0,grid_n):
                a1=grid[i*(grid_n)+n]
                poss.append(a1)

            count_v = poss.count(q)

            if ((count_v == (grid_n-1)) & ('a' in poss)):
                random_n= (((grid_n)*i+(poss.index('a')))+1);
                sys_choice.remove(random_n)
                del poss[:]
                return random_n

            del poss[:]

        #For Column Block opponent validation
        for i in range(0, grid_n):
            for n in range(0,grid_n):
                a1=grid[i+((grid_n)*n)]
                poss.append(a1)

            count_v = poss.count(q)

            if (count_v == (grid_n - 1)) & ('a' in poss):
                random_n= ( i+((grid_n)*(poss.index('a')))+1);
                sys_choice.remove(random_n)
                del poss[:]
                return random_n

            del poss[:]

        #For Diagonal Block opponent Validation
            for j in range(0,grid_n):
                    a1=grid[(grid_n+1)*j];
                    poss.append(a1);
                    a2=grid[(grid_n-1)*(j+1)];
                    poss1.append(a2);

                    count_d1=poss.count(q);
                    count_d2=poss1.count(q);
                    if (count_d1 == (grid_n-1)) & ('a' in poss):
                            random_n= ((grid_n+1)*(poss.index('a')))+1;
                            sys_choice.remove(random_n);
                            del poss[:]
                            return  random_n;

                    elif (count_d2 == (grid_n - 1)) & ('a' in poss1):
                        random_n = ((grid_n - 1) * (poss1.index('a')+1))+1;
                        sys_choice.remove(random_n);
                        del poss1[:]
                        return random_n;


            del poss[:]
            del poss1[:]



   random_n = random.choice(sys_choice)
   sys_choice.remove(random_n)

   return random_n

 elif(nop1 == 1):
     random_n = random.choice(sys_choice)
     sys_choice.remove(random_n)

     return random_n

def choice(grid,nop,nop1,grid_n):
    choice_lo=9
    player=counter()

    pd = player % 2

    #For 2 Players
    if nop == 2:

      if player!= (grid_n * grid_n )+1:
         if pd == 0:
          print ("Enter the Choice for Player ",pd+2)
         elif pd == 1:
             print ("Enter the choice for Player ",pd)

         hasInput_2=True

         #Input Validation
         while hasInput_2:
            choice_n = (input())
            if choice_n!="":
                if choice_n.isdigit():
                        choice_n=int(choice_n)
                        if choice_n in sys_choice:
                            hasInput_2=False
                        else:
                            print ("Enter a Valid Number from the remaining choices ",sys_choice)

                else:
                    print ("Enter the numbers only\n")
            else:
                print ("Please enter something as input\n")

         choice_lo=choice_lo-1
         if pd == 1:
            grid[choice_n-1]='X'
         elif(pd == 0):
             grid[choice_n - 1] = 'O'

         sys_choice.remove(choice_n)

         initial_Board(grid,grid_n )
         checkWin(grid,choice_lo,grid_n )
         choice(grid,nop,nop1,grid_n )
      else:
         print ("\n No One Wins the Game. Its a TIE !!!!")

    # For 1 Player
    elif nop == 1:

         if player != ((grid_n * grid_n )+1):

             # For Player1
             if pd == 1:
                 print ("Enter the Choice for Player ", pd)
                 hasInput= True

                 #Input Validation
                 while hasInput :

                        choice_n = (input())

                        if choice_n != "":

                            if choice_n.isdigit():

                                 choice_n=int(choice_n)
                                 if choice_n in sys_choice:
                                       hasInput=False
                                 else:
                                       print ("Enter a Valid Number from remaining choices ",sys_choice)

                            else:
                                print ("Please enter numbers only\n")

                        else:
                            print ("Please enter something as input\n")

                 grid[choice_n - 1] = 'X'
                 sys_choice.remove(choice_n)

             #For Player System
             if pd == 0:
                 print ("System Turn to Play")
                 choice_n = int(pickRandom(grid,nop1,grid_n ))
                 choice_lo = choice_lo - 1


                 print ("system choice", choice_n, "\n")
                 grid[choice_n - 1] = 'O'

             initial_Board(grid,grid_n )
             checkWin(grid, pd,grid_n )
             choice(grid, nop,nop1,grid_n)
         else:
              print ("\n No One Wins the Game. Its a TIE !!!!")
              exit(1)


#For creating a static variable as static do not exists in python
def counter():
    if 'cnt' not in counter.__dict__:
        counter.cnt = 0
    counter.cnt += 1
    return counter.cnt


def checkWin(grid, pd, grid_n):
    win_count_row1 = 0; win_count_col1 = 0; win_count_dia1 = 0
    win_count_row2 = 0; win_count_col2 = 0; win_count_dia2 = 0
    count_r1 = 0; count_r2 = 0;
    count_c1 = 0; count_c2 = 0;
    count_d2 = 0; count_d22 = 0;
    count_d1 = 0; count_d11 = 0;

    # For Horizontal win Check
    for i in range(0,grid_n):
        count_r1 = 0;count_r2 = 0;
        for j in range(0,grid_n ):

            if(grid[i*grid_n +j]=='X'):
                count_r1=count_r1+1
                if count_r1 == grid_n:
                    win_count_row1=win_count_row1+1
            elif (grid[i*grid_n +j]=='O'):
                count_r2 = count_r2 + 1
                if (count_r2 == grid_n):
                    win_count_row2 = win_count_row2 + 1

    # For Vertical Win Check
    for i in range(0,grid_n ):
        count_c1 = 0;
        count_c2 = 0;
        for j in range(0 , grid_n):
            if grid[i + (grid_n *j)] == 'X':
                count_c1 = count_c1 + 1
                if count_c1 == (grid_n ):
                    win_count_col1=win_count_col1+1
            elif grid[i + (grid_n * j )]=='O':
                count_c2 = count_c2 + 1
                if count_c2 == (grid_n):
                    win_count_col2 = win_count_col2 + 1

    # For Diagonal Win Check
    for i in range(0,grid_n ):
        if grid[(grid_n + 1)*i] == 'X':
            count_d1 = count_d1 + 1
        if grid[(grid_n - 1) * (i+1)] == 'X':
            count_d11 = count_d11 + 1
        if grid[(grid_n + 1) * i] == 'O':
            count_d2 = count_d2 + 1
        if grid[(grid_n - 1) * (i+1)] == 'O':
            count_d22 = count_d22 + 1

        if count_d1 == grid_n | count_d11 == grid_n:
                win_count_dia1 = win_count_dia1 + 1

        elif count_d2 == grid_n | count_d22 == grid_n:
                win_count_dia2 = win_count_dia2 + 1


    # wining status
    if win_count_row1 == 1 | win_count_col1 == 1 | win_count_dia1 == 1:
        print("Player1 Wins the Game\n")
        exit(0)

    elif win_count_row2 == 1 | win_count_col2 == 1 | win_count_dia2 == 1 & pd == 0:
        print("System Wins the Game\n")
        exit(0)

    elif win_count_row2 == 1 | win_count_col2 == 1 | win_count_dia2 == 1:
        print("Player2 Wins the Game\n")
        exit(0)
start=0;
while start==0:
    print("                                    WELCOME TO THE TIC-TAC-TOE GAME                         \n")
    print("                                    -------------------------------                         \n")
    print("                                       Choose number of Grids                               \n")
    print("                                              3 x 3 Grid                                  \n")
    print("                                              4 x 4 Grid                                  \n")

    grid_input = True

    # To choose 1/2 Players
    user_choice_n=[1,2]
    grid_choice_n=[3,4]

    print ("Enter the choice to select Grid\n")
    while grid_input:
        grid_n = ( input());

        if grid_n != "":

                if grid_n.isdigit():

                        grid_n = int(grid_n)
                        if grid_n in grid_choice_n:
                            grid_input = False

                        else:
                            print ("Enter the Valid Grid Number 3 or 4  \n")

                else:

                        print ("Please Enter the numbers only \n")

        else:
            print ("Please Enter something as input\n")


    print("                                       Choose number of players                             \n")
    print("                                             1.One Player                                   \n")
    print("                                             2.Two Players                                  \n")

    # Creating the Grid for printing the game
    grid=[]

    for i in range(1, (grid_n*grid_n)+1):
        grid.append('a')

    # Player system choices
    sys_choice=[]

    for i in range(1, (grid_n*grid_n)+1):
        sys_choice.append(i)

    print("Enter the choice 1 or 2 \n")

    hasInput1 = True
    nop1 = 0

    #  For validation of input data
    while hasInput1:

        nop = input()

        if nop != "":

            if nop.isdigit():
                nop = int(nop)
                if nop in user_choice_n:
                    hasInput1 = False
                else:
                    print("Enter a Valid Number 1 or 2 for number of players ")

            else:
                   print ("Enter the Numbers only\n")
        else:
            print ("Please enter something as input\n")

    # Defining the Players
    if nop == 1:
        print("                                       Choose Level for Single Player                       \n")
        print("                                             1.Beginner                                     \n")
        print("                                             2.Expert                                      \n\n")
        print("                                       THE SECOND PLAYER IS SYSTEM                           \n")
        hasInput2 = True
        while hasInput2:

            nop1 = (input())

            if nop1 != "":

                if nop1.isdigit():
                        nop1=int(nop1)
                        if nop1 in user_choice_n:
                            hasInput2 = False
                        else:
                            print("Enter a Valid Number 1 or 2 for choosing the level ")
                else:
                    print ("Enter the numbers only\n")

            else:
                print ("Please enter something as input\n")

    initial_Board(grid,grid_n )
    choice(grid,nop,nop1,grid_n )
    start=start+1;
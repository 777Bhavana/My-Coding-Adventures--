// works perfect but....... it cant tell a tie ! sry

import java.util.Scanner;
public class tic_tac_toe
{
     static String m[] = new String [10];
     static String X="X", O="O";

     

    
    
    
     public static void boardPrinter( String[] b)
    {
       System.out.println(b[7]+" | "+b[8]+" | "+b[9]); 
       System.out.println("----------");
       System.out.println(b[4]+" | "+b[5]+" | "+b[6]);  
       System.out.println("----------");
       System.out.println(b[1]+" | "+b[2]+" | "+b[3]);
       System.out.println("\n");

    }



        
    public static void winner()
	{
		for (int a = 0; a < 8; a++) {
			String line = null;

			switch (a)
            {
			case 0:
				line = m[0] + m[1] +m[2];
				break;
			case 1:
				line = m[3] + m[4] + m[5];
				break;
			case 2:
				line = m[6] +m[7] + m[8];
				break;
			case 3:
				line = m[0] + m[3] + m[6];
				break;
			case 4:
				line =m[1] + m[4] +m[7];
				break;
			case 5:
				line = m[2] + m[5] + m[8];
				break;
			case 6:
				line = m[0] + m[4] + m[8];
				break;
			case 7:
				line = m[2] + m[4] + m[6];
				break;
			}
			//For X winner
			if (line.equals("XXX"))
            {
				System.out.println("the player X is the winner");
                System.exit(0);
            }
			
			// For O winner
			 else if (line.equals("OOO")) 
             {
            System.out.println("the player O is the winner");
            System.exit(0);
             }
			
		}

    
		}

    

    


   public static void play() 
   {
     /**
      * the player x is the user and o is the random computer player */
      int count =0; boolean w,r;
      boardPrinter(m);
      Scanner in = new Scanner(System.in);
      System.out.println("The player 'X' is the user and 'O' is the computer");
      while(count<=9)
      {
        
        w=true;r=true;

        // players loop turn
        while (w==true)
        {
            System.out.println("enter your move ");
            int player = in.nextInt();
            if (m[player]==" ")
            {
            count+=1;
            m[player]="X";
            boardPrinter(m);
            w=false;
            }
            else
            { 
            System.out.println(" oh the place is already taken try again");
            continue  ;
            }

        while (r==true)
        {
            int computer = (int)(Math.random()*8)+1;

            if (m[computer]==" ")
            {
                m[computer]="O";
                count+=1;
                boardPrinter(m);
                r=false;
            }
            else continue;
        }

        if (count>5)
        {
            winner();
        }

    }
}

      
      }
    
    public static void main(String[] args) 
    {
        for (int i=1;i<=9;i++) 
        m[i] = " " ;
        
        play();
        
    }

}


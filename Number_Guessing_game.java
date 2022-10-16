import java.util.Scanner;
public class Number_Guessing_game 
{
    public static int baby()
    {
        Scanner in = new Scanner(System.in);
        int guess=0,score=0,ran,x=10;
        
        ran =(int)(Math.random()*x)+1;
        while(guess!=ran)
        {
            System.out.println("Enter you Guess");
            guess =in.nextInt();
            score+=1;
            if(guess>x || guess<1) 
            System.out.println("PLEASE ENTER WITHIN THE RANGE");
            if(guess>ran)
            System.out.println("The numer is lower than this");
            if(guess<ran)
            System.out.println("the number is higher than this");
        }
        System.out.println("Yayy you guessed the no right in\t "+ score + "\t  attempts");
        
        return score;
    }

                                                 


    public static void main(String[] args) {
        while(true)
        {
        baby();
        System.out.println("enter 1  to play again or 2 to exit");
        Scanner in = new Scanner (System.in);
        int ch =in.nextInt();
        if (ch==1) continue; 
        else 
        System.out.println("Alvida bye sayonara matashita"); break;
        }
    }


}

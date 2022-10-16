import java.util.Scanner;
class temperature_conversion
{
    public static void main(String args[])
    {
        Scanner in = new Scanner(System.in);
        System.out.println('\u000C');
        System.out.println("Welcome To My Temperature Conversion Calculator");
        System.out.println("Please Choose Your Required Option Properly");
        System.out.println("1. Celsius     to   Kelvin");
        System.out.println("2. Kelvin      to   Celsius");
        System.out.println("3. Farhienheit to   Celsius");
        System.out.println("4. Celcius     to   Farhienheit ");
        System.out.println("5. Farhienheit to   Kelvin");
        System.out.println("6. Kelvin      to   Farhienheit");

        System.out.println("Enter Your Choice");
        int ch =in.nextInt();
        double k,f,c;
        System.out.println('\u000C');
        switch (ch)
        {
            case 1:
                System.out.println("1. Celsius     to   Kelvin");
                System.out.println("enter in Celcius ");
                c=in.nextDouble();
                k=c+273.15;
                System.out.println("your answer"+k+"K");
                break;

            case 2:
                System.out.println("2. Kelvin      to   Celsius");
                System.out.println("enter in kelvin");
                k=in.nextDouble();
                c=k-273.15 ;
                System.out.println("your answer"+c +"C ");
                break;


            case 3:
                System.out.println("3. Farhienheit to   Celsius");
                System.out.println("enter in Farhienheit ");
                f=in.nextDouble();
                c=(f-32)*5/9;
                System.out.println("your answer"+c +"C ");
                break;

            case 4:
                System.out.println("4. Celcius     to   Farhienheit ");
                System.out.println("enter in Celcius  ");
                c=in.nextDouble();
                f= c*(9/5)+32;
                System.out.println("your answer"+f +" F");
                break;

            case 5:
                System.out.println("5. Farhienheit to   Kelvin");

                System.out.println("enter in Farhienheit ");
                f=in.nextDouble();
                k=(f-32)*5/9+273.15;
                System.out.println("your answer"+ k+" K");
                break;


            case 6:
                System.out.println("6. Kelvin      to   Farhienheit");
                System.out.println("enter in kelvin");
                k=in.nextDouble();
                f=(k-273)*9/5+32;
                System.out.println("your answer"+f +"F ");
                break;
        }

        in.close();

    }
}


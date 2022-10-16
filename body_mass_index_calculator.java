import java.util.Scanner;
public class body_mass_index_calculator {
    public static void main(String[] args){
        Scanner iyer =new Scanner(System.in);
        System.out.println("Hello!!!!");
        System.out.println("Welcome to BMI Calculator");
        System.out.println("Body mass index (BMI) is a value derived from the mass (weight) and \n height of a person. The BMI is defined as the body mass divided by the square of the body \n height, and is expressed in units of kg/m2, resulting  from mass in kilograms \n and height in metres.");
        System.out.println();
        System.out.println();
        System.out.println();
        System.out.println("To Calculate your body mass index [BMI] do as directed");
        System.out.println("Please enter your input in the METRIC SYSTEM");
        double h,w,bmi;
        System.out.println("enter your height in METERS");
        h=iyer.nextDouble();
        System.out.println("Enter your weight in KILOGRAMS");
        w=iyer.nextDouble();
        h=h*h;
        bmi = w/h;
        System.out.println('\u000C');
        System.out.println("YOUR BMI ="+bmi);
        iyer.close();


    }

}

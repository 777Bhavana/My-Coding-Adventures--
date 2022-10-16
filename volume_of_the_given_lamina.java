import java.util.Scanner;
class volume_of_the_given_lamina {
    public static void main(String[]args){
        Scanner in = new Scanner(System.in);
        System.out.println("Volume Calculator");
        System.out.println("Enter your Lamina");
        System.out.println("1.cube \n 2.Cylinder \n 3.Cuboid \n 4.Sphere \n 5.Cone \n 6.pyramid");
        int ch = in.nextInt();
        double length ,volume,radius,height,pi=3.14159265 ,width,base;
        switch (ch)
        {
            case 1: //cube
                System.out.println("Enter the length");
                length =in.nextDouble();
                volume =Math.pow(length,3);
                System.out.println("volume of the cube =\t"+volume);
                break;
            case 2:// cylinder
                System.out.println("Enter the radius");
                radius =in.nextDouble();
                System.out.println("Enter the height");
                height= in.nextDouble();
                volume=pi*(radius*2)*height;
                System.out.println("volume of the cylinder =\t"+volume);
                break;
            case 3://cuboid
                System.out.println("Enter the length");
                length=in.nextDouble();
                System.out.println("Enter the width");
                width=in.nextDouble();
                System.out.println("Enter the height");
                height=in.nextDouble();
                volume=length*width*height;
                System.out.println("volume of the cuboid =\t"+volume);
                break;
            case 4://sphere
                System.out.println("Enter the radius");
                radius =in.nextDouble();
                volume = (4 * pi * (radius * 3)) / 3;
                System.out.println("the volume of the sphere =\t"+volume);
                break;
            case 5://cone
                System.out.println("Enter the height");
                height=in.nextDouble();
                System.out.println("Enter the radius");
                radius=in.nextDouble();
                volume=(pi * (radius * 2) * height) / 3;
                System.out.println("volume of the cone =\t"+volume);
                break;
            case 6:
                System.out.println("Enter the base");
                base=in.nextDouble();
                System.out.println("Enter the height");
                height=in.nextDouble();
                volume = (base*height)/3;
                System.out.println("volume of the pyramid =\t"+volume);
                break;
            default:
                System.out.println("You have entered the wrong option \\n the program terminates \\n bye!!!!!!");
                break;

        }
in.close();
    }
}
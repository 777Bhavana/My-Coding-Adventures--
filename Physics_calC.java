import java.util.Scanner;
class physics {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        System.out.println('\u000C');
        System.out.println("what kind of scientific calC do you need");
        System.out.println("enter the quantities from the standard formula only");
        System.out.println("and in SI units ONLY");
        System.out.println("enter 1 for area");
        System.out.println("enter 2 for volume");//
        System.out.println("enter 3 for speed/velocity");//
        System.out.println("enter 4 for force[m*a]");//
        System.out.println("enter 5 for acceleration");//
        System.out.println("enter 6 for density ");//
        System.out.println("enter 7 for work");//
        System.out.println("enter 8 for linear momentum ");//
        System.out.println("enter 9 for torque ");//
        System.out.println("enter 10 for power ");
        System.out.println("enter 11 for pressure");
        System.out.println("enter 12 for frequency");
        System.out.println("enter 13 for electric charge");
        System.out.println("enter 14 for Electromotive Force");
        System.out.println("enter 15 electrical power");
        int c = in.nextInt();
        switch (c)
        {
            case 1://area
                int l,b,ar;
                System.out.println("enter the length");
                l=in.nextInt();
                System.out.println("enter the breadth");
                b=in.nextInt();
                ar=l*b;
                System.out.println("area of the rectangle="+ar);System.out.print("m^2");
                break;
            case 2://volume
                int h,v,L,B;
                System.out.println("enter the length");
                L= in.nextInt();
                System.out.println("enter the breadth");
                B= in.nextInt();
                System.out.println("enter the height");
                h= in.nextInt();
                v=L*B*h;
                System.out.println("volume ="+v);System.out.print("m^3");
                break;
            case 3://speed/velocity
                int d,t,S;
                System.out.println("enter the distance");
                d=in.nextInt();
                System.out.println("enter the time taken");
                t= in.nextInt();
                S=d/t;
                System.out.println("speed/velocity ="+S);System.out.print("m/s");
                break;
            case 4://force
                int f,M,A;
                System.out.println("enter the MASS of the body ");
                M= in.nextInt();
                System.out.println("enter the Acceleration");
                A= in.nextInt();
                f=M*A;
                System.out.print("force ="+f);System.out.print("N");
                break;
            case 5://acceleration
                int V,T,a;
                System.out.println("enter the velocity");
                V= in.nextInt();
                System.out.println("enter the time taken");
                T= in.nextInt();
                a=V/T;
                System.out.println("acceleration ="+a);System.out.print("m/s^2");
                break;
            case 6://density
                int m,o,D;
                System.out.println("enter the mass ");
                m= in.nextInt();
                System.out.println("enter the volume ");
                o= in.nextInt();
                D=m/o;
                System.out.println("density= "+D);System.out.print("kgm/s^2");
                break;
            case 7: //work
                int W,q;
                System.out.println("enter the mass ");
                m= in.nextInt();
                System.out.print("enter displacement ");
                q= in.nextInt();
                W=m*q;
                System.out.println("work ="+W);
                break;
            case 8://momentum
                int r,z,p;
                System.out.println("enter the mass ");
                r= in.nextInt();
                System.out.println("enter the velocity");
                z= in.nextInt();
                p=z*r;
                System.out.println("linear momentum="+p);System.out.print("kgm/s^1");
                break;
            case 9://torque
                int e,y,O;
                System.out.println("enter the force ");
                e= in.nextInt();
                System.out.println("enter the distance ");
                y= in.nextInt();
                O=e*y;
                System.out.println("torque="+O);System.out.print("Nm");
                break;
            case 10:
                int k,w,g;
                System.out.println("enter the work ");
                w= in.nextInt();
                System.out.println("enter the time ");
                g= in.nextInt();
                k=w/g;
                System.out.println("power="+k);System.out.print("Js^1 or W");
                break;

            case 11:
                int fw ,ao,pc;
                System.out.println("enter the force");
                fw=in.nextInt();
                System.out.println("enter the area");
                ao=in.nextInt();
                pc=fw/ao;
                System.out.println("your pressure ="+pc+"kgm/s");
                break;

            case 12:
                int fo,ti;
                System.out.println("enter the time period ");
                ti=in.nextInt();
                fo=1/ti;
                System.out.println("frequency ="+fo+"Hz");
                break;

            case 13:
                int ec,cge,tm;
                System.out.println("enter the charge");
                cge=in.nextInt();
                System.out.println("enter the time");
                tm=in.nextInt();
                ec=cge*tm;
                System.out.println("electric charge ="+ec+"A");
                break;

            case 14:
                int emf,wo,cg;
                System.out.println("enter the work");
                wo=in.nextInt();
                System.out.println("enter the charge");
                cg=in.nextInt();
                emf=wo/cg;
                System.out.println("Electric Potential="+emf+"V");
                break;

            case 15:
                int ep,pn,cu;
                System.out.println("enter the potential of current");
                pn=in.nextInt();
                System.out.println("enter the current");
                cu=in.nextInt();
                ep=pn*cu;
                System.out.println("electric power="+ep+"W");
                break;


            default:
                System.out.println("please read the instructions properly and enter");
        }
in.close();
    }
}
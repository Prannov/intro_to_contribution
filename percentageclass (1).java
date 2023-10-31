import java.util.Scanner;
public class  percentageclass{
    public static void main(String[] args){

//        Scanner scan = new Scanner(System.in);
        Scanner scan = new Scanner(System.in);
        System.out.println(" enter your mathematics marks : ");
        int mathematics = scan.nextInt();
        System.out.println(" enter your physics marks : ");
        int physics = scan.nextInt();
        System.out.println(" enter your chemistry marks : ");
        int chemistry = scan.nextInt();
        System.out.println(" enter your biology marks : ");
        int biology = scan.nextInt() ;
        System.out.println(" enter your economics marks : ");
        int economics = scan.nextInt();

        float percentage = (( mathematics + physics + chemistry + biology + economics )/500.0f)*100;

        System.out.println("percentage :  ");
        System.out.println(percentage);



    }
}
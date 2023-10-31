import java.util.Scanner;
public class Series{
    public static void main(String[] args){
        float sum = 0;
        int n;
        System.out.println("enter the no of terms : ");
        Scanner scn = new Scanner("System.in");
        n = scn.nextInt();
        while(n>0){
            sum = sum +(float)1/n;
            n--;

        }
        System.out.println(+sum);
    }
}

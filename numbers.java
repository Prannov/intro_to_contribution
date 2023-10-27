import java.util.*;
class xyz
{
   
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter any number to check if it is prime or not");
        int n=sc.nextInt();
        boolean  flag=true;
        for(i=2;i<n/2;i++)
        {
           if(n%i==0)
           {
            flag=false;
            break;
           }
        }
    System.out.println(flag);
    }
}
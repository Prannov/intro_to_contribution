class base{
    public int a;
    public int getA(){
        return a;

    }
    public void setA(int i){
        a=i;
    }

}
class derived extends base{
    public int b;
    public int getB(){
        return b;
    }
    public void setB(int j){
        b=j;
    }
}

public class inheritance {
    public static void main(String[] args) {
        base a1=new base();
        a1.setA(23);
        System.out.println(a1.getA());
        derived a2=new derived();
        a2.setA(34);
        System.out.println(a2.getA());
    }
}

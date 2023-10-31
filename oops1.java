interface sample{
    void paper();
    void paper2();
}
interface sample2 extends sample{
    void paper3();
    void paper4();
}
class que implements sample2{
    public void paper(){
        System.out.println("paper");
    }
    public void paper2() {
        System.out.println("paper");
    }
    public void paper3() {
        System.out.println("paper");
    }
    public void paper4() {
        System.out.println("paper");
    }
}

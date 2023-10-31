class function{
    private int id;
    private String name;
    public function(String myName,int myId){
        id=myId;
        name=myName;
    }
    public int getId(){
        return id;
    }
    public void setId(int a){
        id=a;
    }
    public String getName(){
        return name;
    }
    public void setName(String n){
        name =n;
    }

}



public class constructer {
    public static void main(String[] args) {
        function emp=new function("shivasai",38);
        System.out.println(emp.getId());
        System.out.println(emp.getName());
    }
}

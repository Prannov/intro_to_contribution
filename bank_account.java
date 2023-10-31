class staff{
String codename;
staff (String codename){
this.codename=codename;
}
public String getinfo(){
return "Codename: "+this.codename;
}}
class Teacher extends staff{
String subject;
String publication;
Teacher (String codename,String subject,String publication){
super (codename);
this.subject=subject;
this.publication=publication;
}
public String getinfo(){
return super.getinfo()+" Subject:"+this.subject+" publication:"+this.publication;
}}
class Typist extends staff{
float speed;
Typist (String codename, float speed){
super (codename);
this.speed=speed;
}
public String getinfo(){
return super.getinfo()+" Speed:"+this.speed;
}}
class staff1 extends Typist{
staff1 (String codename, float speed) {super (codename,speed) ;}
public String getinfo() {return super.getinfo();}
}
class staff2 extends Typist{
staff2 (String codename, float speed){
super (codename,speed);
}
public String getinfo() {return super.getinfo();}
}
class Officer extends staff{
Character Grade;
Officer (String codename,Character g){
super (codename);
this.Grade=g;
}
public String getinfo(){
return super.getinfo()+" Grade:"+this.Grade;
}}
public class lab4_Q3{
public static void main(String[] args){
teacher teacher = new Teacher ("luffy", "OOPS", "MUJ Publications"),
Typist typist=new Typist ("nami", 69);
officer officer = new Officer ("zoro", 'A');
System.out.println(teacher.getinfo());
System.out.println(typist.getinfo());
system.out.println(officer.getinfo());
}}
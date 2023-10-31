import java.util.Scanner;

class Staff {
    protected int code;
    protected String name;

    public void setdata() {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the code : ");
        code = input.nextInt();
        System.out.println("Enter the name : ");
        name = input.next();
    }
}

class Teacher extends Staff {
    private String sub;
    private String publication;

    public void getdata() {
        setdata();
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the subject of teacher : ");
        sub = input.next();
        System.out.println("Enter the publication : ");
        publication = input.next();
    }

    public void showdata() {
        System.out.println("Code            : " + code);
        System.out.println("Name of teacher : " + name);
        System.out.println("Subject of teacher  : " + sub);
        System.out.println("Publication of teacher  : " + publication);
    }
}

class Officer extends Staff {
    private char grade;

    public void getdata() {
        setdata();
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the grade of officer (A, B, C, D): ");
        grade = input.next().charAt(0);
    }

    public void showdata() {
        System.out.println("Code             : " + code);
        System.out.println("Name of officer  : " + name);
        System.out.println("Grade of officer : " + grade);
    }
}

class Typist extends Staff {
    protected int speed;

    public void getdata() {
        setdata();
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the speed of typing in wps: ");
        speed = input.nextInt();
    }

    public void showdata() {
        System.out.println("Code            : " + code);
        System.out.println("Name of typist  : " + name);
        System.out.println("Speed of typist : " + speed + " wps");
    }
}

class Regular extends Typist {
    // No additional fields or methods for Regular typist
}

class Casual extends Typist {
    private int dailyWages;

    public void set() {
        getdata();
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the daily wages of casual typist: ");
        dailyWages = input.nextInt();
    }

    public void display() {
        showdata();
        System.out.println("Daily wages of casual typist: " + dailyWages + " Rs.");
    }
}

public class DatabaseofEmployees {
    public static void main(String[] args) {
        Staff member;
        Scanner input = new Scanner(System.in);
        int i;
        System.out.println("Choose any staff member: ");
        System.out.println("1. Teacher");
        System.out.println("2. Officer");
        System.out.println("3. Typist");
        i = input.nextInt();
        if (i == 1) {
            Teacher mem = new Teacher();
            mem.getdata();
            mem.showdata();
        } else if (i == 2) {
            Officer mem = new Officer();
            mem.getdata();
            mem.showdata();
        } else if (i == 3) {
            Typist mem = new Typist();
            int t;
            System.out.println("Choose typist type: ");
            System.out.println("1. Regular");
            System.out.println("2. Casual");
            t = input.nextInt();
            if (t == 1) {
                Regular m = new Regular();
                m.getdata();
                m.showdata();
            } else if (t == 2) {
                Casual m = new Casual();
                m.set();
                m.display();
            }
        }
    }
}
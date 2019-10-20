import Domain.Activity;
import Domain.Discipline;
import Domain.Teacher;

public class Main {
    public static void main(String[] args) {
        Teacher Teacher1 = new Teacher("Teacher1");
        Activity Activity1 = new Activity("Activity1");
        Discipline Discipline1 = new Discipline("Discipline1");
        System.out.println(Teacher1.getName());
        System.out.println(Activity1.getName());
        System.out.println(Discipline1.getName());
    }
}

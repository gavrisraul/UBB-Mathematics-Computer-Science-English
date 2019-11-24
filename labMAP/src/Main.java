import Domain.Teacher;
import Repository.DatabaseIORepository;

public class Main {

    public static void main(String[] args) throws Exception {
//        Ui app = new Ui();
//        app.start();
        Teacher teacher = new Teacher("TESTTEST");

        DatabaseIORepository<Teacher> db = new DatabaseIORepository<Teacher>((Class<Teacher>) teacher.getClass());
        db.initializeDB((Class<Teacher>) teacher.getClass());
        db.add(teacher, 0, "raul1");
        db.add(teacher, 1, "raul2");
        db.add(teacher, 2, "raul3");
        db.add(teacher, 3, "raul4");
        db.add(teacher, 4, "raul5");
        System.out.println(db.getByIndex(teacher, 2));
        System.out.println(db.getAllData(teacher));
        System.out.println(db.setAtIndex(teacher, 4, "aaaa"));
        System.out.println(db.deleteAtIndex(teacher, 3));
        System.out.println(db.getAllData(teacher));

//        FileIORepository<Teacher> teacherRepository;
//        teacherRepository =  new FileIORepository<Teacher>(Teacher.class, "/home/rg/IdeaProjects/labMAP/src/FilesIO/Teacher.csv");
//        System.out.println(teacherRepository.getAllData());
//        teacherRepository.add(teacher);
//        System.out.println(teacherRepository.getAllData());

//        Repository<Teacher> teacherRepository = new Repository<Teacher>();
//        teacherRepository.addNew(teacher);
//        System.out.println(teacherRepository.getAllData());
    }
}

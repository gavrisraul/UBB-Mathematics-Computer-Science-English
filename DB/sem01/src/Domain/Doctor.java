package Domain;

public class Doctor extends Entity {
    private static String name;
    private static String speciality;
    private static String location;
    public Doctor(int id, String name, String speciality, String location) {
        super(id);
        this.name = name;
        this.speciality = speciality;
        this.location = location;
    }
}

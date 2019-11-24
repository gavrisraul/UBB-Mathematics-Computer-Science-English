package Controller;

import Domain.*;
import Repository.*;

import java.lang.reflect.InvocationTargetException;
import java.sql.SQLException;
import java.util.ArrayList;

public class Controller {

    // Database
    private DatabaseIORepository<Teacher> teacherDBRepository;
    private DatabaseIORepository<Discipline> disciplineDBRepository;

    // File
    private FileIORepository<Activity> activityRepository;
    private FileIORepository<Discipline> disciplineRepository;
    private FileIORepository<Formation> formationRepository;
    private FileIORepository<Room> roomRepository;
    private FileIORepository<Teacher> teacherRepository;

    // Memory
    private Repository<Relation> teacherActivityRelation;
    private Repository<Relation> formationActivityRelation;
    private Repository<Relation> roomActivityRelation;

    public Controller() throws Exception {
        this.teacherDBRepository = new DatabaseIORepository<Teacher>(Teacher.class);
        this.disciplineDBRepository = new DatabaseIORepository<Discipline>(Discipline.class);

        this.activityRepository = new FileIORepository<Activity>(Activity.class, "/home/rg/IdeaProjects/labMAP/src/FilesIO/Activity.csv");
        this.disciplineRepository = new FileIORepository<Discipline>(Discipline.class, "/home/rg/IdeaProjects/labMAP/src/FilesIO/Discipline.csv");
        this.formationRepository = new FileIORepository<Formation>(Formation.class, "/home/rg/IdeaProjects/labMAP/src/FilesIO/Formation.csv");
        this.roomRepository = new FileIORepository<Room>(Room.class, "/home/rg/IdeaProjects/labMAP/src/FilesIO/Room.csv");
        this.teacherRepository = new FileIORepository<Teacher>(Teacher.class, "/home/rg/IdeaProjects/labMAP/src/FilesIO/Teacher.csv");

        this.teacherActivityRelation = new Repository<Relation>();
        this.formationActivityRelation = new Repository<Relation>();
        this.roomActivityRelation = new Repository<Relation>();
    }

    public void addActivity(String a2, String name) {
        Activity newActivity = new Activity(name);
        this.activityRepository.add(newActivity);
    }

    public void addDiscipline(String name) {
        Discipline newDiscipline = new Discipline(name);
        this.disciplineRepository.add(newDiscipline);
    }

    public void addFormation(String name) {
        Formation newFormation = new Formation(name);
        this.formationRepository.add(newFormation);
    }

    public void addRoom(String name) {
        Room newRoom = new Room(name);
        this.roomRepository.add(newRoom);
    }

    public void addTeacher(String name) {
        Teacher newTeacher = new Teacher(name);
        this.teacherRepository.add(newTeacher);
    }

    public void addTeacherActivityRelation(String first, String second) {
        Relation newRelation = new Relation(first, second);
        this.teacherActivityRelation.addNew(newRelation);
    }

    public void addFormationActivityRelation(String first, String second) {
        Relation newRelation = new Relation(first, second);
        this.formationActivityRelation.addNew(newRelation);
    }

    public void addRoomActivityRelation(String first, String second) {
        Relation newRelation = new Relation(first, second);
        this.roomActivityRelation.addNew(newRelation);
    }

    public ArrayList<Activity> getAllActivities() {
        return this.activityRepository.getAllData();
    }

    public ArrayList<Discipline> getAllDisciplines() {
        return this.disciplineRepository.getAllData();
    }

    public ArrayList<Formation> getAllFormations() {
        return this.formationRepository.getAllData();
    }

    public ArrayList<Room> getAllRooms() {
        return this.roomRepository.getAllData();
    }

    public ArrayList<Teacher> getAllTeachers() {
        return this.teacherRepository.getAllData();
    }

    public ArrayList<Relation> getAllTeacherActivityRelations() {
        return this.teacherActivityRelation.getAllData();
    }

    public ArrayList<Relation> getAllFormationActivityRelations() {
        return this.formationActivityRelation.getAllData();
    }

    public ArrayList<Relation> getAllRoomActivityRelations() {
        return this.roomActivityRelation.getAllData();
    }

    public Activity getActivityByIndex(int index) {
        return this.activityRepository.getByIndex(index);
    }

    public Discipline getDisciplineByIndex(int index) {
        return this.disciplineRepository.getByIndex(index);
    }

    public Formation getFormationByIndex(int index) {
        return this.formationRepository.getByIndex(index);
    }

    public Room getRoomByIndex(int index) {
        return this.roomRepository.getByIndex(index);
    }

    public Teacher getTeacherByIndex(int index) {
        return this.teacherRepository.getByIndex(index);
    }

    public Relation getTeacherActivityRelationByIndex(int index) {
        return this.teacherActivityRelation.getByIndex(index);
    }

    public Relation getFormationActivityRelationByIndex(int index) {
        return this.formationActivityRelation.getByIndex(index);
    }

    public Relation getRoomActivityRelationByIndex(int index) {
        return this.roomActivityRelation.getByIndex(index);
    }

    public void updateActivityByIndex(int index, String name) {
        Activity currentActivity = this.activityRepository.getByIndex(index);
        currentActivity.setName(name);
        this.activityRepository.setAtIndex(currentActivity, index);
    }

    public void updateDisciplineByIndex(int index, String name) {
        Discipline currentDiscipline = this.disciplineRepository.getByIndex(index);
        currentDiscipline.setName(name);
        this.disciplineRepository.setAtIndex(currentDiscipline, index);
    }

    public void updateFormationByIndex(int index, String name) {
        Formation currentFormation = this.formationRepository.getByIndex(index);
        currentFormation.setName(name);
        this.formationRepository.setAtIndex(currentFormation, index);
    }

    public void updateRoomByIndex(int index, String name) {
        Room currentRoom = this.roomRepository.getByIndex(index);
        currentRoom.setName(name);
        this.roomRepository.setAtIndex(currentRoom, index);
    }

    public void updateTeacherByIndex(int index, String name) {
        Teacher currentTeacher = this.teacherRepository.getByIndex(index);
        currentTeacher.setName(name);
        this.teacherRepository.setAtIndex(currentTeacher, index);
    }

    public void updateTeacherToActivityRelationByIndex(int index, String first, String second) {
        Relation currentRelation = this.teacherActivityRelation.getByIndex(index);
        currentRelation.setFirst(first);
        currentRelation.setSecond(second);
        this.teacherActivityRelation.setAtIndex(currentRelation, index);
    }

    public void updateFormationToActivityRelationByIndex(int index, String first, String second) {
        Relation currentRelation = this.formationActivityRelation.getByIndex(index);
        currentRelation.setFirst(first);
        currentRelation.setSecond(second);
        this.formationActivityRelation.setAtIndex(currentRelation, index);
    }

    public void updateRoomToActivityRelationByIndex(int index, String first, String second) {
        Relation currentRelation = this.roomActivityRelation.getByIndex(index);
        currentRelation.setFirst(first);
        currentRelation.setSecond(second);
        this.roomActivityRelation.setAtIndex(currentRelation, index);
    }

    public void deleteActivity(int index) {
        this.disciplineRepository.deleteAtIndex(index);
    }

    public void deleteDiscipline(int index) {
        this.activityRepository.deleteAtIndex(index);
    }

    public void deleteFormation(int index) {
        this.formationRepository.deleteAtIndex(index);
    }

    public void deleteTeacher(int index) {
        this.teacherRepository.deleteAtIndex(index);
    }

    public void deleteTeacherActivityRelation(int index) {
        this.teacherActivityRelation.deleteAtIndex(index);
    }

    public void deleteFormationActivityRelation(int index) {
        this.formationActivityRelation.deleteAtIndex(index);
    }

    public void deleteRoomActivityRelation(int index) {
        this.formationActivityRelation.deleteAtIndex(index);
    }

    public void addDisciplineDB(Discipline newDiscipline, int id, String name) throws SQLException, ClassNotFoundException, NoSuchMethodException, InstantiationException, IllegalAccessException, InvocationTargetException {
        this.disciplineDBRepository.add(newDiscipline, id, name);
    }

    public void addTeacherDB(Teacher newTeacher, int id, String name) throws SQLException, ClassNotFoundException, NoSuchMethodException, InstantiationException, IllegalAccessException, InvocationTargetException {
        this.teacherDBRepository.add(newTeacher, id, name);
    }

    public void getAllDisciplineDB(Discipline newDiscipline) throws SQLException, InvocationTargetException, ClassNotFoundException, InstantiationException, NoSuchMethodException, IllegalAccessException {
        this.disciplineDBRepository.getAllData(newDiscipline);
    }

    public void getAllTeachersDB(Teacher newTeacher) throws SQLException, InvocationTargetException, ClassNotFoundException, InstantiationException, NoSuchMethodException, IllegalAccessException {
        this.teacherDBRepository.getAllData(newTeacher);
    }

    public void getDisciplineByIndexDB(Discipline newDiscipline, int index) throws SQLException {
        this.disciplineDBRepository.getByIndex(newDiscipline, index);
    }

    public void getTeacherByIndexDB(Teacher newTeacher, int index) throws SQLException {
        this.teacherDBRepository.getByIndex(newTeacher, index);
    }

    public void setDisciplineAtIndexDB(Discipline newDiscipline, int index, String name) throws SQLException, ClassNotFoundException, NoSuchMethodException, InstantiationException, IllegalAccessException, InvocationTargetException {
        this.disciplineDBRepository.setAtIndex(newDiscipline, index, name);
    }

    public void setTeacherAtIndexDB(Teacher newTeacher, int index, String name) throws SQLException, ClassNotFoundException, NoSuchMethodException, InstantiationException, IllegalAccessException, InvocationTargetException {
        this.teacherDBRepository.setAtIndex(newTeacher, index, name);
    }

    public void deleteDisciplineAtIndexDB(Discipline newDiscipline, int index) throws SQLException, ClassNotFoundException, NoSuchMethodException, InstantiationException, IllegalAccessException, InvocationTargetException {
        this.disciplineDBRepository.deleteAtIndex(newDiscipline, index);
    }

    public void deleteTeacherAtIndexDB(Teacher newTeacher, int index) throws SQLException, ClassNotFoundException, NoSuchMethodException, InstantiationException, IllegalAccessException, InvocationTargetException {
        this.teacherDBRepository.deleteAtIndex(newTeacher, index);
    }


//    public ArrayList<Teacher> getSortedTeachersByRank(String rank) {
//        ArrayList<Teacher> teachers = this.teacherRepo.getAllEntries();
//
//        System.out.printf("%d\n", teachers.size());
//        teachers.stream()
//                .filter(t -> t.getRank() == rank)
//                .sorted(Comparator.comparing(Teacher::getName)).forEach(System.out::println);
//
//
//        Stream<Teacher> teacherStream = teachers.stream()
//                .filter(t -> t.getRank() == rank)
//                .sorted(Comparator.comparing(Teacher::getName));
//
//        ArrayList<Teacher> result = new ArrayList<Teacher>();
//        teacherStream.forEach(result::add);
//
//        return result;
//    }
}

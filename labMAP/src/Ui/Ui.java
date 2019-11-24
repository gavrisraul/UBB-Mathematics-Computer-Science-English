package Ui;

import Controller.Controller;
import Domain.*;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Ui {

    private Controller controller;
    private Scanner reader;

    public Ui() throws Exception {
        this.controller = new Controller();
        this.reader = new Scanner(System.in);
    }

    private int getNextOption(ArrayList<String> optionList) {
        int minOption = 0;
        int maxOption = optionList.size();
        int choice = -1;

        while (choice < minOption || choice > maxOption) {
            System.out.println("Option:");

            for (int i = 0; i < optionList.size(); i++) {
                System.out.printf("\t%d - %s\n", i, optionList.get(i));
            }

            choice = this.reader.nextInt();
            if (choice < minOption || choice > maxOption) {
                System.out.println("Invalid option!");
            }
        }

        return choice;
    }

    private void addTeacher() {
        this.reader.nextLine();

        System.out.println("\tNew teacher name:");
        String name = this.reader.nextLine();

        this.controller.addTeacher(name);
    }

    private void addActivity() {
        this.reader.nextLine();
        System.out.println("\tNew activity name:");
        String name = this.reader.nextLine();

        this.reader.nextLine();
        System.out.println("\tNew activity teacher_name:");
        String teacher_name = this.reader.nextLine();

        this.controller.addActivity(name, teacher_name);
    }

    private void addDiscipline() {
        this.reader.nextLine();

        System.out.println("\tNew discipline name:");
        String name = this.reader.nextLine();

        this.controller.addDiscipline(name);
    }

    private void create() {
        ArrayList<String> optionList = new ArrayList<>(
                Arrays.asList(
                        "back", "add teacher", "add activity", "add discipline")
        );

        int choice = this.getNextOption(optionList);
        while (choice != 0) {
            switch (choice) {
                case 1:
                    this.addTeacher();
                    break;
                case 2:
                    this.addActivity();
                    break;
                case 3:
                    this.addDiscipline();
                    break;
            }
            choice = this.getNextOption(optionList);
        }
    }

    private void getAllTeachers() {
        ArrayList<Teacher> teacherList = this.controller.getAllTeachers();

        for (int i=0; i<teacherList.size(); i++) {
            System.out.printf("\t%d - %s\n", i, teacherList.get(i));
        }
    }

    private void getTeacherByIndex() {
        this.reader.nextLine();

        System.out.println("Teacher index: ");
        int index = this.reader.nextInt();

        Teacher entry = this.controller.getTeacherByIndex(index);

        System.out.printf("\t%s", entry);
    }

    private void getTeachers() {
        ArrayList<String> optionList = new ArrayList<>(
                Arrays.asList(
                        "back", "get all teachers", "get teacher by index")
        );

        int choice = this.getNextOption(optionList);
        while (choice != 0) {
            switch (choice) {
                case 1:
                    this.getAllTeachers();
                    break;
                case 2:
                    this.getTeacherByIndex();
                    break;
            }
            choice = this.getNextOption(optionList);
        }
    }

    private void getAllActivities() {
        ArrayList<Activity> activityList = this.controller.getAllActivities();

        for (int i=0; i<activityList.size(); i++) {
            System.out.printf("\t%d - %s\n", i, activityList.get(i));
        }
    }

    private void getActivityByIndex() {
        this.reader.nextLine();

        System.out.println("Activity index: ");
        int index = this.reader.nextInt();

        Activity entry = this.controller.getActivityByIndex(index);

        System.out.printf("\t%s", entry);
    }

    private void getActivities() {
        ArrayList<String> optionList = new ArrayList<>(
                Arrays.asList(
                        "back", "get all activities", "get activity by index")
        );

        int choice = this.getNextOption(optionList);
        while (choice != 0) {
            switch (choice) {
                case 1:
                    this.getAllActivities();
                    break;
                case 2:
                    this.getActivityByIndex();
                    break;
            }
            choice = this.getNextOption(optionList);
        }
    }

    private void getAllDisciplines() {
        ArrayList<Discipline> disciplineList = this.controller.getAllDisciplines();

        for (int i=0; i<disciplineList.size(); i++) {
            System.out.printf("\t%d - %s\n", i, disciplineList.get(i));
        }
    }

    private void getDisciplineByIndex() {
        this.reader.nextLine();

        System.out.println("Discipline index: ");
        int index = this.reader.nextInt();

        Discipline entry = this.controller.getDisciplineByIndex(index);

        System.out.printf("\t%s", entry);
    }

    private void getDisciplines() {
        ArrayList<String> optionList = new ArrayList<>(
                Arrays.asList(
                        "back", "get all disciplines", "get discipline by index")
        );

        int choice = this.getNextOption(optionList);
        while (choice != 0) {
            switch (choice) {
                case 1:
                    this.getAllDisciplines();
                    break;
                case 2:
                    this.getDisciplineByIndex();
                    break;
            }
            choice = this.getNextOption(optionList);
        }
    }

    private void read() {
        ArrayList<String> optionList = new ArrayList<>(
                Arrays.asList(
                        "back", "get teachers", "get activities", "get disciplines")
        );

        int choice = this.getNextOption(optionList);
        while (choice != 0) {
            switch (choice) {
                case 1:
                    this.getTeachers();
                    break;
                case 2:
                    this.getActivities();
                    break;
                case 3:
                    this.getDisciplines();
                    break;
            }
            choice = this.getNextOption(optionList);
        }
    }

    private void updateTeacher() {
        this.reader.nextLine();

        System.out.println("Teacher index to update: ");
        int index = this.reader.nextInt();

        this.reader.nextLine();
        System.out.println("New teacher name");
        String name = this.reader.nextLine();

        this.controller.updateTeacherByIndex(index, name);
        System.out.printf("Updated teacher at %d!", index);
    }

    private void updateActivity() {
        this.reader.nextLine();

        System.out.println("Activity index to update: ");
        int index = this.reader.nextInt();

        this.reader.nextLine();
        System.out.println("New activity name");
        String name = this.reader.nextLine();

        this.controller.updateActivityByIndex(index, name);
        System.out.printf("Updated activity at %d!", index);
    }

    private void updateDiscipline() {
        this.reader.nextLine();

        System.out.println("Enter discipline index to update: ");
        int index = this.reader.nextInt();

        this.reader.nextLine();
        System.out.println("New discipline name");
        String name = this.reader.nextLine();

        this.controller.updateDisciplineByIndex(index, name);
        System.out.printf("Updated discipline at %d!", index);
    }

    private void update() {
        ArrayList<String> optionList = new ArrayList<>(
                Arrays.asList(
                        "back", "update teacher", "update activity", "update discipline")
        );

        int choice = this.getNextOption(optionList);
        while (choice != 0) {
            switch (choice) {
                case 1:
                    this.updateTeacher();
                    break;
                case 2:
                    this.updateActivity();
                    break;
                case 3:
                    this.updateDiscipline();
                    break;
            }
            choice = this.getNextOption(optionList);
        }
    }

    private void deleteTeacher() {
        this.reader.nextLine();

        System.out.println("Enter teacher index to delete: ");
        int index = this.reader.nextInt();

        this.controller.deleteTeacher(index);
    }

    private void deleteActivity() {
        this.reader.nextLine();

        System.out.println("Activity index to delete: ");
        int index = this.reader.nextInt();

        this.controller.deleteActivity(index);
    }

    private void deleteDiscipline() {
        this.reader.nextLine();

        System.out.println("Discipline index to delete: ");
        int index = this.reader.nextInt();

        this.controller.deleteDiscipline(index);
    }

    private void delete() {
        ArrayList<String> optionList = new ArrayList<>(
                Arrays.asList(
                        "back", "delete teacher", "delete activity", "delete discipline")
        );

        int choice = this.getNextOption(optionList);
        while (choice != 0) {
            switch (choice) {
                case 1:
                    this.deleteTeacher();
                    break;
                case 2:
                    this.deleteActivity();
                    break;
                case 3:
                    this.deleteDiscipline();
                    break;
            }
            choice = this.getNextOption(optionList);
        }
    }

    public void start() {
        this.controller.addTeacher("T1");
        this.controller.addTeacher("T2");
        this.controller.addTeacher("T3");
        this.controller.addTeacher("T4");
        this.controller.addTeacher("T5");

        this.controller.addDiscipline("D1");
        this.controller.addDiscipline("D2");
        this.controller.addDiscipline("D3");
        this.controller.addDiscipline("D4");
        this.controller.addDiscipline("D5");

        this.controller.addActivity("A1", "T1");
        this.controller.addActivity("A2", "T1");
        this.controller.addActivity("A2", "T2");
        this.controller.addActivity("A3", "T3");
        this.controller.addActivity("A4", "T5");

        ArrayList<String> optionList = new ArrayList<>(
                Arrays.asList(
                        "quit", "create", "read", "update", "delete")
        );

        int choice = this.getNextOption(optionList);
        while (choice != 0) {
            switch (choice) {
                case 1:
                    this.create();
                    break;
                case 2:
                    this.read();
                    break;
                case 3:
                    this.update();
                    break;
                case 4:
                    this.delete();
                    break;
            }
            choice = this.getNextOption(optionList);
        }
    }
}

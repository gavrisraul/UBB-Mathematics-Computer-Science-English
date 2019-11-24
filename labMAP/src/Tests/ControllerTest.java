package Tests;

import Controller.Controller;
import Domain.Teacher;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static org.junit.Assert.assertEquals;

class ControllerTest {

    private Controller controller;

    @BeforeEach
    void setUp() throws Exception {
        this.controller = new Controller();
        this.controller.addTeacher("data 0");
        this.controller.addTeacher("data 1");
        this.controller.addTeacher("data 2");
    }

    @Test
    void addTeacher() {
        this.controller.addTeacher("data 3");
        assertEquals("Should have data 3 on 3rd position", this.controller.getTeacherByIndex(3), "data 3");
    }

    @Test
    void getAllTeachers() {
        ArrayList<String> goodList = new ArrayList<String>();
        goodList.add("data 0");
        goodList.add("data 1");
        goodList.add("data 2");
        ArrayList<Teacher> list = this.controller.getAllTeachers();

        for (int i=0; i<goodList.size(); i++) {
            assertEquals(goodList.get(i), list.get(i).getName());
        }
    }

    @Test
    void getTeacherByIndex() {
        ArrayList<String> goodList = new ArrayList<String>();
        goodList.add("data 0");
        goodList.add("data 1");
        goodList.add("data 2");

        for (int i=0; i<goodList.size(); i++) {
            assertEquals(goodList.get(i), this.controller.getTeacherByIndex(i).getName());
        }
    }

    @Test
    void updateTeacherByIndex() {
        this.controller.updateTeacherByIndex(1, "test");
        assertEquals(this.controller.getTeacherByIndex(1).getName(), "test");
    }

    @Test
    void deleteTeacher() {
        this.controller.deleteTeacher(0);
        assertEquals(this.controller.getTeacherByIndex(0).getName(), "data 1");
        assertEquals(this.controller.getTeacherByIndex(1).getName(), "data 2");
    }
}

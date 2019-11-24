package Tests;

import Domain.Teacher;
import org.junit.Assert;
import org.junit.Test;

public class TeacherTest {

    public TeacherTest() {};

    @Test
    public void testAttributes() {
        Teacher entry = new Teacher("test1");
        Assert.assertEquals("Name should be test1", "test1", entry.getName());

        entry.setName("test2");
        Assert.assertEquals("Name should be test2", "test2", entry.getName());
    }
}
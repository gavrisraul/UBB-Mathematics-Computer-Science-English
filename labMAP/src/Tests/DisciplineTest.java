package Tests;

import Domain.Discipline;
import org.junit.Assert;
import org.junit.Test;

public class DisciplineTest {

    public DisciplineTest() {};

    @Test
    public void testAttributes() {
        Discipline entry = new Discipline("test1");
        Assert.assertEquals("Name should be test1", "test1", entry.getName());

        entry.setName("test2");
        Assert.assertEquals("Name should be test2", "test2", entry.getName());
    }
}
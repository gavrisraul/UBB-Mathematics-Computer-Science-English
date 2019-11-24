package Tests;

import Domain.Formation;
import org.junit.Assert;
import org.junit.Test;

public class FormationTest {

    public FormationTest() {};

    @Test
    public void testAttributes() {
        Formation entry = new Formation("test1");
        Assert.assertEquals("Name should be test1", "test1", entry.getName());

        entry.setName("test2");
        Assert.assertEquals("Name should be test2", "test2", entry.getName());
    }
}
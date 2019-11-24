package Tests;

import Domain.Activity;
import org.junit.Assert;
import org.junit.Test;

public class ActivityTest {

    public ActivityTest() {};

    @Test
    public void testAttributes() {
        Activity entry = new Activity("test1");
        Assert.assertEquals("Name should be test1", "test1", entry.getName());

        entry.setName("test2");
        Assert.assertEquals("Name should be test2", "test2", entry.getName());
    }
}
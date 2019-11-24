package Tests;

import Domain.Room;
import org.junit.Assert;
import org.junit.Test;

public class RoomTest {

    public RoomTest() {};

    @Test
    public void testAttributes() {
        Room entry = new Room("test1");
        Assert.assertEquals("Name should be test1", "test1", entry.getName());

        entry.setName("test2");
        Assert.assertEquals("Name should be test2", "test2", entry.getName());
    }
}
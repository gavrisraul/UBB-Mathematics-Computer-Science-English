//package Tests;
//
//import org.junit.jupiter.api.BeforeEach;
//import Repository.Repository;
//import static org.junit.Assert.*;
//import org.junit.Test;
//
//import java.util.ArrayList;
//
//class RepositoryTest {
//
//    private Repository<String> stringRepo;
//
//    @BeforeEach
//    void setUp() {
//        this.stringRepo = new Repository<String>();
//        this.stringRepo.addNew("Entry 0");
//        this.stringRepo.addNew("Entry 1");
//        this.stringRepo.addNew("Entry 2");
//    }
//
//    @Test
//    public void addEntry() {
//        this.stringRepo.addNew("Entry 3");
//        assertEquals("Should have entry 3 on 3rd position", this.stringRepo.getByIndex(3), "Entry 3");
//    }
//
//    @Test
//    public void getAllEntries() {
//        ArrayList<String> goodList = new ArrayList<String>();
//        goodList.add("Entry 0");
//        goodList.add("Entry 1");
//        goodList.add("Entry 2");
//        ArrayList<String> list = this.stringRepo.getAllData();
//
//        for (int i=0; i<goodList.size(); i++) {
//            assertEquals(goodList.get(i), list.get(i));
//        }
//    }
//
//    @Test
//    public void getByIndex() {
//        ArrayList<String> goodList = new ArrayList<String>();
//        goodList.add("Entry 0");
//        goodList.add("Entry 1");
//        goodList.add("Entry 2");
//
//        for (int i=0; i<goodList.size(); i++) {
//            assertEquals(goodList.get(i), this.stringRepo.getByIndex(i));
//        }
//    }
//
//    @Test
//    public void setAtIndex() {
//        this.stringRepo.setAtIndex("Dummy", 1);
//        assertEquals(this.stringRepo.getByIndex(1), "Dummy");
//    }
//
//    @Test
//    public void deleteIndex() {
//        this.stringRepo.deleteAtIndex(0);
//        assertEquals(this.stringRepo.getByIndex(0), "Entry 1");
//        assertEquals(this.stringRepo.getByIndex(1), "Entry 2");
//    }
//}
package Repository;

import Domain.BaseObject;

import java.util.ArrayList;

public class Repository<CustomObject extends BaseObject> {

    private ArrayList<CustomObject> dataList = new ArrayList<CustomObject>();

    public boolean addNew(CustomObject newData) {
        this.dataList.add(newData);
        return true;
    }

    public ArrayList<CustomObject> getAllData() {
        return this.dataList;
    }

    public CustomObject getByIndex(int index) {
        return this.dataList.get(index);
    }

    public boolean setAtIndex(CustomObject newObject, int index) {
        this.dataList.set(index, newObject);
        return true;
    }

    public boolean deleteAtIndex(int index) {
        this.dataList.remove(index);
        return true;
    }
}

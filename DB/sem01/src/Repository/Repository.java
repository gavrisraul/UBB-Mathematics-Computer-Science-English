package Repository;

import Domain.Entity;

import java.util.ArrayList;


public class Repository<T extends Entity> implements IRepository<T> {
    private ArrayList<Entity> entities = new ArrayList<>();

    public Repository() {
        this.entities = entities;
    }

    public static void add(ArrayList<Entity> entities, Entity entity) {
        entities.add(entity);
    }

    public static int remove(ArrayList<Entity> entities, Entity entity) {
        entities.remove(entity);
        return 1;
    }

    public static int find(ArrayList<Entity> entities, Entity entity) {
        if (entities.indexOf(entity) != -1) {
            return entities.indexOf(entity);
        }
        return -1;
    }

    public static int getSize(ArrayList<Entity> entities) {
        return entities.size();
    }

    public void add(T elem) {

    }

    public void remove(int id) {

    }

    //    public static Entity getAll(ArrayList<Entity> entities) {
    //
    //    }
}
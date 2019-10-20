package Repository;

import Domain.Entity;
import java.util.ArrayList;

public interface IRepository<T extends Entity> {
    void add(T elem);
    void remove(int id);
}
package Domain;

import Utils.CustomException;

import java.io.Serializable;

public class Discipline extends BaseObject implements Serializable {

    public String name;

    public Discipline(String name) {
        super(name);
        this.name = name;
    }

    @Override
    public String getName() {
        return this.name;
    }

    public void validateName(String name) throws CustomException {
        if (name.isEmpty()) {
            throw new CustomException("Name not given!");
        }
    }

    @Override
    public boolean setName(String name) {
        try {
            this.validateName(this.name);
            this.name = name;
        } catch (CustomException e) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return this.name;
    }
}

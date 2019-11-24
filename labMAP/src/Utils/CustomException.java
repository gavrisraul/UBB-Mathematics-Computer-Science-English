package Utils;

public class CustomException extends Exception {

    public String message;

    public CustomException( String message ) {
        this.message = message;
    }

    @Override
    public String getMessage() {
        return this.message;
    }

    public String toString() {
        return this.message;
    }
}

package Repository;

import Domain.BaseObject;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;
import java.sql.*;
import java.util.ArrayList;
import java.util.Properties;

public class DatabaseIORepository<CustomObject extends BaseObject> {
    private String dbDriver, dbUrl, user, password;
    private Connection connection;

    public DatabaseIORepository(Class<CustomObject> newData) throws Exception {

        try (InputStream input = new FileInputStream("/home/rg/IdeaProjects/labMAP/src/Resources/settings.properties")) {

            Properties configProperties = new Properties();

            configProperties.load(input);

            this.dbDriver = configProperties.getProperty("db.driver");
            this.dbUrl = configProperties.getProperty("db.url");
            this.user = configProperties.getProperty("db.user");
            this.password = configProperties.getProperty("db.password");

        } catch (IOException ex) {
            ex.printStackTrace();
        }

        this.connection = this.connect();
        this.initializeDB(newData);
    }

    private Connection connect() throws SQLException, ClassNotFoundException {
        Connection conn = null;
        try {
            Class.forName(this.dbDriver);
            conn = DriverManager.getConnection(this.dbUrl, this.user, this.password);
        } catch (SQLException | ClassNotFoundException e) {
            e.printStackTrace();
        }

        return conn;
    }

    private Connection getConnection() {
        return this.connection;
    }

    public void initializeDB(Class<CustomObject> newData) throws SQLException {
        String objectName = newData.getName().replace("Domain.", "");
        Statement myStatement = this.getConnection().createStatement();
        myStatement.executeUpdate("USE testDB;");
        myStatement.executeUpdate("CREATE TABLE IF NOT EXISTS " + objectName + "(\n" +
                "   id VARCHAR(100) NOT NULL,\n" +
                "   name VARCHAR(100) NOT NULL,\n" +
                "   PRIMARY KEY ( id )\n" +
                ");");
    }

    public ArrayList<CustomObject> getAllData(CustomObject newData) throws SQLException, IllegalAccessException, InvocationTargetException, InstantiationException, ClassNotFoundException, NoSuchMethodException {
        String objectName = newData.getClass().getName().replace("Domain.", "");
        Statement myStatement = this.getConnection().createStatement();
        ResultSet myResultSet = myStatement.executeQuery("SELECT * FROM " + objectName + ";");

        ArrayList<CustomObject> dataList = new ArrayList<CustomObject>();

        while (myResultSet.next()) {
            String name = myResultSet.getString("name");
            Constructor<?> constructor = Class.forName("Domain." + objectName).getConstructor(String.class);
            Object instance = constructor.newInstance(name);
            instance.getClass().getMethod("getName").invoke(instance);

            synchronized (instance) {
                dataList.add((CustomObject) instance);
            }
        }

        return dataList;
    }

    public ArrayList<CustomObject> add(CustomObject newData, int id, String name) throws SQLException, InvocationTargetException, ClassNotFoundException, InstantiationException, NoSuchMethodException, IllegalAccessException {
        String objectName = newData.getClass().getName().replace("Domain.", "");
        Statement myStatement = this.getConnection().createStatement();
        myStatement.executeUpdate("INSERT IGNORE INTO " + objectName + " VALUES('" + id + "', '" + name + "');");
        return this.getAllData(newData);
    }

    public ArrayList<CustomObject> getByIndex(CustomObject newData, int index) throws SQLException {
        ArrayList<CustomObject> dataList = new ArrayList<CustomObject>();
        String objectName = newData.getClass().getName().replace("Domain.", "");
        Statement myStatement = this.getConnection().createStatement();
        ResultSet myResultSet = myStatement.executeQuery("SELECT * FROM " + objectName + " WHERE id='" + index + "';");

        while (myResultSet.next()) {
            String name = myResultSet.getString("name");
            newData.setName(name);
            dataList.add(newData);
        }

        return dataList;
    }

    public ArrayList<CustomObject> setAtIndex(CustomObject newData, int index, String name) throws SQLException, InvocationTargetException, ClassNotFoundException, InstantiationException, NoSuchMethodException, IllegalAccessException {
        String objectName = newData.getClass().getName().replace("Domain.", "");
        Statement myStatement = this.getConnection().createStatement();
        myStatement.executeUpdate("UPDATE " + objectName + " SET name='" + name + "' WHERE id='" + index + "';");
        return this.getAllData(newData);
    }

    public ArrayList<CustomObject> deleteAtIndex(CustomObject newData, int index) throws SQLException, InvocationTargetException, ClassNotFoundException, InstantiationException, NoSuchMethodException, IllegalAccessException {
        String objectName = newData.getClass().getName().replace("Domain.", "");
        Statement myStatement = this.getConnection().createStatement();
        myStatement.execute("DELETE FROM " + objectName + " WHERE id='" + index + "';");
        return this.getAllData(newData);
    }
}
package Repository;

import Domain.BaseObject;

import java.io.*;
import java.util.ArrayList;
import java.util.Properties;


public class FileIORepository<CustomObject extends BaseObject> {

    private String file;
    private boolean isCsv;

    private Class<CustomObject> CustomObjectClass;

    public FileIORepository(Class<CustomObject> _Class, String file) {
        this.CustomObjectClass = _Class;
        this.file = file;
        File config = new File("/home/rg/IdeaProjects/labMAP/src/Resources/settings.properties");

        try {
            FileReader reader = new FileReader(config);
            Properties configProperties = new Properties();
            configProperties.load(reader);

            String fileType = configProperties.getProperty("file.type");
            this.isCsv = fileType.equals("csv");

            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void updateFile(ArrayList<CustomObject> dataList) {
        if (this.isCsv) {
            try {
                FileWriter fw = new FileWriter(this.file, false);
                PrintWriter pw = new PrintWriter(fw);

                for (CustomObject customObject : dataList) {
                    pw.printf("%s\n", customObject);
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        } else {
            try {
                FileOutputStream fos = new FileOutputStream(this.file);
                ObjectOutputStream oos = new ObjectOutputStream(fos);

                oos.writeObject(dataList);
                oos.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

    }

    public void add(CustomObject newData) {
        ArrayList<CustomObject> dataList = this.getAllData();
        dataList.add(newData);
        this.updateFile(dataList);
    }

    public ArrayList<CustomObject> getAllData() {
        ArrayList<CustomObject> dataList = new ArrayList<CustomObject>();

        if (this.isCsv) {
            try {
                BufferedReader br = new BufferedReader(new FileReader(this.file));
                String csvLine;
                while ((csvLine = br.readLine()) != null) {
                    try {
                        CustomObject newData = this.CustomObjectClass.getConstructor(String.class).newInstance(csvLine);
                        dataList.add(newData);
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        } else {
            try {
                FileInputStream fis = new FileInputStream(this.file);
                ObjectInputStream ois = new ObjectInputStream(fis);
                ArrayList<CustomObject> data = (ArrayList<CustomObject>) ois.readObject();

                ois.close();
                return data;
            } catch (IOException | ClassNotFoundException e) {
                e.printStackTrace();
            }
        }
        return dataList;
    }

    public CustomObject getByIndex(int index) {
        return this.getAllData().get(index);
    }

    public void setAtIndex(CustomObject newObject, int index) {
        ArrayList<CustomObject> dataList = this.getAllData();
        dataList.set(index, newObject);
        this.updateFile(dataList);
    }

    public void deleteAtIndex(int index) {
        ArrayList<CustomObject> dataList = this.getAllData();
        dataList.remove(index);
        this.updateFile(dataList);
    }
}

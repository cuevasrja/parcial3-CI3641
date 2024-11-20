import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;

public class persons {
    
    public static class Person {
        private String name;
        private int age;

        /**
         * Constructor
         * Initialize the name and age of the person
         * @param name Name of the person
         * @param age Age of the person
         */
        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }

        /**
         * Get the name of the person
         * @return Name of the person
         */
        public String getName() {
            return name;
        }

        /**
         * Get the age of the person
         * @return Age of the person
         */
        public int getAge() {
            return age;
        }
    }

    public static class Persons {
        private List<Person> persons;
        private HashMap<String, Integer> names;

        /**
         * Constructor
         * Initialize the list of persons and the map of names
         */
        public Persons() {
            persons = new ArrayList<>();
            names = new HashMap<>();
        }

        /**
         * Check if a person with the given name and age exists
         * @param name Name of the person
         * @param age Age of the person
         * @return True if the person exists, false otherwise
         */
        public Boolean exists(String name, int age) {
            Person person = this.persons.stream().filter(p -> p.getName().equals(name) && p.getAge() == age).findFirst().orElse(null);
            return person != null;
        }

        /**
         * Add a person with the given name and age. If the person already exists, it will not be added
         * @param name Name of the person
         * @param age Age of the person
         */
        public void add(String name, int age) {
            // Check if the person already exists
            if (!exists(name, age)) {
                // Add the person
                Person person = new Person(name, age);
                this.persons.add(person);
                this.names.put(name, this.names.getOrDefault(name, 0) + 1);
            }
        }

        /**
         * Get the number of persons
         * @return Number of persons
         */
        public Integer size() {
            return this.persons.size();
        }

        /**
         * Get the persons with age greater or equal to 18
         * @return Persons with age greater or equal to 18
         */
        public Persons adults() {
            Persons up18Persons = new Persons();
            this.persons.stream().filter(p -> p.getAge() >= 18).forEach(p -> up18Persons.add(p.getName(), p.getAge()));
            return up18Persons;
        }

        /**
         * Get the most repeated name
         * @return Most repeated name
         */
        public String getMostRepeatedName() {
            return this.names.entrySet().stream().filter(e -> e.getValue() == this.names.values().stream().max(Integer::compare).get()).findFirst().get().getKey();
        }
    }

    public static void main(String[] args) {
        Persons persons = new Persons();
        persons.add("Alice", 20);
        persons.add("Bob", 30);
        persons.add("Alice", 2);
        persons.add("Charlie", 40);
        persons.add("Alice", 20);
        persons.add("Alice", 12);
        persons.add("Alice", 80);
        persons.add("Juan", 96);

        System.out.println("Number of persons: " + persons.size());
        System.out.println("Number of persons with age greater or equal to 18: " + persons.adults().size());
        System.out.println("Most repeated name: " + persons.getMostRepeatedName());
    }

    
}

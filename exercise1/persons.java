import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Hashtable;

public class persons {
    public static class Person {
        private String name;
        private int age;

        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }

        public String getName() {
            return name;
        }

        public int getAge() {
            return age;
        }
    }

    public static class Persons {
        private List<Person> persons;
        private HashMap<String, Integer> names;

        public Persons() {
            persons = new ArrayList<>();
            names = new HashMap<>();
        }

        public Boolean exists(String name, int age) {
            Person person = this.persons.stream().filter(p -> p.getName().equals(name) && p.getAge() == age).findFirst().orElse(null);
            return person != null;
        }

        public void add(String name, int age) {
            if (!exists(name, age)) {
                Person person = new Person(name, age);
                this.persons.add(person);
                this.names.put(name, this.names.getOrDefault(name, 0) + 1);
            }
        }

        public Integer countPersons() {
            return this.persons.size();
        }

        public Persons getUpOr18Persons() {
            Persons up18Persons = new Persons();
            this.persons.stream().filter(p -> p.getAge() >= 18).forEach(p -> up18Persons.add(p.getName(), p.getAge()));
            return up18Persons;
        }

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

        System.out.println("Number of persons: " + persons.countPersons());
        System.out.println("Number of persons with age greater or equal to 18: " + persons.getUpOr18Persons().countPersons());
        System.out.println("Most repeated name: " + persons.getMostRepeatedName());
    }

    
}

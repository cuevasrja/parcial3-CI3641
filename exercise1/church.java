import java.util.function.UnaryOperator;

public class church {
    public static void main(String[] args) {
        // Check if the number of arguments is correct
        if (args.length != 1) {
            System.out.println("Usage: java Main <n>");
            return;
        }

        // Parse the argument
        int n = Integer.parseInt(args[0]);
        System.out.println("n = " + n);

        // Calculate the result
        Church<Integer> result = Church.of(n);
        System.out.println("Church(" + n + ") = " + result.apply(x -> x + 1, 0));
    }

    // public class ChurchNumeral {
    //     int n;
    //     ChurchNumeral next;

    //     // Constructor
    //     public ChurchNumeral(int n) {
    //         this.n = n;
    //     }

    //     // Methods

    //     public ChurchNumeral nextChurchNumeral() {
    //         // TODO
    //         return null;
    //     }
        
    //     public ChurchNumeral add(ChurchNumeral n) {
    //         // TODO
    //         return null;
    //     }

    //     public ChurchNumeral multiply(ChurchNumeral n) {
    //         // TODO
    //         return null;
    //     }

    // }

    // // Zero extends ChurchNumeral
    // public class Zero extends ChurchNumeral {
    //     int n = 0;
    //     ChurchNumeral next = null;

    //     // Constructor
    //     public Zero() {
    //         super(0);
    //         // Create the Successor
    //         next = new ChurchNumeral(1);
    //     }
    // }

    static interface Church<T> extends UnaryOperator<UnaryOperator<T>> {

        static <T> Church<T> of(int n) {
            if (n < 0) {
                throw new IllegalArgumentException();
            } else if (n == 0) {
                return zero();
            } else {
                return sum(one(), Church.of(n - 1));
            }
        }

        static <T> Church<T> zero() {
            return f -> (t -> t);
        }

        static <T> Church<T> one() {
            return f -> f;
        }

        static <T> Church<T> sum(Church<T> a, Church<T> b) {
            return f -> b.apply(f).andThen(a.apply(f))::apply;
        }

        static <T> Church<T> mul(Church<T> a, Church<T> b) {
            return f -> a.apply(b.apply(f))::apply;
        }

        @SuppressWarnings("unchecked")
        default <U> Church<U> convert() {
            return (Church<U>) this;
        }

        default T apply(UnaryOperator<T> f, T t) {
            return this.apply(f).apply(t);
        }

    }
}
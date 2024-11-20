public class church {
    public static class Church {
        private String value;
        
        /**
         * Constructor
         */
        public Church() {
            this.value = "ZERO";
        }
    
        /**
         * Define the successor function
         * @return Church
         */
        public Church suc() {
            String value = "Suc(" + this.value + ")";
            Church suc = new Church();
            suc.value = value;
            return suc;
        }
    
        /**
         * Apply the successor function n times to the Church instance
         * @param other Church instance
         * @return Church instance with the sum of both
         */
        public Church add(Church other) {
            int n = this.toInteger();
            int m = Church.toInteger(other);
            Church result = Church.toChurch(n + m);
            return result;
        }
    
        /**
         * Sum the Church instance with an integer
         * @param other int
         * @return Church instance with the sum of both
         */
        public Church add(int other) {
            int n = this.toInteger();
            int m = other;
            Church result = Church.toChurch(n + m);
            return result;
        }
    
        /**
         * Multiply the Church instance with an other Church instance
         * @param other Church instance
         * @return Church instance with the product of both
         */
        public Church multiply(Church other) {
            int n = Church.toInteger(other);
            int m = Church.toInteger(this);
            Church result = Church.toChurch(n * m);
            return result;
        }
    
        /**
         * Convert an integer to a Church numeral
         * @param v int
         * @return Church instance
         */
        public static Church toChurch(int v) {
            Church number = new Church();
            StringBuilder funStart = new StringBuilder();
            StringBuilder funEnd = new StringBuilder();
            while (v-- > 0) {
                funStart.append("Suc(");
                funEnd.append(")");
            }
            number.value = funStart + number.value + funEnd;
            return number;
        }
    
        /**
         * Convert the Church numeral to an integer
         * @return integer transformed from the Church numeral
         */
        public int toInteger() {
            int i = 0;
            for (int j = 0; j < this.value.length(); j++) {
                if (this.value.charAt(j) == '(') i++;
            }
            return i;
        }
    
        /**
         * Convert the Church numeral to an integer
         * @param a Church instance
         * @return integer transformed from the Church numeral
         */
        public static int toInteger(Church a) {
            int i = 0;
            for (int j = a.value.length() - 1; j > 0 && a.value.charAt(j) != 'O'; j--) {
                if (a.value.charAt(j) == ')') i++;
            }
            return i;
        }

        /**
         * Convert the Church numeral to a string
         * @return string transformed from the Church numeral
         */
        @Override
        public String toString() {
            return this.value;
        }
    }

    public static void main(String[] args) {
        Church cero = new Church();
        Church uno = cero.suc();
        Church dos = uno.suc();

        System.out.println("Cero: " + cero);
        System.out.println("Uno: " + uno);
        System.out.println("Dos: " + dos);

        Church tres = Church.toChurch(3);
        System.out.println("Tres: " + tres);

        Church suma = uno.add(dos);
        System.out.println("Uno + Dos: " + suma);

        Church producto = dos.multiply(tres);
        System.out.println("Dos * Tres: " + producto);
    }
}
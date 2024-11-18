COMPILER=javac
TARGET-B=church.class
TARGET-C=persons.class
.PHONY: comp-b run-c clean

comp-b: church.java
	$(COMPILER) church.java

$(TARGET-C): persons.java
	$(COMPILER) persons.java

run-c: $(TARGET-C)
	java persons

clean:
	rm -f *.class
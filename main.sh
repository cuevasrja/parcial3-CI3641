# !/bin/bash

# This script is used to run the main program

function menu() {
    echo -e "\033[92m1.\033[0m $1 exe1-b <n>"
    echo -e "\033[92m2.\033[0m $1 exe1-c"
    echo -e "\033[92m5.\033[0m $1 exe3"
    echo -e "\033[92m6.\033[0m $1 exe3-test"
    echo -e "\033[92m6.\033[0m $1 exe4"
    echo -e "\033[92m6.\033[0m $1 exe5 <n>"
    echo -e "\033[92m6.\033[0m $1 help"
}

# If the input is lower than 1, the program will exit
if [ $# -lt 1 ]; then
    echo -e "\033[91;1mError:\033[0m The program needs at least 1 argument"
    echo -e "For more information, type: \033[1;92m$0 help\033[0m"
    exit 1
fi

if [ $1 == "help" ]; then
    echo -e "\033[92;1mUsage:\033[0m $0 <command> <args>"
    echo -e "\033[92;1mCommands:\033[0m"
    menu $0
    exit 0
fi

ACTUAL_PATH=$(pwd)
SRC_PATH=$(dirname $0)

cd $SRC_PATH

# If the first argument is exe1-b, then the program has to have 2 arguments
if [ $1 == "exe1-b" ]; then
    # TODO
    if [ $# -lt 2 ]; then
        echo -e "\033[91;1mError:\033[0m The program needs at least 2 arguments"
        echo -e "For more information, type: \033[1;92m$0 help\033[0m"
        cd $ACTUAL_PATH
        exit 1
    fi
    cd exercise1
    if [ ! -f "partb.c" ]; then
        make partb > /dev/null
    fi
    ./partb.out $2
    cd ..
elif [ $1 == "exe1-c" ]; then
    # TODO
    if [ $# -lt 2 ]; then
        echo -e "\033[91;1mError:\033[0m The program needs at least 2 arguments"
        echo -e "For more information, type: \033[1;92m$0 help\033[0m"
        cd $ACTUAL_PATH
        exit 1
    fi
    cd exercise1
    if [ ! -f "partc.c" ]; then
        make partc > /dev/null
    fi
    # Send all the arguments except the first one
    ./partc.out "${@:2}"
    cd ..
elif [ $1 == "exe3" ]; then
    cd exercise3
    python main.py
    cd ..
elif [ $1 == "exe3-test" ]; then
    cd exercise3
    coverage run -m unittest discover
    coverage report -m
    coverage html
    cd ..
elif [ $1 == "exe4" ]; then
    cd exercise4
    make > /dev/null
    # If results.csv exists, then remove it
    if [ -f "results.csv" ]; then
        rm results.csv
    fi
    echo "rows,cols,attempt,time,operation" > results.csv
    ./main.out >> results.csv && python analyze.py
    cd ..
elif [ $1 == "exe5" ]; then
    if [ $# -lt 2 ]; then
        echo -e "\033[91;1mError:\033[0m The program needs at least 2 arguments"
        echo -e "For more information, type: \033[1;92m$0 help\033[0m"
        cd $ACTUAL_PATH
        exit 1
    fi
    cd exercise5
    python main.py $2
    cd ..
    
else
    echo -e "\033[91;1mError:\033[0m The command is not valid"
    echo -e "For more information, type: \033[1;92m$0 help\033[0m"
    cd $ACTUAL_PATH
    exit 1
fi

cd $ACTUAL_PATH
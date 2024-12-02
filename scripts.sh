AOC_COOKIE="53616c7465645f5ff564a3e39b9abc58f190bee85c89497102310ab08fca8f6d8879c7cb552487673da6f8733e3fb5859d14619780f216073ab912cfbced5545" # get this from the cookies tab in network tools on the AOC website

alias aos="python3 solution.py < in.txt"
alias aot="echo -ne '\\e[0;34m'; python3 solution.py < test.txt; echo -ne '\\e[0m'"
alias aoc="aot; echo; aos"

function aoc-load () {
    if [ $1 ]
    then
        curl --cookie "session=$AOC_COOKIE" https://adventofcode.com/$1/day/$2/input > in.txt
    else
        curl --cookie "session=$AOC_COOKIE" "$(echo `date +https://adventofcode.com/%Y/day/%d/input` | sed 's/\/0/\//g')" > in.txt
    fi
}
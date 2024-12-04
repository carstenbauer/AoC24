AOC_COOKIE="53616c7465645f5fb2e1eed867886ff4bcb6b168075544b72b120c45ac2e3458b5c29d0a160411f72b9e235e1b1fa738f63a156c614b70703ce6a3f5781f0a23" # get this from the cookies tab in network tools on the AOC website

alias aos="python3 solution.py < in.txt"
alias aot="echo -ne '\\e[0;34m'; python3 solution.py < test.txt; echo -ne '\\e[0m'"
alias aoc="aot; echo; aos"

function aoc-load() {
  if [ $1 ]; then
    curl --cookie "session=$AOC_COOKIE" https://adventofcode.com/$1/day/$2/input >in.txt
  else
    curl --cookie "session=$AOC_COOKIE" "$(echo $(date +https://adventofcode.com/%Y/day/%d/input) | sed 's/\/0/\//g')" >in.txt
  fi
}

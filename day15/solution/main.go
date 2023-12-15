package main

import (
	"fmt"
	"helpers"
)

func part1() uint64 {
	input := helpers.ReadFileContentsIgnoreNewline("input")
	return helpers.SumArr(helpers.HASHInput(input))
}

func main() {
	fmt.Println(part1())
}

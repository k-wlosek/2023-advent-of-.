package main

import (
	"fmt"
	"helpers"
)

func part1() int {
	contents := helpers.ReadFileContents("input")
	helpers.TiltPlatformNorth(contents)
	roundLoads := helpers.CalculateRoundLoads(contents)
	sum := helpers.AddAll(roundLoads)
	return sum
}

func part2() int {
	contents := helpers.ReadFileContents("input")
	cycles := 1000000000
	i := 0
	states := map[string]int{}
	for i < cycles {
		helpers.CyclePlatform(contents, 1)
		h := helpers.PlatformToStr(contents)
		if _, ok := states[h]; ok {
			off := i - states[h]
			remaining := cycles - i
			i += remaining / off * off
			states = map[string]int{}
		}
		states[h] = i
		i += 1
	}
	roundLoads := helpers.CalculateRoundLoads(contents)
	sum := helpers.AddAll(roundLoads)
	return sum
}

func main() {
	fmt.Println(part1())
	fmt.Println(part2())
}

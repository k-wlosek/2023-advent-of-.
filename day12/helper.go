package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"sync"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func readFileContents(filename string) []string {
	contents, err := os.ReadFile(filename)
	check(err)
	return strings.Split(string(contents), "\n")
}

func splitGridOn(lines []string, splitOn string) [][]string {
	springs := []string{}
	broken := []string{}

	for _, line := range lines {
		a := strings.Split(line, splitOn)
		springs = append(springs, a[0])
		broken = append(broken, a[1])
	}
	return [][]string{springs, broken}
}

func splitBrokenOn(broken []string, splitOn string) [][]int {
	res := [][]int{}
	for _, brokenList := range broken {
		numbers := []int{}
		for _, brokenNumber := range strings.Split(brokenList, splitOn) {
			numberAsInt, _ := strconv.Atoi(brokenNumber)
			numbers = append(numbers, numberAsInt)
		}
		res = append(res, numbers)
	}
	return res
}

func unfoldBrokenStr(broken []string) []string {
	res := []string{}
	for _, str := range broken {
		str = str + concatStrNTimes("?"+str, 4)
		res = append(res, str)
	}
	return res
}

func concatStrNTimes(str string, n int) string {
	res := ""
	for i := 0; i < n; i++ {
		res += str
	}
	return res
}

func unfoldBrokenInt(broken [][]int) [][]int {
	res := [][]int{}
	for _, numbers := range broken {
		res = append(res, concatIntArrNTimes(numbers, 5))
	}
	return res
}

func concatIntArrNTimes(arr []int, n int) []int {
	res := []int{}
	for i := 0; i < n; i++ {
		res = append(res, arr...)
	}
	return res
}

var cache = make(map[string]map[string]int)
var cacheMutex sync.Mutex

func countFills(line string, numbers []int) int {
	cacheKey := fmt.Sprintf("%s-%v", line, numbers)

	// Check if result is cached
	cacheMutex.Lock()
	if cachedResult, exists := cache[cacheKey]; exists {
		cacheMutex.Unlock()
		return cachedResult["result"]
	}
	cacheMutex.Unlock()

	// Base case: if no more numbers to check
	if len(numbers) == 0 {
		// If '#' is present in the line, no valid substitution
		if strings.Contains(line, "#") {
			return 0
		}
		// If no '#' is present, there's one valid substitution
		return 1
	} else if line == "" || numbers[0] > len(line) {
		// Base case: if line is empty or the current group size is greater than the remaining line length
		return 0
	}

	// Recursive cases based on the current character in the line
	if line[0] == '.' {
		// If the current character is '.', move to the next character
		result := countFills(line[1:], numbers)

		// Cache the result
		cacheMutex.Lock()
		cache[cacheKey] = map[string]int{"result": result}
		cacheMutex.Unlock()

		return result
	} else if line[0] == '#' {
		// If the current character is '#'
		size := numbers[0]
		result := true

		// Check if all characters in the current group not '.'
		for i := 0; i < size; i++ {
			if line[i] == '.' {
				result = false
				break
			}
		}

		if result {
			// If all characters in the current group are not '.'
			if len(line) == size {
				// If the line is exhausted after this group
				if len(numbers) == 1 {
					result := 1 // Valid substitution found

					// Cache the result
					cacheMutex.Lock()
					cache[cacheKey] = map[string]int{"result": result}
					cacheMutex.Unlock()

					return result
				}
				return 0 // Continue with the next group
			}

			// If there are more characters after the current group
			if line[size] != '#' {
				result := countFills("."+line[size+1:], numbers[1:]) // Move to the next group

				// Cache the result
				cacheMutex.Lock()
				cache[cacheKey] = map[string]int{"result": result}
				cacheMutex.Unlock()

				return result
			}
		}
		return 0 // Invalid substitution, move to the next character
	} else {
		// If the current character is '?', try both possibilities
		result := countFills("."+line[1:], numbers) + countFills("#"+line[1:], numbers)

		// Cache the result
		cacheMutex.Lock()
		cache[cacheKey] = map[string]int{"result": result}
		cacheMutex.Unlock()

		return result
	}
}

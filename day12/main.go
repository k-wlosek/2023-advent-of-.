package main

import (
	"fmt"
	"sync"
)

func solve1(filename string) int {
	contents := readFileContents(filename)
	split := splitGridOn(contents, " ")
	broken := splitBrokenOn(split[1], ",")
	runningTotal := 0
	for i, line := range split[0] {
		runningTotal += countFills(line, broken[i])
	}
	return runningTotal
}

func solve2(filename string) int {
	contents := readFileContents(filename)
	split := splitGridOn(contents, " ")
	fmt.Println("split")
	unfoldedBrokenStr := unfoldBrokenStr(split[0])
	fmt.Println("unfoldedBrokenStr")
	broken := splitBrokenOn(split[1], ",")
	fmt.Println("broken")
	unfoldedBrokenInt := unfoldBrokenInt(broken)
	fmt.Println("unfoldedBrokenInt")
	runningTotal := 0
	for i, line := range unfoldedBrokenStr {
		runningTotal += countFills(line, unfoldedBrokenInt[i])
		fmt.Printf("step %d/%d, runningTotal so far: %d\n", i, len(unfoldedBrokenStr), runningTotal)
	}
	return runningTotal
}

func solve2Parallel(filename string) int {
	contents := readFileContents(filename)
	split := splitGridOn(contents, " ")
	fmt.Println("split")
	unfoldedBrokenStr := unfoldBrokenStr(split[0])
	fmt.Println("unfoldedBrokenStr")
	broken := splitBrokenOn(split[1], ",")
	fmt.Println("broken")
	unfoldedBrokenInt := unfoldBrokenInt(broken)
	fmt.Println("unfoldedBrokenInt")

	var wg sync.WaitGroup
	resultChan := make(chan int, len(unfoldedBrokenStr))
	progressMutex := &sync.Mutex{}
	var progress int

	for i, line := range unfoldedBrokenStr {
		wg.Add(1)
		go func(i int, line string, unfoldedBrokenIntVal []int) {
			defer wg.Done()
			count := countFills(line, unfoldedBrokenIntVal)
			resultChan <- count

			// Update progress safely using a mutex
			progressMutex.Lock()
			progress++
			fmt.Printf("step %d/%d, runningTotal so far: %d\n", progress, len(unfoldedBrokenStr), count)
			progressMutex.Unlock()
		}(i, line, unfoldedBrokenInt[i])
	}

	go func() {
		wg.Wait()
		close(resultChan)
	}()

	runningTotal := 0
	for count := range resultChan {
		runningTotal += count
	}

	return runningTotal
}

func main() {
	fmt.Println(solve1("input"))
	fmt.Println(solve2Parallel("input"))
}

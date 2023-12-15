package helpers

import (
	"os"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func ReadFileContentsIgnoreNewline(filename string) []string {
	fileContents, err := os.ReadFile(filename)
	check(err)
	fileContentsStr := string(fileContents)
	for i := 0; i < len(fileContentsStr); i++ {
		if fileContentsStr[i] == '\n' {
			fileContentsStr = fileContentsStr[:i] + fileContentsStr[i+1:]
		}
	}
	// Split on commas
	ret := []string{}
	for i := 0; i < len(fileContentsStr); i++ {
		if fileContentsStr[i] == ',' {
			ret = append(ret, fileContentsStr[:i])
			fileContentsStr = fileContentsStr[i+1:]
			i = 0
		}
	}
	ret = append(ret, fileContentsStr)
	return ret
}

func HASHAlgorithm(input string) uint64 {
	currentValue := 0
	for i := 0; i < len(input); i++ {
		currentValue += int(input[i])
		currentValue *= 17
		currentValue %= 256
	}
	return uint64(currentValue)
}

func HASHInput(input []string) []uint64 {
	ret := []uint64{}
	for _, inputPart := range input {
		ret = append(ret, HASHAlgorithm(inputPart))
	}
	return ret
}

func SumArr(arr []uint64) uint64 {
	ret := uint64(0)
	for _, val := range arr {
		ret += val
	}
	return ret
}

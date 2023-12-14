package helpers

import (
	"os"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func ReadFileContents(filename string) []string {
	contents, err := os.ReadFile(filename)
	check(err)
	return strings.Split(string(contents), "\n")
}

// Mutates platform
func TiltPlatformNorth(platform []string) {
	for k := 0; k < len(platform); k++ {
		for i := 1; i < len(platform); i++ {
			// Skip first row
			for j := 0; j < len(platform[i]); j++ {
				if platform[i][j] == 'O' && platform[i-1][j] == '.' {
					rowAbove := []rune(platform[i-1])
					rowAbove[j] = 'O'
					platform[i-1] = string(rowAbove)

					rowCurrent := []rune(platform[i])
					rowCurrent[j] = '.'
					platform[i] = string(rowCurrent)
				}
			}
		}
	}
}

func TiltPlatformSouth(platform []string) {
	for k := 0; k < len(platform); k++ {
		for i := len(platform) - 2; i >= 0; i-- {
			// Skip last row
			for j := 0; j < len(platform[i]); j++ {
				if platform[i][j] == 'O' && platform[i+1][j] == '.' {
					rowBelow := []rune(platform[i+1])
					rowBelow[j] = 'O'
					platform[i+1] = string(rowBelow)

					rowCurrent := []rune(platform[i])
					rowCurrent[j] = '.'
					platform[i] = string(rowCurrent)
				}
			}
		}
	}
}

func TiltPlatformWest(platform []string) {
	for k := 0; k < len(platform); k++ {
		for i := 0; i < len(platform); i++ {
			for j := 1; j < len(platform[i]); j++ {
				if platform[i][j] == 'O' && platform[i][j-1] == '.' {
					rowCurrent := []rune(platform[i])
					rowCurrent[j-1] = 'O'
					platform[i] = string(rowCurrent)

					rowCurrent[j] = '.'
					platform[i] = string(rowCurrent)
				}
			}
		}
	}
}

func TiltPlatformEast(platform []string) {
	for k := 0; k < len(platform); k++ {
		for i := 0; i < len(platform); i++ {
			for j := len(platform[i]) - 2; j >= 0; j-- {
				if platform[i][j] == 'O' && platform[i][j+1] == '.' {
					rowCurrent := []rune(platform[i])
					rowCurrent[j+1] = 'O'
					platform[i] = string(rowCurrent)

					rowCurrent[j] = '.'
					platform[i] = string(rowCurrent)
				}
			}
		}
	}
}

func CyclePlatform(platform []string, cycles int) {
	for i := 0; i < cycles; i++ {
		TiltPlatformNorth(platform)
		TiltPlatformWest(platform)
		TiltPlatformSouth(platform)
		TiltPlatformEast(platform)
	}
}

func CalculateRoundLoads(platform []string) []int {
	loads := []int{}
	for i := 0; i < len(platform); i++ {
		for j := 0; j < len(platform[i]); j++ {
			if platform[i][j] == 'O' {
				loads = append(loads, len(platform)-i)
			}
		}
	}
	return loads
}

func PlatformToStr(platform []string) string {
	str := ""
	for i := 0; i < len(platform); i++ {
		str += platform[i] + "\n"
	}
	return str
}

func AddAll(a []int) int {
	sum := 0
	for _, v := range a {
		sum += v
	}
	return sum
}

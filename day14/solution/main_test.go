package main_test

import (
	"helpers"
	"testing"
)

func TestTiltPlatformNorth(t *testing.T) {
	contents := helpers.ReadFileContents("testing")
	helpers.TiltPlatformNorth(contents)
	expected := []string{
		"OOOO.#.O..",
		"OO..#....#",
		"OO..O##..O",
		"O..#.OO...",
		"........#.",
		"..#....#.#",
		"..O..#.O.O",
		"..O.......",
		"#....###..",
		"#....#....",
	}

	// Check each element in the slices
	for i := 0; i < len(contents); i++ {
		if contents[i] != expected[i] {
			t.Errorf("Mismatch at index %d, got %v, want %v", i, contents[i], expected[i])
			break
		}
	}
}

func TestTiltPlatformSouth(t *testing.T) {
	contents := helpers.ReadFileContents("testing")
	helpers.TiltPlatformSouth(contents)
	expected := []string{
		".....#....",
		"....#....#",
		"...O.##...",
		"...#......",
		"O.O....O#O",
		"O.#..O.#.#",
		"O....#....",
		"OO....OO..",
		"#OO..###..",
		"#OO.O#...O",
	}

	// Check each element in the slices
	for i := 0; i < len(contents); i++ {
		if contents[i] != expected[i] {
			t.Errorf("Mismatch at index %d, got %v, want %v", i, contents[i], expected[i])
			break
		}
	}
}

func TestTiltPlatformWest(t *testing.T) {
	contents := helpers.ReadFileContents("testing")
	helpers.TiltPlatformWest(contents)
	expected := []string{
		"O....#....",
		"OOO.#....#",
		".....##...",
		"OO.#OO....",
		"OO......#.",
		"O.#O...#.#",
		"O....#OO..",
		"O.........",
		"#....###..",
		"#OO..#....",
	}

	// Check each element in the slices
	for i := 0; i < len(contents); i++ {
		if contents[i] != expected[i] {
			t.Errorf("Mismatch at index %d, got %v, want %v", i, contents[i], expected[i])
			break
		}
	}
}

func TestTiltPlatformEast(t *testing.T) {
	contents := helpers.ReadFileContents("testing")
	helpers.TiltPlatformEast(contents)
	expected := []string{
		"....O#....",
		".OOO#....#",
		".....##...",
		".OO#....OO",
		"......OO#.",
		".O#...O#.#",
		"....O#..OO",
		".........O",
		"#....###..",
		"#..OO#....",
	}

	// Check each element in the slices
	for i := 0; i < len(contents); i++ {
		if contents[i] != expected[i] {
			t.Errorf("Mismatch at index %d, got %v, want %v", i, contents[i], expected[i])
			break
		}
	}
}

func TestCyclePlatformOnce(t *testing.T) {
	contents := helpers.ReadFileContents("testing")
	helpers.CyclePlatform(contents, 1)
	expected := []string{
		".....#....",
		"....#...O#",
		"...OO##...",
		".OO#......",
		".....OOO#.",
		".O#...O#.#",
		"....O#....",
		"......OOOO",
		"#...O###..",
		"#..OO#....",
	}

	// Check each element in the slices
	for i := 0; i < len(contents); i++ {
		if contents[i] != expected[i] {
			t.Errorf("Mismatch at index %d, got %v, want %v", i, contents[i], expected[i])
			break
		}
	}
}

func TestCyclePlatformThrice(t *testing.T) {
	contents := helpers.ReadFileContents("testing")
	helpers.CyclePlatform(contents, 3)
	expected := []string{
		".....#....",
		"....#...O#",
		".....##...",
		"..O#......",
		".....OOO#.",
		".O#...O#.#",
		"....O#...O",
		".......OOO",
		"#...O###.O",
		"#.OOO#...O",
	}

	// Check each element in the slices
	for i := 0; i < len(contents); i++ {
		if contents[i] != expected[i] {
			t.Errorf("Mismatch at index %d, got %v, want %v", i, contents[i], expected[i])
			break
		}
	}
}

func TestCyclePlatformAdditive(t *testing.T) {
	contents := helpers.ReadFileContents("testing")
	for i := 0; i < 3; i++ {
		helpers.CyclePlatform(contents, 1)
	}
	expected := []string{
		".....#....",
		"....#...O#",
		".....##...",
		"..O#......",
		".....OOO#.",
		".O#...O#.#",
		"....O#...O",
		".......OOO",
		"#...O###.O",
		"#.OOO#...O",
	}

	// Check each element in the slices
	for i := 0; i < len(contents); i++ {
		if contents[i] != expected[i] {
			t.Errorf("Mismatch at index %d, got %v, want %v", i, contents[i], expected[i])
			break
		}
	}
}

func TestCalculateRoundLoads(t *testing.T) {
	contents := helpers.ReadFileContents("testing")
	helpers.TiltPlatformNorth(contents)
	roundLoads := helpers.CalculateRoundLoads(contents)
	sum := helpers.AddAll(roundLoads)
	expected := 136

	if sum != expected {
		t.Errorf("Mismatch, got %v, want %v", sum, expected)
	}
}

func TestCalculateRoundLoadsAfterCycles(t *testing.T) {
	contents := helpers.ReadFileContents("testing")

	// Run 1000000000 cycles
	// Optimized by storing states and calculating the remaining cycles
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
	expected := 64

	if sum != expected {
		t.Errorf("Mismatch, got %v, want %v", sum, expected)
	}
}

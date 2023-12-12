package main

import "testing"

func TestSolve1(t *testing.T) {
	result := solve1("testing")
	expected := 21

	if result != expected {
		t.Errorf("Expected %d, but got %d", expected, result)
	}
}

func TestSolve2(t *testing.T) {
	result := solve2("testing")
	expected := 525152

	if result != expected {
		t.Errorf("Expected %d, but got %d", expected, result)
	}
}

func TestSolve2Parallel(t *testing.T) {
	result := solve2Parallel("testing")
	expected := 525152

	if result != expected {
		t.Errorf("Expected %d, but got %d", expected, result)
	}
}

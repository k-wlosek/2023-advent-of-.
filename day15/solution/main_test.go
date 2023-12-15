package main_test

import (
	"helpers"
	"testing"
)

func TestReadFileContentsIgnoreNewline(t *testing.T) {
	contents := helpers.ReadFileContentsIgnoreNewline("testing")
	expected := []string{"rn=1", "cm-", "qp=3", "cm=2", "qp-", "pc=4", "ot=9", "ab=5", "pc-", "pc=6", "ot=7"}
	if len(contents) != len(expected) {
		t.Errorf("Expected length of %d, got %d", len(expected), len(contents))
	}
	for i := 0; i < len(contents); i++ {
		if contents[i] != expected[i] {
			t.Errorf("Expected %s, got %s", expected[i], contents[i])
		}
	}
}

func TestHASHAlgorithm(t *testing.T) {
	input := "HASH"
	actual := helpers.HASHAlgorithm(input)
	expected := uint64(52)
	if actual != expected {
		t.Errorf("Expected %d, got %d", expected, actual)
	}
}

func TestHASHInputWithSum(t *testing.T) {
	input := helpers.ReadFileContentsIgnoreNewline("testing")
	actual := helpers.SumArr(helpers.HASHInput(input))
	expected := uint64(1320)
	if actual != expected {
		t.Errorf("Expected %d, got %d", expected, actual)
	}
}

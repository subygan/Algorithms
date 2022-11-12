package algos

import (
	"bytes"
	"crypto/sha1"
	"encoding/binary"
	"fmt"
)

type Bloom struct {
	bits [1000]bool
}

func (b *Bloom) Set(s string) (int, error) {

	i, err := b.getLocation(s) // Get location in filter to be inserted
	if err != nil {
		return 0, err
	}

	b.bits[i] = true // set true to the location
	return i, nil
}

func (b *Bloom) isPresent(s string) bool {

	i, err := b.getLocation(s) // Get location in filter to be verified
	if err != nil {
		return false
	}

	return b.bits[i]
}

func (b *Bloom) getLocation(value string) (int, error) {

	// hash the string and convert to integer (to be used in binary array)
	h := sha1.New()
	h.Write([]byte(value))
	bits := h.Sum(nil)
	buf := bytes.NewBuffer(bits)
	result, err := binary.ReadUvarint(buf)
	if err != nil {
		return 0, err
	}

	// Ensure all numbers are > 0
	if result < 0 {
		result = -result
	}
	return int(result) % len(b.bits), nil //make sure int is within the array length by doing a modulo
}

func main() {

	var b Bloom
	s := "ThisIsString"
	set, err := b.Set(s)
	if err != nil {
		return
	}
	fmt.Println(s, " set in location", set)
	fmt.Println(s, "in filter : ", b.isPresent(s))

}

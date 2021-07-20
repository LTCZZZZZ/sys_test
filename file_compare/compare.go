package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	a, _ := ioutil.ReadFile("staging.env")
	b, _ := ioutil.ReadFile("staging_error.env")
	fmt.Printf("%v\n", a)
	fmt.Printf("%v\n", b)
// 	for i, _ := range a {
// 		if a[i] != b[i] {
// 			fmt.Println(i, a[i], b[i])
// 		}
// 	}

	fmt.Println(string(a) == string(b))
}

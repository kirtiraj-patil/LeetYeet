package main
import "fmt"

func insertionSort(arr []int) {
  for i := 0; i < len(arr); i++ {
    for j := i + 1; j < len(arr); j++ {
      currIndex := j
      for currIndex > 0 && arr[currIndex] < arr[currIndex - 1] {
        temp := arr[currIndex]
        arr[currIndex] = arr[currIndex - 1]
        arr[currIndex - 1] = temp
        currIndex--
      }
    }
  }
}

func main() {
  numbers := []int {1,9,5,7,2,8,77,44}
  fmt.Println(numbers)
  insertionSort(numbers)
  fmt.Println(numbers)
}

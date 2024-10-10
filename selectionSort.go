package main
import "fmt"

func selectionSort(arr []int) {
  for i := 0; i < len(arr); i++ {
    minIndex := i
    min := arr[i]
    for j := i + 1; j < len(arr); j++ {
      if min > arr[j] {
        min = arr[j]
        minIndex = j
      }
    }
    temp := arr[i]
    arr[i] = min
    arr[minIndex] = temp
  }
}

func main() {
  numbers := []int {1,9,5,7,2,8,77,44}
  fmt.Println(numbers)
  selectionSort(numbers)
  fmt.Println(numbers)
}

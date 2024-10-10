package main
import "fmt"

func bubbleSort(arr []int) {
  for i := 0; i < len(arr); i++ {
    for j := 0; j < len(arr) - i - 1; j++ {
      if arr[j] > arr[j+1] {
        temp := arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp
      }
    }
  }
}

func main() {
  numbers := []int {1,9,5,7,2,8,77,44}
  fmt.Println(numbers)
  bubbleSort(numbers)
  fmt.Println(numbers)
}

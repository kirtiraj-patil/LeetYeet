package main
import "fmt"
import "time"
import "math/rand"

func generateRandomNumbers(count int, min int, max int) []int {
	// Seed the random number generator
	rand.Seed(time.Now().UnixNano())

	// Create a slice to hold the random numbers
	numbers := make([]int, count)

	// Generate random numbers
	for i := 0; i < count; i++ {
		numbers[i] = rand.Intn(max-min+1) + min
	}

	return numbers
}

func merge(left []int, right []int) []int {
  var resultArr []int;
  leftLen := len(left)
  rightLen := len(right)
  i := 0
  j := 0
  
  for i < leftLen && j < rightLen {
    if left[i] > right[j] {
      resultArr = append(resultArr, right[j])
      j++
    } else {
      resultArr = append(resultArr, left[i])
      i++
    }
  }
  
  for i < leftLen {
    resultArr = append(resultArr, left[i])
    i++
  }
  for j < rightLen {
    resultArr = append(resultArr, right[j])
    j++
  }
  
  return resultArr
}

func mergeSort(arr []int) []int {
  if len(arr) < 2 {
    return arr
  }
  
  mid := len(arr) / 2
  var sortedLeft []int = mergeSort(arr[0:mid])
  var sortedRight []int = mergeSort(arr[mid:len(arr)])
  return merge(sortedLeft, sortedRight)
}

func main() {
  numbers := generateRandomNumbers(1000, 0, 10000)
  fmt.Println(numbers)
  startTime := time.Now()
  res := mergeSort(numbers)
  fmt.Println(time.Since(startTime))
  fmt.Println(res)
  // fmt.Println((1 + 2)/2)
}

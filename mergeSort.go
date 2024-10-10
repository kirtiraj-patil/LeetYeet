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

// package main
// import "fmt"
// import "time"
// import "math/rand"

// func generateRandomNumbers(count int, min int, max int) []int {
// 	// Seed the random number generator
// 	rand.Seed(time.Now().UnixNano())

// 	// Create a slice to hold the random numbers
// 	numbers := make([]int, count)

// 	// Generate random numbers
// 	for i := 0; i < count; i++ {
// 		numbers[i] = rand.Intn(max-min+1) + min
// 	}

// 	return numbers
// }

// func merge(left []int, right []int) []int {
//   var resultArr []int;
//   leftLen := len(left)
//   rightLen := len(right)
//   i := 0
//   j := 0
  
//   for i < leftLen && j < rightLen {
//     if left[i] > right[j] {
//       resultArr = append(resultArr, right[j])
//       j++
//     } else {
//       resultArr = append(resultArr, left[i])
//       i++
//     }
//   }
  
//   for i < leftLen {
//     resultArr = append(resultArr, left[i])
//     i++
//   }
//   for j < rightLen {
//     resultArr = append(resultArr, right[j])
//     j++
//   }
  
//   return resultArr
// }

// func mergeSort(arr []int, ch chan<- []int) {
//   if len(arr) < 2 {
//     ch<-arr
//   } else {
//   ch1 := make(chan []int)
//   ch2 := make(chan []int)
  
//   mid := len(arr) / 2
//   go mergeSort(arr[0:mid], ch1)
//   go mergeSort(arr[mid:len(arr)], ch2)
  
//   sortedLeft := <-ch1
//   sortedRight := <-ch2
//   ch <- merge(sortedLeft, sortedRight)
//   }
// }

// func main() {
//   numbers := generateRandomNumbers(1000, 0, 10000)
//   fmt.Println(numbers)
//   ch := make(chan []int)
  
//   startTime := time.Now()
//   go mergeSort(numbers, ch)
//   res := <-ch
//   fmt.Println(time.Since(startTime))
  
//   fmt.Println(res)
//   // fmt.Println((1 + 2)/2)
// }

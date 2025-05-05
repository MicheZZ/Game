package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"strings"
	"time"
)

var balance int

func main() {
	fmt.Println("При обнаружении багов пишите мне на почту - pythonerkk@mail.ru")
	fmt.Println("Нужно кинуть скрин недоработки")
	fmt.Println()
	fmt.Println("______________________________________________________")
	fmt.Println()

	rand.Seed(time.Now().UnixNano())
	reader := bufio.NewReader(os.Stdin)

	for {
		playGame(reader)
		fmt.Printf("\nТвой общий счёт = %d\n", balance)
		fmt.Println("\n______________________________________________________\n")
		fmt.Print("Продолжаем игру? (да/нет): ")
		choice, _ := reader.ReadString('\n')
		choice = strings.TrimSpace(strings.ToLower(choice))
		if choice == "нет" {
			break
		}
	}
	fmt.Println("Для закрытия консоли нажми 'ENTER'")
	fmt.Println("Made by MicheZZ")
	reader.ReadString('\n')
}

func playGame(reader *bufio.Reader) {
	fmt.Println("Выбери уровень сложности:")
	fmt.Println("1 уровень от 1 до 100")
	fmt.Println("2 уровень от 1 до 250")
	fmt.Println("3 уровень от 1 до 500")
	fmt.Println("4 уровень от 1 до 1000")
	fmt.Println("5 уровень от 1 до 2000")

	var level int
	for {
		fmt.Print("Введи номер уровня: ")
		input, _ := reader.ReadString('\n')
		input = strings.TrimSpace(input)
		num, err := strconv.Atoi(input)
		if err == nil && num >= 1 && num <= 5 {
			level = num
			break
		}
		fmt.Println("Ошибка! Введите целое число от 1 до 5")
	}

	var maxNumber, maxAttempts, reward int
	switch level {
	case 1:
		maxNumber = 100
		maxAttempts = 6
		reward = 500
	case 2:
		maxNumber = 250
		maxAttempts = 7
		reward = 800
	case 3:
		maxNumber = 500
		maxAttempts = 8
		reward = 1000
	case 4:
		maxNumber = 1000
		maxAttempts = 9
		reward = 1200
	case 5:
		maxNumber = 2000
		maxAttempts = 10
		reward = 1500
	}

	secret := rand.Intn(maxNumber) + 1
	fmt.Printf("Угадай число от 1 до %d за %d попыток. За лишнюю попытку у тебя будет сниматься по 100 очков\n", maxNumber, maxAttempts)
	fmt.Printf("За прохождение %d уровня можно получить %d очков\n", level, reward)

	attempts := 0
	for {
		attempts++
		fmt.Printf("Твоя %d попытка - ", attempts)
		input, _ := reader.ReadString('\n')
		input = strings.TrimSpace(input)
		guess, err := strconv.Atoi(input)
		if err != nil {
			fmt.Println("Ошибка! Введите целое число")
			attempts--
			continue
		}

		if guess > secret {
			fmt.Println("Много. Попробуй ввести число меньшего значения")
		} else if guess < secret {
			fmt.Println("Мало. Попробуй ввести число большего значения")
		} else {
			points := reward - ((attempts - maxAttempts) * 100)
			if points < 0 {
				points = 0
			}
			balance += points
			fmt.Println("\n______________________________________________________\n")
			fmt.Printf("Молодец! Ты угадал число. Твой счёт увеличился на %d очков\n", points)
			break
		}
	}
}

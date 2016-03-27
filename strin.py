#!/usr/bin/python3

import string
import random


def main():
    input_string = input("Enter the goal string: ")

    input_num_array = string_to_num_array(input_string)
    print("Input number array: " + str(input_num_array))

    input_array_average = array_average(input_num_array)
    print("Array average: " + str(input_array_average))

    machine_string = randomize_string(input_string)
    print("machine_string = " + machine_string)

    while True:
        machine_count = 6
        machine_string_array = []

        for i in range(machine_count):
            machine_string_array.append(machine_string)

        letter_flip_probability = 5  # percent~
        bastard_array = []
        for machine in machine_string_array:
            bastard_array.append(
                mutate_string(machine, letter_flip_probability)
            )

        machine_string_array = bastard_array

        bastard_array = []
        for machine in machine_string_array:
            tmp = array_average(string_to_num_array(machine))
            bastard_array.append(tmp)
        print(machine_string_array)
        print(bastard_array)

        placeholder = 10.0
        placeholder2 = int
        for idx, val in enumerate(bastard_array):
            test2 = abs(val / input_array_average)
            if(test2 < placeholder):
                placeholder2 = idx
        machine_string = machine_string_array[placeholder2]


def mutate_string(instring, rand_probability):
    output = ""
    for letter in instring:
        if(random.randint(0, 99) < rand_probability):
            output += random.choice(string.printable)
        else:
            output += letter
    return output


def randomize_string(i):
    output = ""
    for letter in i:
        output += random.choice(string.printable)
    return output


def string_to_num_array(i):
    array_num = []
    for letter in i:
        letter_to_num = ord(letter)
        array_num.append(letter_to_num)
    return array_num


def array_average(i):
    # averages numbers in array
    array_sum = 0
    count = 0
    for num in i:
        array_sum += num
        count += 1
    average = array_sum / count
    return average


def array_count(i):
    count = 0
    for letter in i:
        count += 1
    return count

if __name__ == "__main__":
    main()

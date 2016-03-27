#!/usr/bin/python3

import string
import random
import time
import sys


def main():
    input_string = input("Enter the goal string: ")

    input_num_array = string_to_num_array(input_string)
    print("Input number array: " + str(input_num_array))

    input_array_average = array_average(input_num_array)
    time.sleep(3)

    machine_string = randomize_string(input_string)
    print("machine_string = " + machine_string)

    letter_flip_probability = 5  # percent~

    while True:
        machine_count = 200
        machine_string_array = create_machine_string_array(
            machine_string, machine_count
        )

        machine_string_array = mutate_array_strings(
            machine_string_array, letter_flip_probability
        )

        output = string_array_to_num_array(machine_string_array)

        output2 = num_list_dist_find(output, input_num_array)

        output3 = create_averaged_num_array(output2)

        m = min(output3)
        for idx, val in enumerate(output3):
            if val == m:
                machine_string = machine_string_array[idx]
        print(machine_string)
        if(m == 0):
            sys.exit()


def create_averaged_num_array(input_array):
    # Given array of arrays of numbers, return array of averaged numbers
    output = []
    for num_list in input_array:
        j = array_average(num_list)
        output.append(j)
    return output


def num_list_dist_find(input_list, compare_list):
    # given array of array of numbers, return array with list of
    # distances from same idx points in compare_list
    output = []
    for num_list in input_list:
        j = dist_find(num_list, compare_list)
        output.append(j)
    return output


def string_array_to_num_array(in_string_array):
    output = []
    for instring in in_string_array:
        num_array = string_to_num_array(instring)
        output.append(num_array)
    return output


def dist_find(array1, array2):
    # given two arrays of numbers, find average of both arrays for each
    # thing in list.
    # eg 1 = [a, b]; 2 = [b, c]; output = [abs(a-b), abs(b-c)]
    output = []
    for idx, val in enumerate(array1):
        m = abs(val - array2[idx])
        output.append(m)
    return(output)


def create_dist_averaged_array(array_to_average, input_array_average):
    output_array = []
    for num in array_to_average:
        dist = abs(num - input_array_average)
        output_array.append(dist)
    return output_array


def find_best_string(tmp_array, input_array_average):
    # For given array of numbers, find int
    # where tmp_array[return_value] is closest to averaged_num_array
    placeholder = 10.0
    placeholder2 = 0
    for idx, val in enumerate(tmp_array):
        dist = abs(val - input_array_average)
        if(dist < placeholder):
            placeholder2 = idx
            placeholder = dist
    return(int(placeholder2))


def create_array_average(input_array):
    output_array = []
    for input_string in input_array:
        num_array = string_to_num_array(input_string)
        num_array_avg = array_average(num_array)
        output_array.append(num_array_avg)
    return output_array


def mutate_array_strings(machine_string_array, letter_flip_probability):
    output_array = []
    for machine in machine_string_array:
        output_array.append(
            mutate_string(machine, letter_flip_probability)
        )
    return output_array


def create_machine_string_array(machine_string, machine_count):
    machine_string_array = []
    for i in range(machine_count):
            machine_string_array.append(machine_string)
    return machine_string_array


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

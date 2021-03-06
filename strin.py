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

    letter_flip_probability = 7  # percent~

    while True:
        machine_count = 200
        machine_string_array = create_machine_string_array(
            machine_string, machine_count
        )

        machine_string_array = mutate_array_strings(
            machine_string_array, letter_flip_probability
        )

        machine_num_array = string_array_to_num_array(machine_string_array)

        machine_dist_array = num_list_dist_find(
            machine_num_array,
            input_num_array
            )

        output3 = create_averaged_num_array(machine_dist_array)

        # finds first and second best ones
        m = min(output3)
        j = 0
        for idx, val in enumerate(output3):
            if val == m:
                j = idx
        k = output3[j]
        n = output3[find_second_min_from_array(output3)]

        bred_machines = breed(
            machine_num_array,
            j,
            find_second_min_from_array(output3)
            )

        # print(str(k) + " " + str(n))
        # print("min:\t\t" + str(machine_num_array[j]))
        # print("second min:\t" + str(machine_num_array[find_second_min_from_array(output3)]))
        # print("bred array:\t" + str(bred_machines))

        # Recalculates after breeding machine
        machine_num_array.pop()
        machine_num_array.append(bred_machines)
        # print("Pre: " + str(machine_string_array))
        machine_string_array = num_array_to_string_array(machine_num_array)
        # print("Post: " + str(machine_string_array))

        machine_dist_array = num_list_dist_find(
            machine_num_array, input_num_array
            )

        output3 = create_averaged_num_array(machine_dist_array)

        # Assigns the number closest to base array as new machien string
        m = min(output3)
        for idx, val in enumerate(output3):
            if val == m:
                machine_string = machine_string_array[idx]
        print(machine_string)
        if(m == 0):
            sys.exit()


def num_array_to_string_array(input_num_array):
    string_array = []
    output = []
    for num_array in input_num_array:
        out = ""
        for num in num_array:
            m = chr(num)
            out += m
        string_array.append(out)
    return string_array


def breed(input_num_array, best_min_idx, sec_min_idx):
    output = []
    for idx, val in enumerate(input_num_array[0]):
        n = abs(
            (
                input_num_array[best_min_idx][idx] +
                input_num_array[sec_min_idx][idx]
            )/2
            )
        output.append(int(n))
    return output


def find_second_min_from_array(input_array):
        m1 = 500000
        m2 = 500000
        goal, not_goal = 0, 0
        for idx, val in enumerate(input_array):
            if val < m2:
                if val <= m1:
                    m1, m2 = val, m1

                else:
                    m2 = val
                    goal = idx
        return goal


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
    for idx, machine in enumerate(machine_string_array):
        if(idx == 0):
            output_array.append(machine)
        else:
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

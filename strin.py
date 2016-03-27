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
    print("Array average: " + str(input_array_average))
    time.sleep(3)

    machine_string = randomize_string(input_string)
    print("machine_string = " + machine_string)

    while True:
        machine_count = 200
        machine_string_array = create_machine_string_array(
            machine_string, machine_count
        )

        letter_flip_probability = 5  # percent~
        machine_string_array = mutate_array_strings(
            machine_string_array, letter_flip_probability
        )
        
        output = []
        for mch_str in machine_string_array:
            #mch_str_num_array = string_to_num_array(mch_str)
            output.append(string_to_num_array(mch_str))
        
        output2 = []
        for num_list in output:
            j = dist_find(num_list, input_num_array)
            output2.append(j)
            
        output3 = []
        for num_list in output2:
            j = array_average(num_list)
            output3.append(j)
        
        m = min(output3)
        for idx, val in enumerate(output3):
            if val == m:
                machine_string = machine_string_array[idx]
        print(machine_string)
        if(m == 0):
            sys.exit()
        #average_dist_array = create_dist_averaged_array(machine_string_array)
        
        #averaged_num_array = create_array_average(machine_string_array, input_array_average)

        #print(machine_string_array)
        #print(averaged_num_array)

        #machine_string = machine_string_array[find_best_string(
        #    averaged_num_array, input_array_average)]

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

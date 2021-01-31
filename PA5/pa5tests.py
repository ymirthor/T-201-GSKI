from hashmap import *
import random
from myhashablekey import *
import string


def random_generator():
    """This is just a test function that random generates numbers and inserts
    them into the HashMap"""
    rnd = random.Random()
    user_bucket = HashMap()
    for i in range(1000):
        number = rnd.randint(0, 1000000)
        rnd_string = randomString(random.randint(1,15)) #Generates random string of length 0-15
        temp_key = MyHashableKey(number, rnd_string)
        try:
            user_bucket.insert(hash(temp_key), "cool")
        except ItemExistsException:
            print("found duplicate", i)
    a_list = how_many_in_bucket(user_bucket)
    return a_list

def how_many_in_bucket(user_bucket):
    """Returns a list with the count of items in each bucket"""
    ret_list = []
    for i in range(len(user_bucket)):
        ret_list.append(len(user_bucket.table[i]))
    return ret_list

def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def visualize(a_list):
    result_max = max(a_list)
    result_min = min(a_list)
    diffrence = result_max - result_min
    ratio = diffrence / result_max
    print("Distribution ratio: {:.10f}".format(ratio))
    print("Bucket with the most items had: " + str(result_max) + " items.")
    print("Bucket with the least items had: " + str(result_min)+ " items.")


my_result = random_generator()
print(my_result)
visualize(my_result)
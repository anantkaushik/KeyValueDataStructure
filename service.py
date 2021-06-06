from kv_ds import KeyValueDataStructure

hash_map = KeyValueDataStructure()


def print_options():
    print("1. Insert")
    print("2. Retrieve")
    print("3. Display Current State")
    print("4. Exit")
    print("Type the number corresponding to the operation you want to perform:")


while True:
    print_options()
    try:
        option = int(input())
    except ValueError:
        print("Invalid Option.")
        continue

    if option == 4:
        print("Bye!")
        break
    elif option == 3:
        result = hash_map.display()
        for pair in result:
            print(pair)
    elif option == 2:
        print("Enter the Key:")
        try:
            key = int(input())
        except ValueError:
            print("Invalid Key Value.")
            continue
        print(hash_map.get(key))
    elif option == 1:
        print("Enter the Key:")
        try:
            key = int(input())
        except ValueError:
            print("Invalid Key Value.")
            continue

        print("Enter the Value:")
        value = str(input())
        hash_map.set(key, value)
    else:
        print("Invalid Option.")

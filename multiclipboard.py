import sys
import json
import clipboard

saved_data = "clipboard.json"

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(saved_data)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(saved_data, data)
        print("Data saved!")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
        else:
            print("Key doesn't exist.")
    elif command == "list":
        print(data)
    else:
        print("Unknown command.")
else:
    print("Please enter exactly one command.")


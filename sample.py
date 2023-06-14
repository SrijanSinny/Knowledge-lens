import json


def parsing():
    opening_file = open("sample_data (1).json", "r")
    sampledata = json.load(opening_file)
    # print(sampledata)
    data = sampledata["parametersList"]
    required_list = []
    for parameter in data:
        dict_parameter = {'parameter_name': parameter["parameterName"], 'min_value': parameter["min"],
                          'max_value': parameter["max"], 'avg_value': parameter["avg"]}
        # print(dict_parameter)
        required_list.append(dict_parameter)
    print(required_list)
    with open("sample_data2.json", "w") as file:
        converting_file = file.write(json.dumps(required_list, indent=2))
        print(converting_file)


if __name__ == "__main__":
    parsing()

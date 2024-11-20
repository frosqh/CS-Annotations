import argparse

from kv3parser import KV3Parser


def define_parser():
    parser = argparse.ArgumentParser(description="Allows to patch nades setup")
    parser.add_argument("file", help="The file to patch", type=argparse.FileType('r'))
    parser.add_argument("--all", "-a", help="Do all patches", action="store_true")
    parser.add_argument("--standing", "-s", help="Patch standing description", action="store_true")
    parser.add_argument("--throw", "-t", help="Patch throw description", action="store_true")
    return parser


def get_json(file):
    data = file.read()
    try:
        kv3 = KV3Parser(data)
        parsed_data = kv3.parse()
    except Exception as e:
        raise Exception(f"Could not parse : {e}")
    return parsed_data


def get_number_of_nodes(data):
    return sum("MapAnnotationNode" in k for k in data)


if __name__ == "__main__":
    arg_parser = define_parser()
    args = arg_parser.parse_args()
    content = get_json(args.file)
    print(f"Considering setups for map {content['MapName']}")
    N = get_number_of_nodes(content)
    for n in range(N):
        node = content[f'MapAnnotationNode{n}']
        if node['Type'] == 'grenade':
            print(f"Considering stuff named {node['Title']['Text']}")
            if (args.standing or args.all) and node['SubType'] == 'main':
                print("Current standing instruction is :")
                print(f"\t {node['Desc']['Text']}")
                change = input("Would you like to change it ? Y/(N)\n")
                if change == 'Y' or change == '':
                    new_desc = input("Enter new standing instruction : ")
                    content[f'MapAnnotationNode{n}']['Desc']['Text'] = new_desc
            if (args.standing or args.all) and node['SubType'] == 'aim_target':
                print("Current throwing instruction is :")
                print(f"\t {node['Desc']['Text']}")
                change = input("Would you like to change it ? Y/(N)\n")
                if change == 'Y' or change == '':
                    new_desc = input("Enter new throwing instruction : ")
                    content[f'MapAnnotationNode{n}']['Desc']['Text'] = new_desc
    print(content)

import os
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-b', '--before', help='before string', required=True)
    parser.add_argument('-a', '--after', default="", help='after string defualt is "" ')
    parser.add_argument('-p', '--path', help="directory path", required=True)

    args = parser.parse_args()

    path = args.path
    
    files = os.listdir(path)
    for file in files:
        if args.before in file:
            before = os.path.join(path, file)
            after = os.path.join(path, file.replace(args.before, args.after).strip())
            os.rename(before, after)
            print(before + " => " + after)
            
import os
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-b', '--before', help='before string', required=True)
    parser.add_argument('-a', '--after', default="", help='after string defualt is "" ')
    parser.add_argument('-p', '--path', help="directory path", required=True)
    parser.add_argument('-s', '--strip', type=bool, help="after replace use strip")

    args = parser.parse_args()

    path = args.path
                
    files = [os.path.splitext(file) for file in os.listdir(path)]
    for name, fmt in files:
        if args.before in name:
            before = os.path.join(path, name + fmt)
            after = name.replace(args.before, args.after).strip()
            if args.strip:
                after = os.path.join(path, after.strip())
            else:
                after = os.path.join(path, after)
            
            os.rename(before, after)
            print(before + " => " + after)
            
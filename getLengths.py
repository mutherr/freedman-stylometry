import argparse
import os


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("directory",help="The directory to prcoess")
    args = parser.parse_args()

    for file in os.listdir(args.directory):
        text = open(os.path.join(args.directory,file)).read()
        tokens = text.split()
        print(f"{file}\t{len(tokens)}")
import argparse
from get_differences import get_differences


def main():
    
    parser = argparse.ArgumentParser()

    parser.add_argument('--file1', required = True)
    parser.add_argument('--file2', required = True)

    args = parser.parse_args()

    get_differences(args.file1, args.file2)



if __name__ == '__main__':
    main()
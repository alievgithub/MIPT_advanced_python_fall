import sys
import argparse

def FiboSeq(n):

	n1, n2 = 0, 1
	for i in range(n):
		n1, n2 = n2, n1 + n2

	return n1


def CreateParser():

	parser = argparse.ArgumentParser()
	parser.add_argument('-n')

	return parser


if __name__ == "__main__":

    try:
        n = int(sys.argv[1])
        print(FiboSeq(n))
    except:
        parser = CreateParser()
        namespace = parser.parse_args()
        print(FiboSeq(int(namespace.n)))

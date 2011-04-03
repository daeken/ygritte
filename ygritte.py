import sys

from game import Game

def main():
	Game().run()

if __name__=='__main__':
	sys.exit(main(*sys.argv[1:]))

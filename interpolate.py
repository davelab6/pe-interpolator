import sys, os

def interpolate( font1, font2, fileName ):
    file = open( fileName, 'r' )

    for line in file:
        fontInfo = line.split()
        os.system( "./interpolate.pe " + font1 + " " + font2 + " " + fontInfo[0] + ".ttf" + " " + fontInfo[1] )


def main( argv ):
    interpolate( argv[1], argv[2], argv[3] )

if __name__ == "__main__":
    main( sys.argv )

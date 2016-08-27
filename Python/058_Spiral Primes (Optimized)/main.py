import corners_generator
import is_prime

def main():
    corners = corners_generator.gen_square_corners()
    sideLength = 1
    noOfPrimes = 0
    ratio = 0

    while ratio > 0.10 or ratio == 0:
        sideLength += 2
        cornersOfSquare = next(corners)

        for corner in cornersOfSquare:
            if is_prime.isprime(corner):
                noOfPrimes += 1

        noInDiagonal = sideLength * 2 - 1
        ratio = noOfPrimes / noInDiagonal

    return(sideLength)

if __name__ == '__main__':
    print("The side length of the spiral when the ratio falls below 10%% is %d" % main())

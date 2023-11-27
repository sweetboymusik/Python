import time
import tqdm

# read defauls and set constants
f = open("Defaults.dat", "r")
MOVIE_ID = int(f.readline())
HST_RATE = float(f.readline())
NEW_REL_DAYS = int(f.readline())
WKS_TO_OBS = int(f.readline())
f.close

# main program
while True:
    movie_name = input("Movie name: ")
    movie_type = input("Movie type (D, C, M, or H): ").upper()
    movie_rating = input("Movie rating (G, P, or R): ").upper()
    rental_cost = float(input("Rental cost (1.99 - 8.99): "))

    for i in range(0, 11):
        if i < 10:
            print(f"Saving... {i}0%", end="\r", flush=True)
        else:
            print(f"Saving... {i}0%")
            print("Data successfully written.")
        time.sleep(0.1)

    # write data to file
    f = open("movies.dat", "a")

    f.write(f"{MOVIE_ID}, ")
    f.write(f"{movie_name}, ")
    f.write(f"{movie_type}, ")
    f.write(f"{movie_rating}, ")
    f.write(f"{rental_cost}\n")

    f.close()

    # update constants
    MOVIE_ID += 1

    print("Movie info successfully saved.")

    cont = input("Add another?: ").upper()
    if cont == "N":
        f = open("Defauls.dat", "w")
        f.write(f"{MOVIE_ID}\n")
        f.write(f"{HST_RATE}\n")
        f.write(f"{NEW_REL_DAYS}\n")
        f.write(f"{WKS_TO_OBS}\n")
        f.close()

        break

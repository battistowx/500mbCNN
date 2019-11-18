import multiprocessing as mp
from PIL import Image
import glob

def transparent(i):
    for filename in glob.glob("C:/Users/Chris Battisto/Desktop/Python projects/PracPerfect/test/0/*.png"):
        img = Image.open(filename)
        img = img.convert("RGBA")
        
        pixdata = img.load()
        
        width, height = img.size
        for y in range(height):
            for x in range(width):
                if pixdata[x, y] == (255, 255, 255, 255):
                    pixdata[x, y] = (255, 255, 255, 0)
        
        img.save(filename, "PNG")


if __name__ == '__main__':
    numprocs=mp.cpu_count() - 1
    pool=mp.Pool(processes=numprocs)
    r2=pool.map(transparent, range(0,16))
    pool.close()
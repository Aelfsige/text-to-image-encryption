from PIL import Image
import numpy as np

def textToPixels():
    text = input('Enter a plaintext: ')

    while len(text) % 3 != 0:
        text += '~'
    
    pixels = [
        [ord(text[0+i]), ord(text[1+i]), ord(text[2+i])] 
        for i in range(0, len(text), 3)
    ]

    return pixels

def createPixelValue(pixels):
    arr = np.zeros((8, 8, 3), np.int16)
    row = 0
    col = 0

    for item in pixels:
        arr[col, row] = item
        col += 1
        if col == 8:
            row += 1
            col = 0

    return arr

def encrypt(arr):
    img = Image.open('frame_sample.png')
    width, height = img.size

    for x in range(width):
        for y in range(height):
            img.putpixel((y, x), tuple(arr[y, x]))
    
    img.show()
    img.save('sample.png')

def decrypt():
    img_path = input('Enter image path: ')
    img = Image.open(img_path)
    pix = img.load()
    row = 8
    col = 8
    text = ''
    pixels = []

    for r in range(row):
        for c in range(col):
            if pix[c, r] == (0, 0, 0, 255):
                break 
            pixels.append(pix[c, r])
    
    for p in pixels:
        text += str(chr(p[0]))
        text += str(chr(p[1]))
        text += str(chr(p[2]))
    
    with open('sample.txt', 'w') as f:
        f.write(text)
    
    print(text)

def main():
    print('===Image to Text Encryption===')
    isRunning = True
    
    while isRunning:
        try:
            choice = int(input('(1) Encrypt\n(2) Decrypt\n> '))

            match choice:
                case 1:
                    pixels = textToPixels()
                    pixel_value = createPixelValue(pixels)
                    encrypt(pixel_value)
                case 2:
                    decrypt()
        except ValueError:
            print('Please enter a valid choice.')

if __name__ == '__main__':
    main()

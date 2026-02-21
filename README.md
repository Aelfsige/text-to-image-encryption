# Text to Image Cryptography

1. Provide a plain text
2. The program translates each character to its ASCII decimal value
3. It stores 3 characters in one pixel, where red, green, blue is equivalent to a letter. The alpha value is constant to 255
4. It saves each pixel to an 8x8 image
5. To get the text, simply reverse the process by reading each pixel and convert the ASCII value back to text

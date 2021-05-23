import bs4
import base64

from Crypto.Cipher import DES

def pad(text):
    n = len(text) % 8
    return text + (b' ' * n)

key = input('Por favor, ingrese una llave de 8 caracteres (Puede intentar con hello123, hola1234, 12345678, etc.)\n')
while len(key) != 8:
    key = input('Recuerde, la llave debe tener 8 caracteres exactos (Puede intentar con hello123, hola1234, 12345678, etc.)\n')

text1 = input('Por favor, ingrese un mensaje a encriptar, este debe tener 28 caracteres (puede probar con "Este es un mensaje de prueba".)\n')
while len(text1) != 28:
    text1 = input('Recuerde, este debe tener 28 caracteres exactos (puede probar con "Este es un mensaje de prueba".)\n')

keyb = bytes(key, 'Utf-8')
text1 = bytes(text1, 'Utf-8')

print(keyb)
print(text1)
# text1 = encode(text1)

des = DES.new(keyb, DES.MODE_ECB)
padded_text = pad(text1)
encrypted_text = des.encrypt(padded_text)

print('El mensaje encriptado es:\n')
print(encrypted_text.hex())
print(des.decrypt(encrypted_text).decode('Utf-8'))


f = open('index.html','w')

message = """<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Mensaje Secreto</title>
  </head>
  <body>
<p>Este sitio contiene un mensaje secreto</p>
<script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0/crypto-js.min.js" integrity="sha512-nOQuvD9nKirvxDdvQ9OMqe2dgapbPB7vYAMrzJihw5m+aNcf0dX53m6YxM4LgA9u8e9eg9QX+/+mPu8kCNpV2A==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script src="./desecb.js"></script>
  </body>
</html>
"""

f.write(message)
f.close()

# load the file
with open("index.html") as inf:
    txt = inf.read()
    soup = bs4.BeautifulSoup(txt)
    soup1 = bs4.BeautifulSoup("<b></b>", 'html.parser')
    new_tag1 = soup1.new_tag("p")
    new_tag1.string = encrypted_text.hex()

attributes = {'class': 'algorithm', 'id': encrypted_text.hex()}
attributes1 = {'class': 'keypy', 'id': key}
# create new link
new_link = soup.new_tag('div', **attributes)
new_link1 = soup.new_tag('div', **attributes1)
# insert it into the document
soup.head.append(new_link)
soup.head.append(new_link1)
soup.head.append(new_tag1)


# save the file again
with open("index.html", "w") as outf:
    outf.write(str(soup))
print(des.decrypt(encrypted_text))

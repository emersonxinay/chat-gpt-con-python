# un chatgpt con python 

## paso a seguir 
### instalar o configurar nuestro entorno de desarrollo
#recuerda tener instalado python 3 o superior
```bash
pip install virtualenv
```
o 
```bash 
pip3 install virtualenv
```

## crear y activar el virtual env

```bash
virtualenv nombre_virtual_env
```
```bash
source nombre_virtual_env/bin/activate
```
## en el caso mio lo cree de la siguiente manera:
```bash
source env/bin/activate
```
## Para desactivar el virtual env solo escribir lo siguiente desde el terminal
```bash
deactivate
``` 

# ahora instalar los paquetes para chat gpt
```bash
pip install openai
```
```bash 
pip install python-dotenv

```
### recuerda sacar tu api_key de las documentación de chatgpt en el siguiente enlace.
<code>https://beta.openai.com/account/api-keys</code>
##### y luego te creas un archivo .env para poner el link recuerda que el ejemplo esta en el archivo .env.example

### hace funcionar compilando el archivo

```bash
python3 chat.py
```


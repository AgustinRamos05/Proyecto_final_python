
import json

#Registro de usuario
def register_user():
    cycle = True
    while cycle == True:
        print('Registrate')
        username = input('Nombre de usuario: ')
        password = input('Contraseña: ')
        
        database = {
                'username': username,
                'password': password
            }
        
        with open('database.json', 'r') as archive:
            data = json.load(archive)
            if username in data['username'] :
                print('Este nombre de usuario ya existe')
                continue
            else:
                with open('database.json', 'w') as archive:
                    json.dump(database, archive, indent= 4)
                    print('Usuario registrado correctamente')
                    break
              
 
#Visualizar usuarios registrados
def data_storage():
    print('Usuarios registrados: ')
    with open('database.json', 'r') as archive:
        data = json.load(archive)
        for username in data['username']:
            print(username)      
  
register_user()
data_storage()





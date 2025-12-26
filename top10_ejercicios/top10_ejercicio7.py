"""✅ 7. Registro de usuarios

Clase Usuario:

__usuario,__password

Clase SistemaUsuarios:

Lista de usuarios

registrar_usuario()

iniciar_sesión()

Usuarios se guardan en archivo plano

📌 Práctica:

Encapsulamiento + listas + archivos + lógica"""


class Usuario:
    """
    Representa a un usuario del sistema con credenciales protegidas.
    """

    def __init__(self, usuario: str, password: str):
        """
        Inicializa un nuevo usuario.

        Args:
            usuario (str): El nombre de usuario.
            password (str): La contraseña del usuario.
        """
        self.__usuario = usuario
        self.__password = password

    def get_usuario(self):
        """Devuelve el nombre de usuario."""
        return self.__usuario

    def get_password(self):
        """Devuelve la contraseña del usuario."""
        return self.__password


class SistemaUsuarios:
    """
    Gestiona el registro y autenticación de usuarios, persistiendo los datos en un archivo de texto.
    """

    def __init__(self, archivo="usuarios.txt"):
        """
        Inicializa el sistema de usuarios y carga los datos existentes.

        Args:
            archivo (str): Nombre del archivo donde se guardarán los usuarios. Por defecto 'usuarios.txt'.
        """
        self.archivo = archivo
        self.usuarios = []
        self.cargar_usuarios()

    def cargar_usuarios(self):
        """
        Lee el archivo de usuarios y carga los datos en la lista en memoria.
        Si el archivo no existe, omite la carga.
        """
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    if not linea.strip():
                        continue
                    usuario, password = linea.strip().split(",")
                    self.usuarios.append(Usuario(usuario, password))
        except FileNotFoundError:
            pass

    def registrar_usuario(self, usuario, password):
        """
        Registra un nuevo usuario si no existe previamente y lo guarda en el archivo.

        Args:
            usuario (str): Nombre de usuario a registrar.
            password (str): Contraseña del usuario.
        """
        for u in self.usuarios:
            if u.get_usuario() == usuario:
                print("❌ Usuario ya existe")
                return

        nuevo = Usuario(usuario, password)
        self.usuarios.append(nuevo)

        with open(self.archivo, "a", encoding="utf-8") as f:
            f.write(f"{usuario},{password}\n")

        print("✅ Usuario registrado correctamente")

    def iniciar_sesion(self, usuario, password):
        """
        Verifica las credenciales de un usuario para iniciar sesión.

        Args:
            usuario (str): Nombre de usuario.
            password (str): Contraseña.
        """
        for u in self.usuarios:
            if u.get_usuario() == usuario and u.get_password() == password:
                print("🔓 Sesión iniciada correctamente")
                return

        print("❌ Usuario o contraseña incorrectos")


sistema = SistemaUsuarios()

sistema.registrar_usuario("luis", "1234")
sistema.registrar_usuario("ana", "abcd")

sistema.iniciar_sesion("luis", "1234")
sistema.iniciar_sesion("luis", "0000")

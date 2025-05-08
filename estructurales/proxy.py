import os

class Ping:
    def execute(self, ip: str):
        if ip.startswith("192."):
            print(f"[Ping] Ejecutando ping a {ip} (con control de IP)...")
            os.system(f"ping -c 10 {ip}")
        else:
            print("[Ping] Dirección IP no permitida. Debe comenzar con '192.'")

    def executefree(self, ip: str):
        print(f"[Ping] Ejecutando ping libre a {ip} (sin control de IP)...")
        os.system(f"ping -c 10 {ip}")


class PingProxy:
    def __init__(self):
        self.real_ping = Ping()

    def execute(self, ip: str):
        if ip == "192.168.0.254":
            print("[Proxy] Dirección especial detectada. Redirigiendo ping a www.google.com...")
            self.real_ping.executefree("www.google.com")
        else:
            print("[Proxy] Pasando solicitud a Ping con validación...")
            self.real_ping.execute(ip)

if __name__ == "__main__":
    # Ejemplo de uso
    print("Ejemplo de uso del patrón Proxy:")
    print("Ejecutando ping a diferentes direcciones IP...")
    # Crear una instancia del proxy
    proxy = PingProxy()

# Caso válido
    proxy.execute("192.168.0.1")  # Ejecuta ping a 192.168.0.1 (con control)

# Caso especial
    proxy.execute("192.168.0.254")  # Redirige a www.google.com usando executefree

# Caso no válido (no comienza con 192.)
    proxy.execute("10.0.0.1")  # No ejecuta ping

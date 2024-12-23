import os
import subprocess
import time
import resource

def find_source_file() -> str:
    """
    Busca automáticamente un archivo fuente (.cpp o .py) en el directorio actual.
    """
    for file in os.listdir():
        if file.endswith('.cpp') or file.endswith('.py'):
            return file
    raise FileNotFoundError("No se encontró ningún archivo fuente (.cpp o .py) en el directorio.")

def compile_program(source_file: str) -> str:
    """
    Compila el programa si es necesario y retorna el nombre del ejecutable.
    """
    if source_file.endswith('.cpp'):
        executable = './program'
        result = subprocess.run(['g++', source_file, '-o', executable], capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"Error de compilación:\n{result.stderr}")
        return executable
    elif source_file.endswith('.py'):
        return f'python3 {source_file}'  # Los scripts Python no requieren compilación
    else:
        raise ValueError("Archivo no soportado. Solo se aceptan .cpp y .py")

def run_algorithm(command: str, input_data: str, time_limit: float, memory_limit: int):
    """
    Ejecuta un programa con límites de tiempo y memoria configurados.
    """
    try:
        start_time = time.time()
        memory_limit_bytes = memory_limit * 1024 * 1024

        process = subprocess.Popen(
            command.split(),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        try:
            output, error = process.communicate(input=input_data, timeout=time_limit)
            execution_time = time.time() - start_time

            memory_used = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss * 1024

            if memory_used > memory_limit_bytes:
                return "Memory Limit Exceeded", execution_time, memory_used / (1024 * 1024)

            return output.strip(), execution_time, memory_used / (1024 * 1024)

        except subprocess.TimeoutExpired:
            process.kill()
            return "Time Limit Exceeded", time_limit, 0

    except Exception as e:
        return f"Runtime Error: {str(e)}", 0, 0

def main():
    try:
        # Detectar archivo fuente automáticamente
        source_file = find_source_file()
        print(f"Archivo detectado: {source_file}")

        # Configuración
        input_data = "3 5\n"               # Entrada de prueba
        time_limit = 1.0                   # Tiempo límite en segundos
        memory_limit = 256                 # Límite de memoria en MB

        # Compilación automática
        command = compile_program(source_file)
        
        # Ejecutar con límites
        result, time_used, memory_used = run_algorithm(command, input_data, time_limit, memory_limit)

        # Resultados
        print(f"Resultado: {result}")
        print(f"Tiempo usado: {time_used:.3f}s")
        print(f"Memoria usada: {memory_used:.2f}MB")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()

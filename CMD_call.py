import subprocess

sln_path = r"C:\Users\falearn\source\repos\my_dll_1\my_dll_1.vcxproj"  # файл проекта
msbuild_path = r"C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\MSBuild\Current\Bin\MSBuild.exe"   #файл сборщика
rebuild_command = [msbuild_path, sln_path, "/t:Rebuild", "/p:Configuration=Release", "/p:platform=x64"]

# Убедитесь, что скрипт Python находится в правильной директории
subprocess.run(["python", "the_func_generationHfile.py"], check=True)

try:
    # Запуск сборки проекта
    result = subprocess.run(rebuild_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("STDOUT:", result.stdout)
    print("Успешная пересборка DLL.")
except subprocess.CalledProcessError as e:
    # Вывод информации об ошибке
    print("Ошибка при пересборке DLL:")
    print(e.stdout)  # Вывод сообщений процесса
    print("STDERR:", e.stderr)  # Вывод сообщений об ошибках


#  MsBuild C:\Users\falearn\source\repos\my_dll_1\my_dll_1.vcxproj /t:Rebuild /p:Configuration=Release /p:platform=x64
#  MsBuild C:\Users\falearn\source\repos\the_func\the_func.sln /t:Rebuild /p:Configuration=Release /p:platform=x64

#  cd C:\Users\falearn\source\repos\the_func\x64\Release
#  the_func.exe 0 C:\Users\falearn\source\repos\the_func
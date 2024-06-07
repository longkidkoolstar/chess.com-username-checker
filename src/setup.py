from cx_Freeze import setup, Executable

setup(
    name="nazuna",
    version="1.0",
    description="Chess.com Checker by Austin @memorises on discord",
    executables=[Executable("checker.py", icon="nazuna.ico")],
)

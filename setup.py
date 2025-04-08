from cx_Freeze import setup, Executable

setup(
    name="Chomsky",
    version="1.0",
    executables=[Executable("Chomsky_A_Greibach.py")]
)
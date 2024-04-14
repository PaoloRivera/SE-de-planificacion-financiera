"""
Sistema experto
"""
import interfaz.menu as menu
from acciones import engine


def main():
    engine.base.from_json("planificacion_financiera.json")  
    app = menu.Interfaz()
    app.mainloop()


if __name__ == '__main__':
    main()

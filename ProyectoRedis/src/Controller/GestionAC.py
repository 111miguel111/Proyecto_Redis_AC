from ProyectoRedis.src.Controller import Utiles, iGestores
from ProyectoRedis.src.Model import GestorBBDD


class GestionAC(iGestores.iGestores):
    @staticmethod
    def alta():
        print("ALTA")

    @staticmethod
    def baja():
        print("BAJA")

    @staticmethod
    def modificar():
        print("MODIFICAR")

    @staticmethod
    def menuModificar():
        print("MENU MODIFICAR")

    @staticmethod
    def buscar():
        print("BUSCAR")

    @staticmethod
    def mostrarTodos():
        print("MOSTRAR TODOS")
        print(

            "\n                                         *(                 " +
            "\n                    /  *,,               (#(                " +
            "\n                   (#,....#  .       *   /%@(               " +
            "\n                ,*%(,//%-----------------------------------RS Weapon:" +
            "\n               *(&%%*/.%%*/    .     *  *#/*/,///(*(        " +
            "\n              (/#& ,(,%#%#&#../(,//((.(#% %#---------------LS Weapon:" +
            "\n                  %#*(#%(/*(/#%((#(&*%*./(%/,/((            " +
            "\n                  %&(#&   @%,,%///-------------------------Head:" +
            "\n                 #(%(&     %&(%&&&(...(     %/(*.           " +
            "\n                (&@/%%    &*&#@@%%#&-----------------------Chest:" +
            "\n               #@#(&&  (#&& ,%(&&&&%%%  &/. *&((@/%(*/      " +
            "\n              ,/(/&   //@*,/@@&#/%/&@@*,&@/*  &,(##--------Arms:" +
            "\n            */&(/&    (%*%(%&@(%*%& @&%%%/%&   &&@,( /      " +
            "\n           **##%       #*(%&&*       &&#*%      /.# /#      " +
            "\n          (.%((%      *&(%&&          &&#&&     ##---------LA Weapon:" +
            "\n         /.&/%,     #&#&&@(            %%#,#(    (*         " +
            "\n          %%-----------------------------------------------RA Weapon:" +
            "\n        ,/%(       #((#&%(%            ##&#%#((             " +
            "\n       ,/&#       /(,/%#%%%            %&#%/---------------Legs:" +
            "\n      ..%         (.*%&%                 %%,*..             " +
            "\n     ,,%        #*,(#&&                    %#* ./           " + "NOMBRE:" +
            "\n    #/*      *&##%&(%%&.                  ,##&%&%#(         " + "ARMADURA: " + GestorBBDD.datoAC(
                "AC_ElNombre", "Armadura") +
            "\n             %&@&&#%%%%                    *&&&&(@@/        " + "CONSUMO ENERGETICO:" + 1 +
            "\n          *#/%%&&&&&%%#                    .%%%%#%#%        " + "PESO:" + 1 +
            "\n         ,#%###                                 &&&%&(      " + "DPS:" + 1 +
            "\n                                                    ,,      " + "RPM:" + 1 +
            "\n      ====================================================     PRECIO:" + 1 + "$"

        )

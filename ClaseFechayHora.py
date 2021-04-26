class FechaHora:
    __dia = '1'
    __mes = '1'
    __año = '2020'
    __hora = '0'
    __minutos = '0'
    __segundos = '0'

    def __init__(self, d=1, me=1, a=2020, h=00, mi=00, s=00):
        self.__dia = int(d)
        self.__mes = int(me)
        self.__año = int(a)
        self.__hora = int(h)
        self.__minutos = int(mi)
        self.__segundos = int(s)

    def Mostrar(self):
        print('{0}/{1}/{2} - {3}:{4}:{5}'.format(self.__dia, self.__mes,
                                                 self.__año, self.__hora, self.__minutos, self.__segundos))

    def PonerEnHora(self, h=00, m=00, s=00):
        self.__hora = h
        self.__minutos = m
        self.__segundos = s

    def AdelantarHora(self, h=00, m=00, s=00):
        self.__hora += h
        self.__minutos += m
        self.__segundos += s
        bisiesto = False
        if self.__segundos >= 60:
            self.__segundos -= 60
            self.__minutos += 1
        if self.__minutos >= 60:
            self.__minutos -= 60
            self.__hora += 1
        if self.__hora >= 24:
            self.__hora -= 24
            self.__dia += 1
        # Comprueba que el año es bisiesto
        if (self.__año % 4 == 0 and self.__año % 100 != 0 or self.__año % 400 == 0):
            bisiesto = True
        # Comprueba si los meses no se pasaron de dias
        # Febrero
        if self.__mes == 2:
            # Febrero bisisesto
            if bisiesto == True:
                if self.__dia >= 29:
                    self.__dia -= 29
                    self.__mes += 1
            # Frebrero normal
            else:
                if self.__dia >= 28:
                    self.__dia -= 28
                    self.__mes += 1
        # Abril, Junio, Septiembre y Noviembre
        if (self.__mes == 4 or self.__mes == 6 or self.__mes == 9 or self.__mes == 11) and self.__dia >= 30:
            self.__dia -= 30
            self.__mes += 1
        # Enero, Marzo, Mayo, Julio, Agosto, Octubre
        if (
                self.__mes == 1 or self.__mes == 3 or self.__mes == 5 or self.__mes == 7 or self.__mes == 8 or self.__mes == 10) and self.__dia >= 31:
            self.__dia -= 31
            self.__mes += 1
        # Diciembre
        if self.__mes == 12 and self.__dia >= 31:
            self.__dia -= 31
            self.__mes = 1
            self.__año += 1





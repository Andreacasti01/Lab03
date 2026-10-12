import csv

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.responsabile = responsabile
        self.elenco_strumenti = []
        self.prestiti = {}

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        try:
            file = open(file_path, "r")
            lettore = csv.reader(file)
            for riga in lettore:
                strumento = [riga[0], riga[1], riga[2], riga[3], riga[4]]
                self.elenco_strumenti.append(strumento)
            #print(self.elenco_strumenti)
            file.close()
        except FileNotFoundError:
            pass


    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        lista_num = []
        for i in self.elenco_strumenti:
            cod = i[0]
            num = int(cod[1:])
            lista_num.append(num)
        num_max=max(lista_num)
        new_cod = "S"+ str(num_max + 1)
        nuovo_strumento = [new_cod, tipo, marca, anno_acquisto, valore]
        self.elenco_strumenti.append(nuovo_strumento)
        #print(self.elenco_strumenti)
        return nuovo_strumento[1]


    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        strumenti_ordinati = []
        a=0
        if a == 0:
            for i in self.elenco_strumenti:
                strumenti_ordinati.append(i[1])
                a=a+1
        else:
            for i in self.elenco_strumenti:
                strumenti_ordinati.append(i[1])
                marca = i[2]
                strumenti_ordinati.sort(key=marca)
        return strumenti_ordinati


    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO
        for j in self.elenco_strumenti:
            if id_strumento in j:
                if self.prestiti == {}:
                    num_prestito=1
                    cod_prestito = "P"+ str(num_prestito)
                    self.prestiti[cod_prestito] = [data, id_strumento, cognome_allievo]
                    nuovo_prestito = (f"E' stato effettuato con successo il prestito {cod_prestito} in data {data} "
                                      f"dello strumento con codice {id_strumento} all'allievo {cognome_allievo}")
                else:
                    lista_num_prestiti = []
                    for k,v in self.prestiti.items():
                        cod_prestito = k
                        num_prestito = int(cod_prestito[1:])
                        lista_num_prestiti.append(num_prestito)
                    num_prestito_max = max(lista_num_prestiti)
                    new_cod_prestito = "P" + str(num_prestito_max + 1)
                    self.prestiti[new_cod_prestito] = [data, id_strumento, cognome_allievo]
                    nuovo_prestito = (f"E' stato effettuato con successo il prestito {new_cod_prestito} in data {data}"
                                      f" dello strumento con codice {id_strumento} all'allievo {cognome_allievo}")
                #print(self.prestiti)
                return nuovo_prestito
            else:
                continue
        else:
            raise Exception("L'id dello strumento inserito non è valido")


    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
        if str(id_prestito) in self.prestiti:
            del self.prestiti[id_prestito]
            return id_prestito
        else:
            raise Exception("L'id del prestito non è valido")

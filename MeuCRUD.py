import sqlite3

class MeuCRUD:
    def __init__(self):
        self.conn = conn = sqlite3.connect('discografia.db')
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS Album (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_album TEXT,
            nome_banda TEXT,
            data_album TEXT
        );
        ''')
        self.conn.commit()
    def fecharBD(self):
        self.conn.close()
    def lerBD(self, chave):
        c = self.conn.cursor()
        if chave == '':
            c.execute("SELECT * FROM Album")
            albuns = c.fetchall()
            return albuns
        else:
            c.execute("SELECT * FROM Album WHERE Id=?", (chave,))
            album = c.fetchone()
            return [album]
    def incluirBD(self, dados):
        c = self.conn.cursor()
        c.execute("INSERT INTO Album VALUES (?, ?, ?, ?)", dados)
        self.conn.commit()
        print('inserido com sucesso')
    def alterarBD(self, chave, campos):
        c = self.conn.cursor()
        campos.append(chave)
        c.execute("UPDATE Album SET nome_album = ?, nome_banda = ?, data_album = ? WHERE Id = ?", campos)
        print('alterado com sucesso')
    def deletarBD(self, chave):
        c = self.conn.cursor()
        c.execute("DELETE FROM Album WHERE Id=?", (chave,))
        print('excluído com sucesso')



crud = MeuCRUD()
while True:
    print('''
    Escolha uma opção:
    1 - incluir
    2 - ler
    3 - alterar
    4 - deletar
    5 - sair
    ''')
    valor = input('->')
    if valor == '1':
        nome_banda = input('Entre com o nome do album: ')
        nome_album = input('Entre com o nome da banda: ')
        data = input('Entre com a data: ')
        dados = [None, nome_banda, nome_album, data]
        crud.incluirBD(dados)
    elif valor == '2':
        chave = input('Qual o valor da chave ou pressione ENTER para visualizar: ')
        resultado = crud.lerBD(chave)
        for i in resultado:
            print(i) # campos
    elif valor == '3':
        chave = input('Qual chave quer alterar: ')
        nome_banda = input('Entre com o nome do album: ')
        nome_album = input('Entre com o nome da banda: ')
        data = input('Entre com a data: ')
        dados = [nome_banda, nome_album, data]
        crud.alterarBD(chave, dados)
    elif valor == '4':
        chave = input('Entre com a chave para deletar: ')
        crud.deletarBD(chave)
    elif valor == '5':
        break
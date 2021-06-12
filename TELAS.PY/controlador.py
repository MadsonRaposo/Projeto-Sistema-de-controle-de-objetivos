from os import curdir, system
from re import X
from PyQt5 import uic,QtWidgets,QtGui
import mysql.connector 


conexão=mysql.connector.connect(
    host='Localhost',
    user='root',
    password='',
    database='projeto_sco' 
)
id_global=str(0)
#
#
#
#
#
#
#
#
#
#
#                                  METODOS PARA CHAMAR AS TELAS COM BOTOES. 
#*************************************************************************************
#------------------------------------------------------------------------------------------------------------------
def chama_meus_objetivos(id ):
    Perfil.close()
    MEUS_OBJETIVOS.show()
    
    
    
    #BOTOS NA TELA MEUS OBJETIVOS
    MEUS_OBJETIVOS.B_NovoObjetivo.clicked.connect(chama_cad_objetivo)
    MEUS_OBJETIVOS.B_Conf_Conta.clicked.connect(chama_dados_conta)
    MEUS_OBJETIVOS.B_Sair.clicked.connect(chama_login)
#-----------------------------------------------------------------------------------------------------------------
def chama_cad_objetivo():
    Perfil.close()
    CADASTRAR_OBEJTIVOS.show()

    #BOTOES NA TELA CADASTRAR OBJETIVOS
    CADASTRAR_OBEJTIVOS.B_MeusObjetivos.clicked.connect(chama_meus_objetivos)
    CADASTRAR_OBEJTIVOS.B_Conf_Conta.clicked.connect(chama_dados_conta)
    CADASTRAR_OBEJTIVOS.B_Sair.clicked.connect(chama_login)

    #CADASTRAR_OBEJTIVOS.B_cadastrar.clicked.connect(chama_login)
#-----------------------------------------------------------------------------------------------------------
def chama_dados_conta():
    Perfil.close()
    EDITAR_USER.close()
    DADOS_CONTA.show()
    global nome_aluno_str
    global e_mail_aluno_str
    global senha_usuario_str
    print(id_global)
    comandoSQL="SELECT id FROM aluno WHERE id='"+id_global+"';"
    cursor=conexão.cursor()
    cursor.execute(comandoSQL)
    id_usuario=cursor.fetchall()
    id_user_str=str(id_usuario[0][0])
    print(id_user_str)

    comandoEMAIL="SELECT e_mail FROM aluno WHERE id='"+id_global+"';"
    cursor=conexão.cursor()
    cursor.execute(comandoEMAIL)
    e_mail_aluno=cursor.fetchall()
    e_mail_aluno_str=str(e_mail_aluno[0][0])
    print(e_mail_aluno_str)

    comandoNOME="SELECT nome FROM aluno WHERE id='"+id_global+"';"
    cursor=conexão.cursor()
    cursor.execute(comandoNOME)
    nome_aluno=cursor.fetchall()
    nome_aluno_str=str(nome_aluno[0][0])
    print(nome_aluno_str)

    comandoSENHA="SELECT senha FROM aluno WHERE id='"+id_global+"';"
    cursor=conexão.cursor()
    cursor.execute(comandoSENHA)
    senha_usuario=cursor.fetchall()
    senha_usuario_str=str(senha_usuario[0][0])
    print(senha_usuario_str)

    DADOS_CONTA.NomeUsuario.setText(nome_aluno_str)
    DADOS_CONTA.C_email.setText(e_mail_aluno_str)
    DADOS_CONTA.C_nome.setText(nome_aluno_str)
    DADOS_CONTA.C_senha.setText(senha_usuario_str)




    #BOTOES NA TELA DE DADOS DO USUARIO
    DADOS_CONTA.B_MeusObjetivos.clicked.connect(chama_meus_objetivos)
    DADOS_CONTA.B_NovoObjetivo.clicked.connect(chama_cad_objetivo)
    DADOS_CONTA.B_Sair.clicked.connect(chama_login)

    DADOS_CONTA.B_editar.clicked.connect(chama_editar_usuario)    
#--------------------------------------------------------------------------------------------------------------
def chama_login():
    Perfil.close()
    CADASTRAR.close()
    LOGIN.show()
    LOGIN.C_usuario.setText("")
    LOGIN.C_senha.setText("")
#---------------------------------------------------------------------------------------------------------------
def chama_perfil(nome_usuario):
    LOGIN.close()
    Perfil.show()
    global id_global
    comandoSQL="SELECT id FROM aluno WHERE nome='"+nome_usuario+"';"
    cursor=conexão.cursor()
    cursor.execute(comandoSQL)
    id_usuario=cursor.fetchall()
    print(id_usuario)
    id_global=str(id_usuario[0][0])
    print(id_global)


        

    Perfil.NomeUsuario_Meio.setText(nome_usuario)
    Perfil.NomeUsuario.setText(nome_usuario)

    #BOTOS NA TELA DO PERFIL
    Perfil.B_MeusObjetivos.clicked.connect(chama_meus_objetivos)
    Perfil.B_NovoObjetivo.clicked.connect(chama_cad_objetivo)
    Perfil.B_Conf_Conta.clicked.connect(chama_dados_conta)
    Perfil.B_Sair.clicked.connect(chama_login)
#--------------------------------------------------------------------
def chama_cadastro():
    LOGIN.close()
    CADASTRAR.show()
    #BOTOES NA TELA DE CADASTRO.
    CADASTRAR.B_Cadastrar.clicked.connect(cadastrando_usuario)
#-----------------------------------------------------------

#
#
#
#
#
#
#
#
#
#
#
#
#                                         METODOS CRUD USUARIO
#*****************************************************************************************************

def cadastrando_usuario ():
    nome = CADASTRAR.C_usuario.text()
    e_mail = CADASTRAR.C_email.text()
    senha = CADASTRAR.C_senha.text()
    c_senha = CADASTRAR.C_ConfirmarSenha.text()
    sero=0
    try:

        verificar_nome="SELECT nome FROM aluno WHERE nome='"+nome+"'"
        cursor=conexão.cursor()
        cursor.execute(verificar_nome)
        verificado=cursor.fetchall()
        str_ver=str(verificado[0][0])
    except:
        str_ver=str(sero)

    if str_ver==nome:
        CADASTRAR.aviso.setText("Nome inserido já existe")        
    else:
        if (c_senha == senha):
            comandoSQL = " INSERT INTO aluno(nome, senha, e_mail)VALUES (%s,%s,%s )"
            valores=(nome,senha,e_mail)
            try:
                cursor=conexão.cursor()
                cursor.execute(comandoSQL,valores) 
                conexão.commit()
                cursor.close()
                CADASTRAR.close()
                LOGIN.show()
                LOGIN.C_aviso.setText("Cadastrado")

            except:
                CADASTRAR.aviso.setText("erro na adição dos dados")
        else:
            CADASTRAR.aviso.setText("Senhas diferentes")

def autenticando_login ():
    usuario=LOGIN.C_usuario.text()
    senha=LOGIN.C_senha.text()
    comandoSQL="  SELECT senha FROM  aluno WHERE  nome= '"+ usuario +"'; "

    try:
        cursor=conexão.cursor()
        cursor.execute(comandoSQL)
        senha_bd=cursor.fetchall()

        if senha_bd[0][0]==senha:
            chama_perfil(usuario)

                    
        else: 
            LOGIN.C_aviso.setText("Dados de login incorretos!!!!")

    except:  
        LOGIN.C_aviso.setText("Dados de login invalidos!!")

def chama_editar_usuario():
    DADOS_CONTA.close()
    EDITAR_USER.show()

    global edit_nome, edit_e_mail, edit_senha, edit_c_senha


    EDITAR_USER.C_usuario.setText(nome_aluno_str)
    EDITAR_USER.C_email.setText(e_mail_aluno_str)
    EDITAR_USER.C_senha.setText(senha_usuario_str)
    EDITAR_USER.C_ConfirmarSenha.setText(senha_usuario_str)


    EDITAR_USER.Editar_nome.clicked.connect(editar_nome_user)
    EDITAR_USER.Editar_email.clicked.connect(editar_email_user)
    EDITAR_USER.Editar_senha.clicked.connect(editar_senha_user)
    EDITAR_USER.Excluir_usuario.clicked.connect(excluir_user)
    EDITAR_USER.voltar.clicked.connect(chama_dados_conta)

def editar_nome_user():

    edit_nome = EDITAR_USER.C_usuario.text()

    print(edit_nome)

    comandoSQL = " UPDATE aluno SET nome = %s WHERE id = %s"
    valores=(edit_nome,id_global)
    try: 
        cursor=conexão.cursor()  
        cursor.execute(comandoSQL,valores)
        conexão.commit()
        cursor.close()
        EDITAR_USER.aviso.setText("Atualizado")
    except:
        EDITAR_USER.aviso.setText("erro ao atualizar dados")

def editar_email_user():

    edit_e_mail = EDITAR_USER.C_email.text()

    print(edit_e_mail)

    comandoSQL = " UPDATE aluno SET e_mail = %s WHERE id = %s"
    valores=(edit_e_mail,id_global)
    try: 
        cursor=conexão.cursor()  
        cursor.execute(comandoSQL,valores)
        conexão.commit()
        cursor.close()
        EDITAR_USER.aviso.setText("Atualizado")
    except:
        EDITAR_USER.aviso.setText("erro ao atualizar dados")

def editar_senha_user():
    edit_senha = EDITAR_USER.C_senha.text()
    edit_c_senha = EDITAR_USER.C_ConfirmarSenha.text()
    
    if edit_c_senha==edit_senha:

        comandoSQL = " UPDATE aluno SET senha = %s WHERE id = %s"
        valores=(edit_senha,id_global)
        try: 
            cursor=conexão.cursor()  
            cursor.execute(comandoSQL,valores)
            conexão.commit()
            cursor.close()
            EDITAR_USER.aviso.setText("Atualizado")
        except:
            EDITAR_USER.aviso.setText("erro ao atualizar dados")
    else:
        EDITAR_USER.aviso.setText("Senhas são diferentes")

def excluir_user():

    comandoSQL = " DELETE FROM aluno WHERE id = '"+id_global+"'"
    try:
        cursor=conexão.cursor()  
        cursor.execute(comandoSQL)
        conexão.commit()
        cursor.close()
        EDITAR_USER.close()
        LOGIN.show()
        LOGIN.C_aviso.setText("Usuario excluido")
    except:
        EDITAR_USER.aviso.setText("erro ao excluir usuario")






#                                         METODOS CRUD MATERIA
#***************************************************************************************************** 
# 
 
#                                         METODOS CRUD RESULTADO_CHAVE
#*****************************************************************************************************


#                                         METODOS CRUD ASSUNTO
#*****************************************************************************************************


#                                         METODOS CRUD OBJETIVO
#*****************************************************************************************************

#
#
#
#
#
#
#
#
#
#
#

#                                      IMPORTANDO TELAS. 
#*****************************************************************************************************

app=QtWidgets.QApplication([])
LOGIN = uic.loadUi ("D:\GITHUB\projetoSCO\TELAS.PY\LOGIN.ui")
Perfil = uic.loadUi ("D:\GITHUB\projetoSCO\TELAS.PY\Perfil.ui")
CADASTRAR = uic.loadUi ("D:\GITHUB\projetoSCO\TELAS.PY\CADASTRAR.ui")
CADASTRAR_OBEJTIVOS = uic.loadUi ("D:\GITHUB\projetoSCO\TELAS.PY\CADASTRAR_OBJETIVOS.ui")
MEUS_OBJETIVOS = uic.loadUi ("D:\GITHUB\projetoSCO\TELAS.PY\MEUS_OBJETIVOS.ui")
DADOS_CONTA = uic.loadUi ("D:\GITHUB\projetoSCO\TELAS.PY\DADOS_CONTA.ui")
EDITAR_USER = uic.loadUi ("D:\GITHUB\projetoSCO\TELAS.PY\EDITAR_USER.ui")

#BOTOES NA TELA DE LOGIN
LOGIN.B_Entrar.clicked.connect(autenticando_login)
LOGIN.B_Cadastrar.clicked.connect(chama_cadastro)


LOGIN.show()
app.exec()
#*******************************************************************************************************
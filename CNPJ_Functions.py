#--- Localizar o primeiro CNPJ em um texto ---

import re

def localizar_cnpj(texto):
  """
  Função que localiza o primeiro CNPJ contido em um texto.

  Parâmetros:
    texto (str): O texto onde o CNPJ será buscado.

  Retorno:
    str: O CNPJ encontrado, ou None se nenhum for encontrado.
  """

  # Expressão regular para CNPJ
  regex_cnpj = r"\d{2}.\d{3}.\d{3}/\d{4}-\d{2}"

  # Procurando o primeiro CNPJ no texto
  match = re.search(regex_cnpj, texto)

  # Retornando o CNPJ encontrado, ou None se nenhum for encontrado
  if match:
    return match.group()
  else:
    return None

# Exemplo de uso
texto = "Este texto contém um CNPJ: 00.000.000/0000-00."
cnpj = localizar_cnpj(texto)

if cnpj:
  print(f"CNPJ encontrado: {cnpj}")
else:
  print("Nenhum CNPJ encontrado.")
  

#--- Localizar varios CNPJS em um texto ----

import re

def localizar_todos_cnpjs(texto):
  """
  Função que localiza todos os CNPJs contidos em um texto.

  Parâmetros:
    texto (str): O texto onde os CNPJs serão buscados.

  Retorno:
    list: Uma lista com todos os CNPJs encontrados.
  """

  # Expressão regular para CNPJ
  regex_cnpj = r"\d{2}.\d{3}.\d{3}/\d{4}-\d{2}"

  # Procurando todos os CNPJs no texto
  matches = re.findall(regex_cnpj, texto)

  # Retornando uma lista com os CNPJs encontrados
  return matches

# Exemplo de uso
texto = "Este texto contém dois CNPJs: 00.000.000/0000-00 e 11.111.111/1111-11."

cnpjs = localizar_todos_cnpjs(texto)

for cnpj in cnpjs:
  print(f"CNPJ encontrado: {cnpj}")


# ----
  

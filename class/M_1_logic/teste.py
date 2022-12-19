import random
import pandas as pd
# ter uma lista para cada um dos dados
# randomizar a criação dos dados
# randomizar a criação dos relacionamentos
# gerar os dados em JSON dict -> salvar num arquivo txt ou csv

aluno_lista = ["Ana", "Maria", "Marta"]
p_nome = ['Paulo', 'Maria', 'Pedro']
p_idade = [34, 48, 52]
materia = ['História', 'Português', 'Matemática']
sexo = ["F", "M", "Outro"]
m_carga = [60, 50, 100]
m_dia = ['Segunda', 'Quarta', 'Sexta']

aluno = {
  "nome": random.choice(aluno_lista),
  "matricula": random.choice(range(1111, 9999)),
  "sexo": random.choice(sexo),
}
professor = {
  "nome": random.choice(p_nome),
  "idade": random.choice(p_idade),
  "sexo": random.choice(sexo),
}
materia = {
  "nome": random.choice(materia),
  "carga": random.choice(m_carga),
  "dia": random.choice(m_dia),
}

entidades = {"aluno": aluno, "professor": professor, "matéria": materia}
print(entidades)
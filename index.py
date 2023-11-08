print("Digite seu nome")
nome = input()

execute = True

while(execute == True):
  print("Digite seu ano de nascimento")
  try:
    ano = int(input())
    if (ano < 1992) or (ano > 2021):
      print("O ano deve ser entre 1992 a 2021")
    else:
      idade = 2022 - ano
      execute = False
      print("Nome: ", nome, "tem ou terá", idade, " anos em 2022")
  except:
    print("Informe apenas números")

exit()


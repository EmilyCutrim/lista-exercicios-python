texto_1= float(input("Preço do carro em 2022: "))
texto_2 = float(input("Preço do carro em 2023: "))
texto_3 = float(input("Preço do carro em 2024: "))

if texto_1 >= texto_2 and texto_2 >= texto_3:
  print (f'o carro de 2022, no valor de R$ {texto_1} é o maior valor médio entres os três anos, sendo o de 2024, no valor de R$ {texto_3} o mais barato')
elif texto_2 >= texto_3 and texto_2 >= texto_1:
  print (f'o carro de 2023, no valor de R$ {texto_2} é o maior valor médio entres os três anos, sendo o de 2022, no valor de R$ {texto_1} o mais barato')
elif texto_3 >= texto_1 and texto_1 >= texto_2:   
  print (f'o carro de 2024, no valor de R$ {texto_3} é o maior valor médio entres os três anos, sendo o de 2023, no valor de R$ {texto_2} o mais barato')
elif texto_2 >= texto_1 and texto_3 >= texto_2:   
  print (f'o carro de 2024, no valor de R$ {texto_3} é o maior valor médio entres os três anos, sendo o de 2023, no valor de R$ {texto_2} o mais barato')
  
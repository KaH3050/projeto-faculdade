print("Olá! Tudo bem? Sou o Cordenador Filipe de Moraes Lodi")
nome= input("Qual é seu nome?")
print("Olá", nome, "É um prazer conhecê-lo")
print(nome, "Qual a matéria que o senhor gostaria de saber a sua média?")
matéria= input("")
print(matéria, "," "Vish..... Essa matéria é bem difícil, acho que você não atingiu a média")
nota01= float(input("Qual foi sua nota da primeira prova?"))
nota02= float(input("Qual foi a sua nota da segunda prova?"))
nota03= float(input("Qual foi a sua nota da terceira prova?"))
print("Aguarda só um momentinho que eu vou calcular e falar a nota para você")
média= (nota01+nota02+nota03) / 3
if média >= 7: 
     print("Sua média em", matéria, "foi:", média, "- Aprovado!")
else: 
         print("Sua média em", matéria, "foi:", média, "- Reprovado! Você precisa estudar mais.")

#converter entre celsius e fahrenheit
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Solicita ao usuário a temperatura e a escala de origem
temperatura = float(input("Digite a temperatura: "))
escala = input("Informe a escala de origem (C para Celsius ou F para Fahrenheit): ").upper()

# Converte e exibe o resultado

if escala == "C":
    convertido = celsius_para_fahrenheit(temperatura)
    print(f"{temperatura}°C equivalem a {convertido:.2f}°F")
elif escala == "F":
    convertido = fahrenheit_para_celsius(temperatura)
    print(f"{temperatura}°F equivalem a {convertido:.2f}°C")
else:
    print("Escala inválida. Use C para Celsius ou F para Fahrenheit.")


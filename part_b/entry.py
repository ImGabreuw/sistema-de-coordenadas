def entry():
    x = int(input("Digite a coordenada X do ponto de origem A do robô: "))
    y = int(input("Digite a coordenada Y do ponto de origem A do robô: "))
    time = int(input("Digite por quanto tempo o robô irá caminhar: "))

    for i in range(time):
        movement = i % 3

        if movement == 0:
            y += 1
            continue

        x += 1

    print(f"Ao final da caminhada o robô estará no ponto ({x}, {y}) do plano cartesiano.")

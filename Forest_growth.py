import matplotlib.pyplot as plt
import random
import numpy as np

# Parametri simulacije --> mogu se mijenjati, ali veći parametri značajno usporavaju izvođenje koda
broj_godina = 10
velicina_sume = 1000  # Veličina šume (broj kvadrata)

# Inicijalizacija šume s nekim početnim stablima
suma = np.zeros((velicina_sume, velicina_sume), dtype=int)
for _ in range(velicina_sume * velicina_sume // 10):
    x, y = random.randint(0, velicina_sume - 1), random.randint(0, velicina_sume - 1)
    suma[x][y] = 1

# Funkcija za rast stabala svake godine
def rast_stabala(suma):
    nova_suma = suma.copy()
    for i in range(velicina_sume):
        for j in range(velicina_sume):
            if suma[i][j] == 1:  # Stablo postoji
                # Postoji šansa da stablo donese novo dijete
                if random.random() < 0.2:
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            if 0 <= i + dx < velicina_sume and 0 <= j + dy < velicina_sume:
                                susjed = suma[i + dx][j + dy]
                                if susjed == 0:
                                    nova_suma[i + dx][j + dy] = 1  # Novo stablo raste
    return nova_suma

# Vizualizacija rasta šume tijekom godina
plt.figure(figsize=(10, 5))
for godina in range(broj_godina):
    suma = rast_stabala(suma)
    plt.subplot(2, 5, godina + 1)
    plt.imshow(suma, cmap='Greens')
    plt.title(f'Godina {godina + 1}')
    plt.axis('off')

plt.tight_layout()
plt.show()

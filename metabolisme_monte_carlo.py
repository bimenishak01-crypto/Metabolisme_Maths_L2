import numpy as np
import matplotlib.pyplot as plt

def main():
    # Paramètres de simulation
    c = 1 / 7700
    y0 = 75.0
    days = 90
    trajectories = 100
    
    E_in = 2800
    E_out_mean = 2500
    E_out_std = 300
    
    # Initialisation de la matrice pour stocker les poids
    # Shape: (trajectories, days + 1)
    y = np.zeros((trajectories, days + 1))
    y[:, 0] = y0
    
    # Simulation des dépenses énergétiques (E_out)
    # On génère toutes les variables aléatoires d'un coup pour les 100 trajectoires sur 90 jours
    E_out = np.random.normal(loc=E_out_mean, scale=E_out_std, size=(trajectories, days))
    
    # Résolution discrète de l'équation différentielle : y(t+1) = y(t) + c * (E_in - E_out(t))
    for t in range(days):
        y[:, t + 1] = y[:, t] + c * (E_in - E_out[:, t])
        
    # Calcul des statistiques
    mean_trajectory = np.mean(y, axis=0)
    std_trajectory = np.std(y, axis=0)
    
    # L'intervalle de confiance à 95% correspond environ à la moyenne +/- 1.96 * écart-type
    ci_upper = mean_trajectory + 1.96 * std_trajectory
    ci_lower = mean_trajectory - 1.96 * std_trajectory
    
    # Tracé graphique
    time_steps = np.arange(days + 1)
    
    plt.figure(figsize=(10, 6))
    
    # Tracer les 100 trajectoires en gris transparent
    for i in range(trajectories):
        plt.plot(time_steps, y[i], color='gray', alpha=0.1)
        
    # Tracer la moyenne en rouge
    plt.plot(time_steps, mean_trajectory, color='red', linewidth=2, label='Moyenne')
    
    # Tracer l'intervalle de confiance à 95% en pointillés
    plt.plot(time_steps, ci_upper, color='red', linestyle='--', linewidth=1.5, label='Intervalle de confiance (95%)')
    plt.plot(time_steps, ci_lower, color='red', linestyle='--', linewidth=1.5)
    
    plt.title('Simulation de Monte-Carlo : Évolution de la masse corporelle')
    plt.xlabel('Jours')
    plt.ylabel('Poids (kg)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Sauvegarder et afficher le graphique
    plt.savefig('metabolisme_simulation.png', dpi=300, bbox_inches='tight')
    print("Le graphique a été sauvegardé sous 'metabolisme_simulation.png'.")
    plt.show()
    
    # Affichage des résultats dans la console
    final_weights = y[:, -1]
    final_mean = np.mean(final_weights)
    final_std = np.std(final_weights)
    final_ci_lower = final_mean - 1.96 * final_std
    final_ci_upper = final_mean + 1.96 * final_std
    
    print("\n--- Résultats au jour 90 ---")
    print(f"Poids moyen estimé : {final_mean:.2f} kg")
    print(f"Intervalle de confiance (95%) : [{final_ci_lower:.2f} kg, {final_ci_upper:.2f} kg]")

if __name__ == "__main__":
    main()

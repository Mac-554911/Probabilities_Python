import random
import statistics
from typing import List, Tuple

class ProbabilitySimulator:
    def __init__(self):
        self.die_faces = 6
        self.theoretical_prob = 1 / self.die_faces
    
    def simulate_die_rolls(self, num_trials: int) -> dict:
        frequencies = {i: 0 for i in range(1, self.die_faces + 1)}
        
        for _ in range(num_trials):
            roll = random.randint(1, self.die_faces)
            frequencies[roll] += 1
        
        return frequencies
    
    def calculate_probabilities(self, frequencies: dict, num_trials: int) -> List[dict]:
        results = []
        
        for face in range(1, self.die_faces + 1):
            freq = frequencies[face]
            empirical_prob = freq / num_trials
            absolute_error = abs(empirical_prob - self.theoretical_prob)
            percentage_error = (absolute_error / self.theoretical_prob) * 100
            
            results.append({
                'face': face,
                'frequency': freq,
                'empirical_prob': empirical_prob,
                'theoretical_prob': self.theoretical_prob,
                'absolute_error': absolute_error,
                'percentage_error': percentage_error
            })
        
        return results
    
    def display_results(self, results: List[dict], num_trials: int):
        print(f"\n{'='*90}")
        print(f"PART A: DIE ROLL SIMULATION RESULTS (Trials: {num_trials})")
        print(f"{'='*90}")
        print(f"{'Face':<6} {'Frequency':<12} {'Empirical P':<15} {'Theoretical P':<15} {'Abs Error':<12} {'% Error':<10}")
        print(f"{'-'*90}")
        
        for result in results:
            print(f"{result['face']:<6} "
                  f"{result['frequency']:<12} "
                  f"{result['empirical_prob']:<15.6f} "
                  f"{result['theoretical_prob']:<15.6f} "
                  f"{result['absolute_error']:<12.6f} "
                  f"{result['percentage_error']:<10.2f}%")
        
        print(f"{'='*90}\n")
    
    def run(self):
        """Main execution method for Part A."""
        print("\n" + "="*50)
        print("PART A: PROBABILITY SIMULATOR - DIE ROLLING")
        print("="*50)
        
        while True:
            try:
                num_trials = int(input("\nEnter the number of trials (1-10000): "))
                if 1 <= num_trials <= 10000:
                    break
                else:
                    print("Please enter a number between 1 and 10,000.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        
        print(f"\nSimulating {num_trials} die rolls...")
        frequencies = self.simulate_die_rolls(num_trials)
        results = self.calculate_probabilities(frequencies, num_trials)
        self.display_results(results, num_trials)

class ExpectationCalculator:
    def __init__(self):
        self.values = []
        self.probabilities = []
    
    def get_user_input(self):
        print("\n" + "="*50)
        print("PART B: EXPECTATION & VARIANCE CALCULATOR")
        print("="*50)
        
        while True:
            try:
                n = int(input("\nEnter the number of discrete values: "))
                if n > 0:
                    break
                else:
                    print("Please enter a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        
        print(f"\nEnter {n} values and their probabilities:")
        
        for i in range(n):
            while True:
                try:
                    value = float(input(f"  Value X[{i+1}]: "))
                    prob = float(input(f"  P(X={value}): "))
                    
                    if 0 <= prob <= 1:
                        self.values.append(value)
                        self.probabilities.append(prob)
                        break
                    else:
                        print("  Probability must be between 0 and 1.")
                except ValueError:
                    print("  Invalid input. Please enter numeric values.")
    
    def validate_distribution(self) -> bool:
        total = sum(self.probabilities)
        return abs(total - 1.0) < 0.0001
    
    def calculate_expectation(self) -> float:

        expectation = sum(x * p for x, p in zip(self.values, self.probabilities))
        return expectation
    
    def calculate_variance(self, expectation: float) -> float:
        e_x_squared = sum(x**2 * p for x, p in zip(self.values, self.probabilities))
        variance = e_x_squared - expectation**2
        return variance
    
    def display_calculations(self, expectation: float, variance: float, std_dev: float):
        print(f"\n{'='*70}")
        print("PROBABILITY DISTRIBUTION TABLE")
        print(f"{'='*70}")
        print(f"{'X':<15} {'P(X)':<15} {'X * P(X)':<20} {'X² * P(X)':<20}")
        print(f"{'-'*70}")
        
        for x, p in zip(self.values, self.probabilities):
            x_p = x * p
            x2_p = x**2 * p
            print(f"{x:<15.4f} {p:<15.6f} {x_p:<20.6f} {x2_p:<20.6f}")
        
        print(f"{'-'*70}")
        print(f"{'Sum:':<15} {sum(self.probabilities):<15.6f} "
              f"{sum(x*p for x,p in zip(self.values, self.probabilities)):<20.6f} "
              f"{sum(x**2*p for x,p in zip(self.values, self.probabilities)):<20.6f}")
        print(f"{'='*70}\n")
        
        print("RESULTS:")
        print(f"  E(X) = Σ[X * P(X)] = {expectation:.6f}")
        print(f"  E(X²) = Σ[X² * P(X)] = {sum(x**2*p for x,p in zip(self.values, self.probabilities)):.6f}")
        print(f"  Var(X) = E(X²) - [E(X)]² = {variance:.6f}")
        print(f"  SD(X) = √Var(X) = {std_dev:.6f}")
        print(f"{'='*70}\n")
    
    def run(self):
        self.get_user_input()
        
        if not self.validate_distribution():
            print("\n⚠ WARNING: Probabilities do not sum to 1.0")
            print(f"  Sum of probabilities: {sum(self.probabilities):.6f}")
            
            response = input("  Continue anyway? (y/n): ")
            if response.lower() != 'y':
                print("  Calculation cancelled.")
                return
        
        expectation = self.calculate_expectation()
        variance = self.calculate_variance(expectation)
        std_dev = variance ** 0.5
        
        self.display_calculations(expectation, variance, std_dev)

def main():
    print("\n" + "="*70)
    print("  DISCRETE STRUCTURES 2 - PROBABILITY & EXPECTATION SIMULATOR")
    print("="*70)
    
    while True:
        print("\nMAIN MENU:")
        print("  [1] Part A: Probability Simulator (Die Rolling)")
        print("  [2] Part B: Expectation & Variance Calculator")
        print("  [3] Run Both Parts")
        print("  [4] Exit")
        
        choice = input("\nSelect an option (1-4): ")
        
        if choice == '1':
            simulator = ProbabilitySimulator()
            simulator.run()
        
        elif choice == '2':
            calculator = ExpectationCalculator()
            calculator.run()
        
        elif choice == '3':
            simulator = ProbabilitySimulator()
            simulator.run()
            calculator = ExpectationCalculator()
            calculator.run()
        
        elif choice == '4':
            print("\nThank you for using the Probability & Expectation Simulator!")
            print("Exiting program...\n")
            break
        
        else:
            print("\nInvalid choice. Please select 1-4.")

if __name__ == "_main_":

    main()

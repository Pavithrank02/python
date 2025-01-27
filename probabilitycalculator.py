import random

class Hat:
    def __init__(self, **ball_colors):
        # Create a list of balls based on the input arguments
        self.contents = []
        for color, count in ball_colors.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls):
        # Draw a number of balls from the hat (without replacement)
        drawn_balls = random.sample(self.contents, k=min(num_balls, len(self.contents)))
        # Remove the drawn balls from the contents
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0
    
    # Perform the number of experiments
    for _ in range(num_experiments):
        # Create a copy of the hat for each experiment to avoid modifying the original
        hat_copy = Hat(**{color: hat.contents.count(color) for color in hat.contents})
        
        # Draw balls from the hat
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        # Check if the drawn balls match the expected number of balls
        drawn_ball_count = {color: drawn_balls.count(color) for color in drawn_balls}
        if all(drawn_ball_count.get(color, 0) >= count for color, count in expected_balls.items()):
            successful_experiments += 1
    
    # Calculate the probability as the ratio of successful experiments to total experiments
    return successful_experiments / num_experiments


# Example Usage
hat = Hat(red=5, blue=4, green=2)
expected_balls = {'red': 1, 'green': 2}
num_balls_drawn = 4
num_experiments = 2000

probability = experiment(hat, expected_balls, num_balls_drawn, num_experiments)
print(f"The probability of drawing {expected_balls} is approximately {probability:.4f}")

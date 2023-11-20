import pygame
import sys

# Initialize Pygame
pygame.init()

# Colors and dimensions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 500, 600

# Initialize Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Seven Segment Binary Display")

# Seven segment configuration
segments = [
    pygame.Rect(150, 100, 200, 20),  # Segment a
    pygame.Rect(350, 120, 20, 200),  # Segment b
    pygame.Rect(350, 350, 20, 200),  # Segment c
    pygame.Rect(150, 550, 200, 20),  # Segment d
    pygame.Rect(130, 350, 20, 200),  # Segment e
    pygame.Rect(130, 120, 20, 200),  # Segment f
    pygame.Rect(150, 320, 200, 20)   # Segment g
]

# Digits to display in seven segment
seven_segment_digits = {
    0: [1, 1, 1, 1, 1, 1, 0],
    1: [0, 1, 1, 0, 0, 0, 0],
    2: [1, 1, 0, 1, 1, 0, 1],
    3: [1, 1, 1, 1, 0, 0, 1],
    4: [0, 1, 1, 0, 0, 1, 1],
    5: [1, 0, 1, 1, 0, 1, 1],
    6: [1, 0, 1, 1, 1, 1, 1],
    7: [1, 1, 1, 0, 0, 0, 0],
    8: [1, 1, 1, 1, 1, 1, 1],
    9: [1, 1, 1, 1, 0, 1, 1]
}

# Define button properties
button_width, button_height = 50, 30
button_margin = 20
button_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

# Initialize button states and colors
button_states = [0, 0, 0, 0]
button_current_colors = button_colors.copy()

# Define button rectangles
buttons = [
    pygame.Rect(WIDTH - 120, 50, button_width, button_height),
    pygame.Rect(WIDTH - 120, 100, button_width, button_height),
    pygame.Rect(WIDTH - 120, 150, button_width, button_height),
    pygame.Rect(WIDTH - 120, 200, button_width, button_height),
]

def draw_buttons():
    for i in range(4):
        pygame.draw.rect(screen, button_current_colors[i], buttons[i])

# Function to check button clicks
def check_button_click(pos):
    for i, button in enumerate(buttons):
        if button.collidepoint(pos):
            button_states[i] = 1 - button_states[i]  # Toggle button state
            if button_states[i]:
                button_current_colors[i] = (255, 255, 255)  # Change color when pressed
            else:
                button_current_colors[i] = button_colors[i]  # Reset color when released

def draw_seven_segment(number):
    # Clear the screen
    screen.fill(BLACK)

    # Draw segments based on the binary representation of the number
    binary_representation = seven_segment_digits[number]
    for i, segment in enumerate(segments):
        if binary_representation[i]:
            pygame.draw.rect(screen, WHITE, segment)

# Main loop
running = True
number_to_display = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_button_click(event.pos)

    draw_seven_segment(number_to_display)
    draw_buttons()

    # Display corresponding digit based on button states
    binary_input = ''.join(map(str, button_states[::-1]))
    number_to_display = int(binary_input, 2)

    pygame.display.flip()

# Exit the application
pygame.quit()
sys.exit()

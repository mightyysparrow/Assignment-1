import pygame
import time
import os

# Initialize pygame mixer
pygame.mixer.init()

# Load sound effect
current_dir = os.path.dirname(os.path.abspath(__file__))
sound_file = os.path.join(current_dir, "swap_sound.mp3")
swap_sound = pygame.mixer.Sound(sound_file)

def merge_sort(arr):
    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                play_sound_effect()  # Play sound for a swap
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort_recursive(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = merge_sort_recursive(arr[:mid])
        right = merge_sort_recursive(arr[mid:])
        
        merged = merge(left, right)
        print(f"Merging: {left} and {right}")
        print(f"Result: {merged}")
        print_array(merged)
        return merged

    return merge_sort_recursive(arr)

def print_array(arr):
    print(" ".join(map(str, arr)))
    print("-" * 40)
    time.sleep(1)  # Pause to make the visualization easier to follow

def play_sound_effect():
    swap_sound.play()
    time.sleep(0.1)  # Short delay to allow sound to play

# Main program
if __name__ == "__main__":
    # Product IDs
    arr = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
    
    print("Original array:")
    print_array(arr)
    
    print("Sorting process:")
    sorted_arr = merge_sort(arr)
    
    print("Final sorted array:")
    print_array(sorted_arr)

    # Quit pygame mixer
    pygame.mixer.quit()

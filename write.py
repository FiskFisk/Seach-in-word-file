import keyboard

def write_dots():
    with open("..txt", "a") as f:
        while True:
            if keyboard.is_pressed("ctrl"):
                f.write(".")
                f.flush()  # Ensure the dots are written immediately
            else:
                break

def main():
    print("Press and hold Ctrl to write dots to '..txt'. Release Ctrl to stop.")
    while True:
        keyboard.wait("ctrl")
        write_dots()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram exited.")

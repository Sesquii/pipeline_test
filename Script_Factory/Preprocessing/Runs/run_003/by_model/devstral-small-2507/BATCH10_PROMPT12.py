import random
import time
import sys

class GlitchyMediaPlayer:
    def __init__(self, video_file):
        self.video_file = video_file
        self.glitch_probability = 0.2  # 20% chance of a glitch occurring

    def play(self):
        print(f"Playing {self.video_file}...")

        with open(self.video_file, 'r') as file:
            for line in file:
                if random.random() < self.glitch_probability:
                    self.apply_glitch(line.strip())
                else:
                    print(line.strip())
                time.sleep(0.1)  # Simulate playback delay

    def apply_glitch(self, frame):
        glitch_type = random.choice(['freeze', 'repeat', 'distort'])

        if glitch_type == 'freeze':
            self.apply_freeze(frame)
        elif glitch_type == 'repeat':
            self.apply_repeat(frame)
        elif glitch_type == 'distort':
            self.apply_distortion(frame)

    def apply_freeze(self, frame):
        print(f"GLITCH: Freezing frame for 0.5 seconds")
        print(frame)
        time.sleep(0.5)

    def apply_repeat(self, frame):
        repeat_count = random.randint(2, 5)
        print(f"GLITCH: Repeating frame {repeat_count} times")
        for _ in range(repeat_count):
            print(frame)
        time.sleep(0.1 * repeat_count)

    def apply_distortion(self, frame):
        distorted_frame = ''.join(
            random.choice([c.lower(), c.upper()]) if c.isalpha()
            else c for c in frame
        )
        print(f"GLITCH: Distorting frame - {distorted_frame}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python BATCH10_PROMPT12_{model_name}.py <video_file>")
        sys.exit(1)

    video_file = sys.argv[1]
    player = GlitchyMediaPlayer(video_file)
    player.play()

if __name__ == "__main__":
    main()
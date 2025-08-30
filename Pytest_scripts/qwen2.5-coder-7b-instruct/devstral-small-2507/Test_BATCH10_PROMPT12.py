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

# ===== GENERATED TESTS =====
```python
import pytest
from unittest.mock import patch, MagicMock

# Original script remains unchanged

def test_play_no_glitches(mocker):
    """Test play method with no glitches"""
    video_file = 'test_video.txt'
    mocker.patch('random.random', return_value=0.1)  # Always less than glitch probability
    player = GlitchyMediaPlayer(video_file)
    with patch('builtins.print') as mock_print:
        player.play()
        assert mock_print.call_count == 3  # Assuming 3 lines in the video file

def test_play_with_glitches(mocker):
    """Test play method with glitches"""
    video_file = 'test_video.txt'
    mocker.patch('random.random', side_effect=[0.1, 0.2, 0.3])  # Glitch on first line
    player = GlitchyMediaPlayer(video_file)
    with patch('builtins.print') as mock_print:
        player.play()
        assert mock_print.call_count == 4  # Assuming 3 lines in the video file plus one glitch

def test_apply_glitch(mocker):
    """Test apply_glitch method"""
    frame = 'test_frame'
    mocker.patch('random.choice', side_effect=['freeze', 'repeat', 'distort'])
    player = GlitchyMediaPlayer('test_video.txt')
    
    with patch('builtins.print') as mock_print:
        player.apply_glitch(frame)
        assert mock_print.call_count == 1

def test_apply_freeze(mocker):
    """Test apply_freeze method"""
    frame = 'test_frame'
    mocker.patch('time.sleep', return_value=None)
    player = GlitchyMediaPlayer('test_video.txt')
    
    with patch('builtins.print') as mock_print:
        player.apply_freeze(frame)
        assert mock_print.call_count == 1

def test_apply_repeat(mocker):
    """Test apply_repeat method"""
    frame = 'test_frame'
    mocker.patch('time.sleep', return_value=None)
    player = GlitchyMediaPlayer('test_video.txt')
    
    with patch('builtins.print') as mock_print:
        player.apply_repeat(frame)
        assert mock_print.call_count >= 2

def test_apply_distortion(mocker):
    """Test apply_distortion method"""
    frame = 'test_frame'
    mocker.patch('random.choice', side_effect=['lower', 'upper', 'lower'])
    player = GlitchyMediaPlayer('test_video.txt')
    
    with patch('builtins.print') as mock_print:
        player.apply_distortion(frame)
        assert mock_print.call_count == 1

def test_main_no_args(mocker):
    """Test main function with no arguments"""
    mocker.patch('sys.argv', ['script.py'])
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 1

def test_main_with_video_file(mocker):
    """Test main function with video file argument"""
    mocker.patch('sys.argv', ['script.py', 'test_video.txt'])
    player = GlitchyMediaPlayer('test_video.txt')
    with patch.object(player, 'play') as mock_play:
        main()
        assert mock_play.called

# Add more tests as needed
```
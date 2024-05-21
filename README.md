# Text to Music Generator 🎵

This repository contains a Streamlit-based web application that generates music from text descriptions using Meta's Audiocraft library and the MusicGen model.

## Features

- **Text Input**: Enter a textual description of the type of music you want to generate.
- **Duration Control**: Select the duration of the generated music (up to 20 seconds).
- **Music Generation**: Generates music based on the provided description and duration.
- **Audio Playback**: Listen to the generated music directly in the browser.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/text-to-music-generator.git
    cd text-to-music-generator
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv music-env
    source music-env/bin/activate
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

2. **Open your web browser** and go to `http://localhost:8501` to access the app.

3. **Enter a description** of the type of music you want to generate in the text area.

4. **Select the duration** of the music using the slider.

5. **Click "Generate Music"** to create and listen to your music.

## Example

1. Enter a description like "80s pop track with bassy drums and synth".
2. Select a duration, e.g., 10 seconds.
3. Click "Generate Music".
4. Listen to the generated music.

## Requirements

- `streamlit`
- `audiocraft`
- `torchaudio`
- `scipy`

## Project Structure

- `app.py`: The main Streamlit application script.
- `requirements.txt`: The dependencies required to run the app.
- `audios/`: Directory to save generated audio files.

## Contributing

If you have any suggestions or improvements, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgements

- The app uses Meta's [Audiocraft](https://github.com/facebookresearch/audiocraft) library.
- Special thanks to the developers of the [MusicGen model](https://github.com/facebookresearch/audiocraft/blob/main/docs/MUSICGEN.md).

---

Happy music generating! 🎶

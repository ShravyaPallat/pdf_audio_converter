import pyttsx3
import PyPDF2
import os

def select_pdf_file():
    # Ask the user to provide the path to the PDF file
    pdf_path = input("Enter the path to the PDF file: ")
    if os.path.isfile(pdf_path):
        return pdf_path
    else:
        print("File not found. Please enter a valid path.")
        return select_pdf_file()

def select_voice(engine):
    # Get available voices
    voices = engine.getProperty('voices')
    print("Available voices:")
    for index, voice in enumerate(voices):
        print(f"{index}: {voice.name}")

    # Ask the user to select a voice
    voice_index = int(input("Enter the number of the voice you want to use: "))
    if 0 <= voice_index < len(voices):
        engine.setProperty('voice', voices[voice_index].id)
    else:
        print("Invalid selection. Using default voice.")


# Select PDF file
pdf_file_path = select_pdf_file()
pdf_file = open(pdf_file_path, 'rb')
reader = PyPDF2.PdfReader(pdf_file, strict=False)
number_of_pages = len(reader.pages)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Allow the user to select the voice
select_voice(engine)

# Set audio speed and volume
newrate = 200
engine.setProperty('rate', newrate)
newvolume = 1.0  # Volume should be between 0.0 and 1.0
engine.setProperty('volume', newvolume)

# Iterate over selected PDF pages (you can change the range to read more pages)
for i in range(number_of_pages): 
    # Read the PDF page
    page = reader.pages[i]
    # Extract the text from the designated PDF page
    page_content = page.extract_text()
    # Read out the text
    engine.say(page_content)

# Save the audio to a file
engine.save_to_file(page_content, 'pdf_audio.mp3')

# Run and wait for the engine to finish processing
engine.runAndWait()

# Stop the engine
engine.stop()
    
# Close the PDF file
pdf_file.close()



import os
import sys
from mcp.server.fastmcp import FastMCP
import headless_voxnovel
import subprocess

# Initialize FastMCP server
mcp = FastMCP("VoxNovel")

EXCLUDED_VOICE_ACTORS = ['cond_latent_example', '.DS_Store']
CALIBRE_SUPPORTED_FORMATS = ('.cbz', '.cbr', '.cbc', '.chm', '.epub', '.fb2', '.html', '.lit', '.lrf', 
                             '.mobi', '.odt', '.pdf', '.prc', '.pdb', '.pml', '.rb', '.rtf', '.snb', '.tcr')

@mcp.tool()
def list_available_voices() -> str:
    """Lists the current voices available in the system."""
    voice_actors_folder = "Working_files/Voice_Actors"
    if not os.path.exists(voice_actors_folder):
        return "Voice actors folder not found."
    
    voices = []
    voice_actors = [va for va in os.listdir(voice_actors_folder) if os.path.isdir(os.path.join(voice_actors_folder, va)) and va not in EXCLUDED_VOICE_ACTORS]
    for va in voice_actors:
        voice_path = os.path.join(voice_actors_folder, va)
        model_path = os.path.join(voice_path, "model")
        status = ""
        if os.path.exists(model_path) and os.path.isdir(model_path):
            required_files = ["config.json", "model.pth", "vocab.json_"]
            existing_files = os.listdir(model_path)
            if all(file in existing_files for file in required_files):
                status = " (Fine-tuned XTTS model available)"
            else:
                status = " (Incomplete XTTS model)"
        voices.append(f"{va}{status}")
        
    return "Voices available:\n" + "\n".join(voices)

@mcp.tool()
def convert_and_process_ebook(file_path: str) -> str:
    """
    Converts and processes an ebook file, extracting chapters, generating text,
    and creating the required CSV files for audio generation.
    """
    if not os.path.exists(file_path):
        return f"Error: File {file_path} not found."
        
    if file_path.lower().endswith(CALIBRE_SUPPORTED_FORMATS):
        try:
            if headless_voxnovel.calibre_installed():
                file_path = headless_voxnovel.convert_with_calibre(file_path)
            else:
                return "Error: Calibre is required to convert this ebook format, but it is not installed."
        except Exception as e:
            return f"Error converting ebook: {str(e)}"
            
    try:
        if file_path.lower().endswith('.epub'):
            headless_voxnovel.convert_epub_and_extract_chapters(file_path)
            headless_voxnovel.process_chapter_files("Working_files/Book/Chapter_txt_files", "Working_files/Book/book.csv")
            return f"Successfully processed epub: {file_path}"
        elif file_path.lower().endswith('.txt'):
            import shutil
            os.makedirs("Working_files/Book", exist_ok=True)
            shutil.copy(file_path, "Working_files/Book/book.txt")
            # Directly processes the csv generated from the txt
            headless_voxnovel.process_and_split_csv("Working_files/Book/book.csv", 'NEWCHAPTERABC')
            return f"Successfully processed text file: {file_path}"
        else:
            return "File format not supported for direct processing. Try epub or txt."
    except Exception as e:
        return f"Error processing file: {str(e)}"

@mcp.tool()
def run_audio_generation() -> str:
    """
    Runs the auto_noGui_run.py script which handles the end-to-end audio generation 
    with zero human interaction, processing whatever is in the Working_files.
    """
    try:
        # Run auto_noGui_run.py
        result = subprocess.run(
            [sys.executable, "auto_noGui_run.py"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            lines = result.stdout.splitlines()[-20:] if result.stdout else []
            return "Audio generation completed successfully.\n" + "\n".join(lines)
        else:
            return f"Audio generation failed.\nError: {result.stderr}"
    except Exception as e:
        return f"Failed to execute audio generation: {str(e)}"

if __name__ == "__main__":
    # Start the MCP server using stdio transport
    mcp.run()

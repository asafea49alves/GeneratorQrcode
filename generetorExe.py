from PyInstaller.__main__ import run

if __name__ == "__main__":
    run([
        '--onefile',
        '--name=GeneratorImage',
        'GeneratorImage.py'
    ])
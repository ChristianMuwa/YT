import typer
from ytube_api import Auto



def main(
        media: str, 
        mp3: bool = False, 
        mp4: bool = False,
        mp3_quality: int = 128,
        mp4_quality: int = 360
        ):
    """
    Download music from YouTube in mp3 and mp4 

    use --mp3 and --mp4 flags to download in the percepective format



    """
# if --mp3 is given and a --mp3-quality
    if mp3:
        Auto(
            query = media,
            format = 'mp3',
            quality = str(mp3_quality)
        )
    
    elif mp4:
        mp3 = False
        Auto(
            query = media,
            format = 'mp4',
            quality = str(mp4_quality)
        )
    # default
    else:
        Auto(
            query = media,
            format = 'mp3',
            quality = str(mp3_quality)
        )

def cli():
    typer.run(main)

if __name__ == "__main__":
    typer.run(main)

